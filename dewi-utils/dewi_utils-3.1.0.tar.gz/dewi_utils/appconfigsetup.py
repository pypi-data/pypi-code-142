# Copyright 2009-2021 Laszlo Attila Toth
# Distributed under the terms of the Apache License, Version 2.0
# vim: sts=4 ts=8 et ai


import typing

import aenum

from dewi_core.config.appconfig import get_config
from dewi_core.config.iniconfig import convert_from_bool, convert_to_bool
from dewi_utils.config_page import ConfigPage


class ConfigStep(aenum.Enum):
    CORE = (1, 'Core Settings')

    def __init__(self, index: int, title: str):
        self.index = index
        self.title = title

    def __lt__(self, other):
        return isinstance(other, ConfigStep) and self.index < other.index

    def __gt__(self, other):
        return isinstance(other, ConfigStep) and self.index > other.index

    @classmethod
    def extend(cls, new_step_name: str, title: str):
        return aenum.extend_enum(cls, new_step_name, (cls.max_index() + 1, title))

    @classmethod
    def max_index(cls) -> int:
        return max([x.index for x in cls])


class InputType(aenum.IntEnum):
    BOOL = 1
    INPUT = 2
    PASSWORD = 3


class Q:
    """
    Defines an interactive question.

    Mostly the fields are straightforward, some controls the config setup (skip_*), and the `internal_label`
    and `section` are to override calculated fields.

    The 'option' parameter - field - is optional, can be None, indicating that the question doesn't have
    an app config entry, but it's used to control the config setup, like asking if git setup is needed or not.

    The config setup stores the values in a dict, so each question must have a unique name. Mostly this can be
    calculated from the step name and the option, but sometimes it's either not provides the expected result,
    or not possible (due to the lack of option) or the exact name is important. The `internal_label` can be
    used in these cases.

    Also the 'section' is calculated from the step's name for simplicity. Sometimes the step should be different
    than the 'section' as the step has more meaningful name. An example: the 'core' section may contain both
    the 'basedir' and the credentials to access some parts of the required infrastructure. A dedicated step
    for the credentials might be a better option, so the 'section' field is necessary.

    As the default ConfigStep contains only a single step, in a complete application the ConfigStep should
    be extended.

    Some of the questions may be irrelevant based on earlier inputs.

    For the fields please refer the __init__() method.
    """

    def __init__(self, step: ConfigStep,
                 input_type: InputType,
                 option: typing.Optional[str],
                 default_value: typing.Union[str, bool],
                 title: str,
                 help: str,
                 *,
                 internal_label: typing.Optional[str] = None,
                 skip_if_true: typing.Optional[str] = None,
                 skip_if_false: typing.Optional[str] = None,
                 section: typing.Optional[str] = None,
                 ):
        """
        Defines a question.

        :param step: A ConfigStep enum value (probably differs from ConfigStep.Core)
        :param input_type: Defines how the answer can be provided
        :param option: The name of the app config
        :param default_value: If the config doesn't contain the field, this value is used
        :param title: The question's title, which is also in the input prompt
        :param help: A comprehensive description to shown if help is needed at this question
        :param internal_label: Overrides the calculated label used in the config setup
        :param skip_if_true: An internal label; Skip this question if
                             the answer of internal label `value of skip_if_true` evaluates to True
        :param skip_if_false: An internal label; Skip this question if
                              the answer of internal label `value of skip_if_true` evaluates to False
        :param section: Overrides the calculated section name (which is the lowercase form of the step's name)
        """
        self.step = step
        self.input_type = input_type
        self.section = section or self.step.name.lower()
        self.option = option
        self.default_value = default_value
        self.title = title
        self.help = help
        self.internal_label = internal_label or f'{self.step.name.lower()}-{self.option}'
        self.skip_if_true = skip_if_true
        self.skip_if_false = skip_if_false


class PrivQ(Q):
    """
    Internally used question without app config entry.
    The section and option fields cannot be specified and the internal_label field is mandatory.
    Otherwise the same as the parent Q class.
    """

    def __init__(self, step: ConfigStep,
                 input_type: InputType,
                 default_value: typing.Union[str, bool],
                 title: str,
                 help: str,
                 *,
                 internal_label: typing.Optional[str],
                 skip_if_true: typing.Optional[str] = None,
                 skip_if_false: typing.Optional[str] = None,
                 ):
        super().__init__(step, input_type, None, default_value, title, help, internal_label=internal_label,
                         skip_if_true=skip_if_true, skip_if_false=skip_if_false)


BASEDIR_Q = Q(ConfigStep.CORE, InputType.INPUT, 'basedir', '~/workspace',
              'Basedir of projects and app-specific files',
              'The base directory for every command related to projects. '
              'The subdirectories: projects/ (after the use of any project-based command), '
              'and others which are recommended only for an app: src/bare/ for bare repositories if '
              'git worktrees are used; etc/ for different project-global settings, e.g. common dependency list or so. '
              'Please consult with the documentation of the application.'),


class AppConfigSetup:
    def __init__(self,
                 questions: typing.List[Q],
                 config_path: str,
                 *,
                 incremental: bool = False
                 ):
        self._questions = questions
        self._config_path = config_path
        self._incremental = incremental  # if True, only new options should be asked

        self._new_options = []  # since last setup (internal names)
        self._old_options = []  # internal names
        self._bool_option_names = []  # internal names

        self._config_map = dict()  # internal name -> config value map
        self._question_map = dict()  # internal name -> Q map

    def _is_print_only(self, name: str):
        return self._incremental and name in self._old_options

    def _ask_input(self, prompt, name, default_value='', password=False, help=None, ):
        if name in self._config_map:
            default_value = self._config_map[name]
        answer = ConfigPage(prompt, help).input(default_value, print_only=self._is_print_only(name), password=password)
        self._config_map[name] = answer

    def _ask_yesno(self, prompt, name, default_value=True, help=None):
        if name in self._config_map:
            default_value = convert_to_bool(self._config_map[name])
        answer = ConfigPage(prompt, help).yesno(default_value, print_only=self._is_print_only(name))
        self._config_map[name] = answer

    def setup(self):
        self._load_config()
        self._load_additional_config()
        self._prepare_questions()
        self._ask_questions()
        self._process_answers()
        self._save_config()

    def _load_config(self):
        get_config(self._config_path)

    def _load_additional_config(self):
        """
        Loads additional parts of config into _config_map. Eg. username and email for git setup from ~/.gitconfig
        """

        # In this class: NOOP
        pass

    def _prepare_questions(self):

        for q in self._questions:
            self._question_map[q.internal_label] = Q
            self._load_question_from_app_config(q)

    def _load_question_from_app_config(self, q: Q):
        if q.input_type == InputType.BOOL:
            self._bool_option_names.append(q.internal_label)
        if q.option is None:
            return

        item = get_config().get(q.section, q.option)
        if item:
            if q.input_type in (InputType.INPUT, InputType.PASSWORD):
                self._config_map[q.internal_label] = item
            else:
                self._config_map[q.internal_label] = convert_to_bool(item)

    def _ask_questions(self):
        step_q_map: typing.Dict[ConfigStep, typing.List[Q]] = {}
        for step in ConfigStep:
            step_q_map[step] = []

        for question in self._questions:
            step_q_map[question.step].append(question)

        for step in ConfigStep:
            print(f"\nConfiguring {step.index} of {len(ConfigStep)}: {step.title}")

            if not step_q_map[step]:
                continue

            for q in step_q_map[step]:
                if q.skip_if_false and not self._config_map[q.skip_if_false]:
                    continue
                if q.skip_if_true and self._config_map[q.skip_if_true]:
                    continue
                if q.input_type == InputType.BOOL:
                    self._ask_yesno(q.title, q.internal_label, q.default_value, q.help)
                elif q.input_type == InputType.PASSWORD:
                    self._ask_input(q.title, q.internal_label, q.default_value, password=True, help=q.help)
                else:
                    self._ask_input(q.title, q.internal_label, q.default_value, help=q.help)

    def _process_answers(self):
        """Process the answers which may not be in the config (eg. git setup)"""
        pass

    def _save_config(self):
        app_config = get_config()
        for label, value in self._config_map:
            q = self._question_map[label]
            if q.option is None:
                continue
            if q.ctype == InputType.BOOL:
                value = convert_from_bool(value)
            app_config.set(q.section, q.option, value)
        app_config.write(self._config_path)
