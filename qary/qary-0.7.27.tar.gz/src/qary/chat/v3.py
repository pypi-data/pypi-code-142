# qary.chat.v3
r"""

Engine(states='*.v3.dialog.yml') loads dialog tree definition file

recognize_intent():

  Inputs:
    lang (str): e.g. 'en', 'zh', 'es'
    state name (str): e.g. 'language-selected-english'
    user utterance (str): 'Hello chatobt'
  Outputs:
    id (str): state name
    text: bot utterance

Engine().run(user_text, **context):

  Inputs:
    user_text (str): what user said last
    context (dict): nested dict of everything the bot knows (`lang`, `user_text`, `state_name` etc)
  Outputs:
    context (dict): whatever the bot know after extracting the intent and running any of the associated bot actions.


>>> e = Engine()
>>> e.states[e.context['state_name']]['actions']['en']
'Hello, my name is POLY - short for Polyglot, ...... like me to help you in:\n'
>>> context = e.run(user_text='English')
>>> context['state_name']
'selected-language-welcome'
>>> context['bot_text']
'I\'m part of the Let\'s Talk NYC team and I\'m here to help you learn ... Select "Yes" when ready\n'

>>> state_name = e.context['state_name']
>>> state_name
'selected-language-welcome'
>>> e.states[state_name]
{'name': 'selected-language-welcome', 'level': 1, 'actions': {'en': ... 'iloc': 1}
"""

from collections import abc
import io
import logging
from pathlib import Path
from qary.init import maybe_download
import time
import yaml

import numpy as np
import pandas as pd

log = logging.getLogger('qary')
logging.basicConfig(level=logging.DEBUG)

EXAMPLE_V3_DIALOG_TREE_FILEPATH = maybe_download(filename='chat/example-multilingual.v3.dialog.yml')
WELCOME_STATE_NAME = '__WELCOME__'
DEFAULT_LANG = 'en'
EMPTY_DIALOG_TREE = pd.Series({
    WELCOME_STATE_NAME:
        {'name': WELCOME_STATE_NAME,
         'actions':
            {'en': "I have nothing to say ;-) (My v3 dialog tree is empty)"},
         'triggers':
            {'en': {"": WELCOME_STATE_NAME}},
         }
})


# this is the canonical dialog v3 data structure (pd.Series containing dicts):


def coerce_dialog_tree_series(
    states: (str, Path, abc.Mapping, io.TextIOWrapper, pd.Series, list, np.ndarray, tuple, pd.Series)
):
    """ Ensure that (yamlfilepath | list) -> dict -> Series

    >>> states = coerce_dialog_tree_series(EXAMPLE_V3_DIALOG_TREE_FILEPATH)
    >>> type(states)
    Series
    """
    if isinstance(states, pd.Series):
        return states
    if isinstance(states, (list, np.ndarray, tuple)):
        states = pd.Series(
            states,
            index=[s.get('name', str(i)) for (i, s) in enumerate(states)])
        states.index.name = 'name'
        return states
    if isinstance(states, (str, Path)):
        with Path(states).open() as fin:
            return coerce_dialog_tree_series(yaml.full_load(fin))
    if isinstance(states, io.TextIOWrapper):  # opened file mode='rt'
        return coerce_dialog_tree_series(yaml.full_load(states))
    if isinstance(states, abc.Mapping):
        return pd.Series(states)
    if states is None:
        return EMPTY_DIALOG_TREE
    raise ValueError(
        f"Unable to coerce {type(states)} into pd.Series:\n  states={str(states)[:130]}..."
    )


# TODO see ISO_LANG codes in constants for nessvec or qary package
LANGS = {
    'en': 'en',
    'english': 'en',
    'es': 'es',
    'spanish': 'es',
    'zh': 'zh',
    'chinese': 'zh',
}


def normalize_state_name(name, state_names=None):
    if isinstance(name, int):
        if state_names is None:
            name = str(name)
        else:
            return state_names[name]
    if isinstance(name, str):
        return name.strip().lower()


def normalize_user_text(text):
    return str(text).strip().lower()


def normalize_intent_texts(states):
    for name, state in states.items():
        for lang, intents in state.get('triggers', {}).items():
            states[name]['triggers'][lang].update({
                normalize_user_text(i): v for (i, v) in intents.items()
            })
    return states


def update_node_with_buttons(node, **context):
    """ Use lang in context dict to add button text to bot_text attribute of node """
    lang = context.get('lang', DEFAULT_LANG)
    log.debug(node)
    lang_buttons = node.get('buttons', {})
    node['actions_with_buttons'] = {}
    for lang, buttons in lang_buttons.items():
        if isinstance(buttons, str):
            buttons = [buttons]
        buttons = list(buttons)

        log.debug('=' * 80)
        log.debug(f'Updating bot_text for "{lang}" in node named "{node["name"]}" with {len(buttons)} buttons')
        bot_text = node['actions'].get(lang, '')
        for button_text in buttons:
            bot_text += f'\n  > {button_text}'
        log.debug(bot_text)
        log.debug('=' * 80)
        node['actions_with_buttons'][lang] = bot_text
    log.debug(node)
    return node


def update_state_series_with_buttons(states):
    states = coerce_dialog_tree_series(states)
    for i, node in states.items():
        states[i] = update_node_with_buttons(node)
    return states


def update_state_list_with_buttons(states):
    for i, node in enumerate(states):
        states.iloc[i] = update_node_with_buttons(node)
    states = coerce_dialog_tree_series(states)
    return states


EXAMPLE_DIALOG_TREE = coerce_dialog_tree_series(states=EXAMPLE_V3_DIALOG_TREE_FILEPATH)
EXAMPLE_DIALOG_TREE_DICT = EXAMPLE_DIALOG_TREE.to_dict()
EXAMPLE_DIALOG_TREE_SERIES = EXAMPLE_DIALOG_TREE


def preprocess_dialog_tree_series(states=EXAMPLE_DIALOG_TREE):
    """ Ensure that all dialog tree index values are normalized strs: Series.index.str.lower().str.strip()."""

    states = coerce_dialog_tree_series(states)
    log.debug(f"\nLoaded {len(states)} states with names:\n{list(states.index)}")

    states = update_state_series_with_buttons(states)
    states = normalize_intent_texts(states)

    # make sure state['name'] is used to overwrite the index
    states.index = [normalize_state_name(s.get('name', i)) for (i, s) in states.items()]
    states.index.name = 'name'

    is_dupe = states.index.duplicated()
    if sum(is_dupe) > 0:
        log.error(f'State pd.Series contains {sum(is_dupe)} duplicate index values!\n'
                  f'The following duplicates will be deleted:\n{states.index[is_dupe].to_series()}'
                  )
    states = pd.Series(states[~is_dupe])
    states_list = []
    for i, (idx, s) in enumerate(states.items()):
        s = dict(s)
        s['name'] = str(idx)
        s['iloc'] = i
        states_list.append((idx, s))

    states = pd.Series(dict(states_list))
    log.debug(f"\nLoaded {len(states)}\nstates with names:\n{list(states.index)}")
    return states


def await_timeout(seconds=0, milliseconds=0):
    time.sleep(seconds + milliseconds / 1000.0)


def on_answer_noop(*args, **kwargs):
    log.debug('User action was a NOOP!!!!')
    log.debug(f'  NOOP\nargs: {args}\nkwargs={kwargs}')


class Engine:  # Engine(pd.Series)
    """ A state machine designed for managing the dialog for a rule-based chatbot

    >>> e = Engine()
    >>> context = e.run(user_text='Chinese')
    >>> context['state_name']
    'selected-language-welcome'
    >>> context = e.run(user_text='yes')
    >>> context['state_name']
    'selected-language-welcome'
    >>> context = e.run(user_text="是")
    >>> context['state_name']
    'is-this-your-first-time'
    """

    def __init__(self, states=EXAMPLE_V3_DIALOG_TREE_FILEPATH, **context):
        self.states = coerce_dialog_tree_series(states=EXAMPLE_V3_DIALOG_TREE_FILEPATH)
        self.states = preprocess_dialog_tree_series(self.states)
        self.history = []
        self.context = {}
        if 'state_name' not in context:
            context['state_name'] = self.states.index.values[0]
        if 'lang' not in context:
            context['lang'] = DEFAULT_LANG
        self.run(**context)
        log.info(f'self.context.get("state_name"): {self.context.get("state_name")}')
        log.info(f'return None in Engine.__init__().')

        # Unused side-effect
#         actions = self.states[state_name]['actions']
#         actions_with_buttons = self.states[state_name]['actions_with_buttons']
#         self.bot_text_with_buttons = actions_with_buttons.get(lang, actions[lang])

    def run(self, **context_changes):
        r""" Move to next state(s) based on user action/text and return the context_changes (new state & bot_text)

        Update self.context with context_changes dict and append context to history

        Inputs:
          user_text (str): whatever message user typed for the current state_name
          state_name (str): skip the current state and go to state_name before processing user_text
          lang (str): en, zh, zht, es, etc

        Returns dict(
          name="name-of-new-state",
          bot_text="Whatever the bot should say in response to this user action or message.",
          lang="en"|"es"|"zh"|... ,
          )

        FIXME: Inifinite loop:
        >>> e = Engine()
        >>> context = e.run(user_text='en')
        """
        log.info(f'Engine.run(context_changes={context_changes})')
        # special context variables (state_name & lang) have their own set_* methods:
        # FIXME:
        #    * create a FIFO user_action_queue and push user_text and context changes into it
        #    * bot processes the context changes FIFO but schedules its own actions with RedEngine/Celery/RMQ

        # Pop actions from context_changes dict in correct order,
        #     execute each bot action required
        #     return dict of accomplished action outputs (echo of context_changes implemented)

        # 1. update language first
        bot_todo_list = []  # list of dicts (context changes)
        bot_actions = {}    # context changes dict
        if 'lang' in context_changes:
            lang = context_changes.pop('lang')
            bot_actions['lang'] = lang
            self.set_lang(lang)
            log.debug(f'Engine.run(lang={lang}) => self.context["lang"]: {self.context["lang"]}')

        # 2. respond to the state_name change input first (but don't utter the associated bot text!
        if 'state_name' in context_changes:
            skipped_to_state_name = self.set_state_name(context_changes.pop('state_name'))
            bot_actions['state_name'] = skipped_to_state_name
            # FIXME: do states have 'actions' key with list of bot utterances?
            self.set_state_name(skipped_to_state_name)
            log.info(f"state: {self.states[self.context['state_name']]}")
            bot_text = self.states[self.context['state_name']]['actions'][self.context['lang']]
            bot_actions['bot_text'] = bot_text

        if bot_actions:
            bot_todo_list.append(bot_actions)
            bot_actions = {}

        # 3. implement state changes triggered by user_text
        if 'user_text' in context_changes:
            user_text = context_changes.pop('user_text')
            self.context['user_text'] = user_text
            self.context.update(self.do_user_intent(self.context))
            bot_actions['user_text'] = user_text
            bot_actions['state_name'] = self.detect_trigger(user_text=user_text)
            # FIXME: do states have 'actions' key with list of bot utterances?
            self.set_state_name(bot_actions['state_name'])
            actions = self.states[self.context['state_name']]['actions']
            bot_actions['bot_text'] = actions.get(self.context['lang'])
            if bot_actions['bot_text'] is None:
                log.error(f"No bot text (action) found for lang {self.context['lang']} among actions.keys(): {actions.keys()}")
                bot_actions['bot_text'] = actions.get(DEFAULT_LANG)
            # TODO make sure preprocessing creates bot text for all states and the DEFAULT_LANG
            assert bot_actions['bot_text'] is not None

        context_changes_done = self.record_bot_actions(bot_todo_list)
        if bot_actions:
            bot_todo_list.append(bot_actions)
            bot_actions = {}

        assert not context_changes, f"all context_changes failed to transfer {context_changes} to bot_actions self.context.update(s)"
        return context_changes_done

    def record_bot_actions(self, bot_actions):
        context_change_dict = {}
        if isinstance(bot_actions, dict):
            bot_actions = [bot_actions]
        for ba in bot_actions:
            self.history.append(bot_actions)
            context_change_dict.update(ba)
        self.context.update(context_change_dict)
        return context_change_dict

    def get_next_state_name(self):
        r""" Recognize desired state transition trigger and return next_state name

          Inputs:
            lang (str): e.g. 'en', 'zh', 'es'
            state name (str): e.g. 'language-selected-english'
            user utterance (str): 'Hello chatobt'
          Outputs:
            name (str): state name
            text: bot utterance

        >>> eng = Engine()

        FIXME:
        >> eng.get_next_state_name()
        'selected-language-welcome'
        """
        log.info('Engine.get_next_state_name()')
        state_name = self.context['state_name']
        log.debug(f"Trying to find next state after {state_name}")
        # default_response = dict(
        #     state_name=states[0]['name'],
        #     bot_text=states[0].get('actions', {}).get(lang, states[0].get('en', '')),
        #     lang=lang)
        if state_name is None:
            return None
        # if str(state_name).lower().strip() in ('__start__', '__welcome__'):
        #     return default_response
        log.debug('\n' + str(self.states))

        try:
            node = self.states[state_name]
        except KeyError as e:
            log.error(e)
            log.error(f"Invalid state_name '{state_name}'. It is not among states.index:\n  {self.states.index}")

        if state_name != node['name']:
            log.debug(f' states[name]:{node.get("name")} != {state_name}:state_name')

        # detect intent (trigger keys) that match user text message
        return self.detect_trigger()

    def detect_trigger(self, **context_changes):
        """ Detects user_text returns the action_dict (a context_change dict)"""
        log.info('Engine.detect_trigger()')
        node = self.states[self.context['state_name']]
        triggers = node['triggers']
        state_name = self.context['state_name']
        log.debug(f"triggers for state_name {state_name}:\n{triggers}")
        context = self.context

        user_text = context.get('user_text')
        log.debug(f"user_text: {user_text}:")

        buttons_and_intents = self.update_intent_triggers_with_buttons()
        log.debug(f"buttons and triggers keys for state_name {state_name}:\n{buttons_and_intents.keys()}")
        user_text = context.get('user_text', '')

        next_state_name = None
        # default to first intent if not a valid intent
        if user_text not in buttons_and_intents:
            next_state_name = list(buttons_and_intents.keys())[0]
        else:
            next_state_name = self.set_state_name(buttons_and_intents[user_text])

        if next_state_name is None or next_state_name not in self.states.keys():
            log.error(f"No state change was triggered by user_text {user_text} for state_name {node['name']}!")
            log.error(f"            context:\n     {context}")
            log.error(f"         node/state:\n     {node}")
            log.error(f"buttons_and_intents:\n     {buttons_and_intents}")
            next_state_name = context.get('state_name')
            log.error(f" Remaining in state: {next_state_name}!")

        next_state = self.states.get(next_state_name, node)
    # if 'timeout' in triggers:
        #     if next_state_name:
        #         log.error('Undefined behavior when both timeout and user_text (intent) trigger a state change')
        #     timeout = triggers['timeout']
        #     if isinstance(timeout, dict):
        #         log.debug(f"Awaiting timeout {timeout}")
        #         timeout = list(list(timeout.items())[0])
        #     if isinstance(timeout, (list, tuple)):
        #         await_timeout(seconds=timeout[0])
        #         # DRY this up with user_text trigger match above
        #         next_state_name = self.set_state_name(timeout[1])
        #         state = self.states[next_state_name]
        #         self.execute_actions(state.get('actions'))
        #         # context['bot_text'] = self.states[next_state_name].get('actions', {}).get(context['lang'], '')
        #     # FIXME: this seems useless and an anti-pattern:
        #     elif isinstance(timeout, (float, int)):
        #         await_timeout(timeout)
        return next_state['name']

    def set_state_name(self, state_name=None):
        """ Skip to arbitrary state_name. """
        log.info(f'Engine.set_state_name({state_name})')
        state_name = normalize_state_name(state_name, state_names=self.states.index.values)
        if state_name is None:
            state_name = self.context.get('state_name', self.states.index[0])
        if not state_name and state_name not in self.states.index:
            log.debug(f"New state_name {state_name} not found in states.index")
            state_name = self.states.index[0]
        self.context['state_name'] = state_name
        log.debug(f"Finished setting context['state_name'] = {self.context['state_name']}")
        return state_name

    def set_lang(self, lang=None):
        """ Set context['lang'] to lang, doing nothing if lang is not available """
        log.info(f'Engine.set_lang({lang})')
        if lang is None or lang not in LANGS:
            lang = self.context.get('lang', DEFAULT_LANG)
        self.context['lang'] = lang
        log.info(f"Engine.set_lang({lang}) => .context['lang']={self.context['lang']}")
        return lang

    def normalize_user_text(self, user_text):
        log.info(f'Engine.normalize_user_text("{user_text}")')
        return(str(user_text).lower().strip())

    def update_context(self, context_changes):
        self.context.update(context_changes)

    def do_user_intent(self, context):
        """ with node at context."""
        log.info(f'Engine.do_user_intent(dict(user_text={self.context["user_text"]}, ...))')
        # self.update_context(context_changes)
        user_text = self.context.get('user_text')
        state_name = self.context.get('state_name')
        node = self.states[state_name]
        on_answer_functions = node.get('on_answer', [])
        for fun_name in on_answer_functions:
            fun = globals().get(fun_name, on_answer_noop)
            self.update_context(fun.__call__(context))
        triggers = node.get('triggers', {})
        lang = self.context.get('lang', DEFAULT_LANG)
        intents = triggers[lang]
        user_intent_text = self.normalize_user_text(user_text)
        self.set_state_name(intents[user_intent_text])
        return self.context

    def execute_on_enter_state_actions(self, actions):
        log.info(f'Engine.execute_actions({actions}))')
        if actions is None:
            return
        if 'update_context' in actions:
            self.update_context(actions['update_context'])
        if self.context['extract_lang'] in actions:
            self.update_context(dict(bot_text=actions[self.context['lang']]))
        if self.context['lang'] in actions:
            self.update_context(dict(bot_text=actions[self.context['lang']]))
        return self.context

    def update_intent_triggers_with_buttons(self):
        log.info('Engine.update_intent_triggers_with_buttons()')
        node = self.states[self.context['state_name']]
        triggers = node['triggers']
        buttons = node.get('buttons', {})
        user_intents = triggers.get(
            self.context['lang'], triggers.get(DEFAULT_LANG, {}))  # fallback to English
        log.debug(f"    Triggers for node name {self.context['state_name']} and lang {self.context['lang']}:\n{user_intents}")

        # TODO?: copy.deepcopy(buttons)
        buttons = buttons.get(self.context['lang'], buttons.get('en', {}))  # fallback to English

        # want to check both button text values and user_intent text values
        buttons.update(user_intents)
        buttons_and_intents = buttons
        log.debug(f"    Buttons and intents for node name {self.context['state_name']} and lang {self.context['lang']}:\n{buttons_and_intents}")
        return buttons_and_intents


default_dialog_engine = Engine()


def extract_lang(context):
    # state = context.get('state', {})
    state_name = context.get('state_name', 'unknown-state')
    context[state_name + '.answer'] = context.get('user_text', '')
    return context


def next_state(state_name='select-language', user_text='English', context=None, engine=None):
    """ API example for Greg

    >>> e = Engine()
    >>> context = next_state(state_name='select-language', user_text='English', engine=e)
    >>> context
    {'state_name': 'selected-language-welcome', 'lang': 'en', 'select-language.answer': 'English', 'message_eng': 'English'}    """
    if engine is None:
        engine = Engine()
    context = {} if context is None else context
    context['state_name'] = state_name
    context['user_text'] = user_text

    context2 = engine.do_user_intent(**context)
    context2["message_eng"] = context2.pop("user_text")

    return context2
#    return default_dialog_engine.do_user_intent(**context)
