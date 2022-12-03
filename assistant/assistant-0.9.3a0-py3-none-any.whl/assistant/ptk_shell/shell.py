import sys, os
import asyncio
import colorama
import math
import toml
#from man_explain import print_man_page_explan

#print("Preparing shell...")
sys.path.insert(0, os.path.abspath('..'))
from time import sleep
from typing import Tuple, Sequence, Optional
from xonsh.ptk_shell.shell import PromptToolkitShell
from xonsh.execer import Execer
from xonsh.tools import XonshError
from xonsh.built_ins import XSH
import builtins
from asyncio import Future, ensure_future
#from assistant.execution_classifier import ExecutionClassifier
from prompt_toolkit import HTML
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.layout.containers import HSplit, Float
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import clear
from prompt_toolkit.widgets import MenuItem
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.application import Application
from prompt_toolkit.filters import Condition
from prompt_toolkit.shortcuts import CompleteStyle

from terminaltables import SingleTable

from assistant import *
#from assistant.completer import word_completer
from assistant.bindings import bindings
from assistant.rasa.nlp import AgentRasaInterface
from assistant.parser import AssistantParser
from assistant.strformat_utils import get_highlighted_text, get_only_text_in_intervals
from assistant.icons import *
from assistant.windows import get_body, get_buffer_window, get_status_bar, get_inner_scrollable_content, get_scrollable_content
from assistant.floats import get_float_item_list
#from assistant.completer import word_completer
from assistant.styles import style_generator
from assistant.layout import get_layout
from assistant.dialogs import MessageDialog, TextInputDialog
from assistant.as_client import is_assistant_up, is_auth_to_listen, is_allowed_to_speak, query, nlp_intent_exit
import assistant.execer



builtin_dict = {}
exit_please = ["/exit", "exit", "exxit", "quit", ":q", "Q", "q", "exit()", "quit()", "stop", "stop()", "terminate", "bye", "bye-bye"]

class AssistantShell(Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.full_screen = True
        #self.refresh_interval = 1
        self.parser = AssistantParser()
        #self.language = XSH.env.get('I18N', "en")
        #self.kernel_interface = AgentRasaInterface()
        #self.exec_classifier = ExecutionClassifier()
        self.exec_function = assistant.execer.execute

        self.float_item_list = get_float_item_list()
        self.menu_items_list = [
            MenuItem(
                "[Assistant]",
                children=[
                    MenuItem(INFO_ICON + " About", handler=self.do_about),
                    MenuItem(SETTINGS_ICON + " Settings", handler=self.do_settings),
                    MenuItem("-", disabled=True),
                    MenuItem(EXIT_ICON + " Quit", handler=self.do_exit),
                    #MenuItem(SLEEP_ICON + " Sleep", handler=self.do_exit),
                    #MenuItem(SHUTDOWN_ICON + " Shutdown", handler=self.do_exit),
                    #MenuItem(REBOOT_ICON + " Reboot", handler=self.do_exit),
                ],
            ),
            MenuItem(
                "[Interface]",
                children=[
                    MenuItem(MIC_ICON + " Toggle STT", handler=self.do_toggle_listen),
                    MenuItem(SPEAK_ICON + " Toggle TTS", handler=self.do_toggle_speak),
                ],
            ),
            MenuItem(
                "[Help]",
                children=[
                    MenuItem(MANUAL_ICON + " Manual", handler=self.do_manual),
                    MenuItem(HELP_ICON + " How can my Assistant help me?",
                            handler=self.do_how_help),
                    MenuItem("Keyboard Shortcuts", self.do_shortcuts)
                ]
            )
        ]
        self.status_bar = get_status_bar(is_assistant_up(), is_auth_to_listen(), is_allowed_to_speak())
        self.buff = Buffer(
                #completer=word_completer,
                complete_while_typing=True,
                name="Input Buffer",
                auto_suggest=AutoSuggestFromHistory(),
                #history=history.PtkHistoryFromXonsh(xhistory=history.XonshJsonHistory(sessionid=history.get_current_xh_sessionid(Path(XSH.env.get('XONSH_DATA_DIR'))))),
                enable_history_search=True,
            )
        self.buffer_window = get_buffer_window(self.buff)
        self.inner_scrollable_content = get_inner_scrollable_content(self.status_bar, self.buffer_window)
        self.scrollable_content = get_scrollable_content(self.inner_scrollable_content)
        self.body = get_body(self.scrollable_content)

        self.exit_screen = False

        @bindings.add("c-c")
        @bindings.add("c-q")
        def _(event):
            "Quit when [Control] + ([Q] or [C]) is pressed."
            #PROC.kill()
            #self.exit()
            self.do_exit()

        @Condition
        def buffer_has_focus():
            if self:
                if self.layout.buffer_has_focus:
                    return True
            return False

        @bindings.add('c-m', filter=buffer_has_focus)  # [Enter]
        async def _(event):
            " Those keys play multiple roles trought the UI. "
            prompt_buffer = event.app.layout.current_buffer

            data = prompt_buffer.text
            #print(data)
            prompt_buffer.reset(append_to_history=True)
            
            if data.lower() in exit_please: #user can type exit to exit.
                self.do_exit()
            elif data.lower() in ["version", "about"]:
                self.do_about()
            elif data:
                r = await self.interpret_command(data)
                #print(f"Recieved answer: {r}")
                if r:
                    if "/exit" in r.lower().split("\n"): #user can ask assistant to exit
                        #print("Answer is exit: exiting...")
                        self.do_exit()
                    elif r and not is_assistant_up():
                        self.show_message("Services are down", r)
        
        self.bindings = bindings

        self.layout = get_layout(self.body, self.menu_items_list, self.float_item_list, self.bindings, self.buffer_window)

        self.style = style_generator()
        #self.state = ApplicationState(**kwargs)

    def do_exit(self):
        self.exit_screen = True
        print(nlp_intent_exit())
        sys.exit(0)


    def do_about(self):
        self.show_message("About this Assistant",
                    "Assistant version %s.\nCreated with love by Danny Waser." % str(__version__))


    def do_settings(self):
        self.show_message("Settings", "Sorry but settings are not yet implemented.")


    def do_manual(self):
        self.show_message("Manual", "If you want to use the voice interface use:\n [Ctrl] + [S] to toggle Text-To-Speech (TTS)\n [Ctrl] + [L] to toggle Speech-To-Text (STT)")

    def do_shortcuts(self):
        kbshortcuts = [
            "<b>[Tab]</b> -> Focus next element",
            "<b>[Ctrl] + [A]</b> -> Open menu <i><u>A</u>ssistant</i>",
            "<b>[Ctrl] + ([Q] or [C])</b> -> <u>Q</u>uit",
        ]
        kbshortcuts_txt = HTML("\n".join(kbshortcuts))
        self.show_message("Keyboard Shortcuts", kbshortcuts_txt)

    def do_how_help(self):
        self.show_message("How can I help?", "Ask me anything, I'll help you. Promise.")

    def do_open_data(self):
        self.do_open_nautilus_location("/home/%s/.assistant" % USERNAME)

    def do_show_abspath(self):
        self.show_message("Absolute Path", PWD)
    
    def load_conf(self, conf_path):
        with open(conf_path, 'r') as f:
            return toml.load(f)

    def save_conf(self, conf, conf_path):
        with open(conf_path, 'w') as f:
            toml.dump(conf, f)

    def toggle_conf(self, conf_path, service_name):
        if os.path.exists(conf_path):
            c = self.load_conf(conf_path)
            is_allowed = "is_allowed"
            c[service_name][is_allowed] = not c.get(service_name, {is_allowed: False}).get(is_allowed, False)
            self.save_conf(c, conf_path)
        else:
            self.show_message("Service Configuration Missing", f"Missing service config at {conf_path}.\nRun the service once to create a default conf.")
    
    def do_toggle_speak(self):
        #p = self.ask_password('Type your password', 'Let me check everything is ready.\nEnter your password.')
        # if os.path.isfile('/usr/lib/systemd/system/multi-user.target.wants/speak.service'):
        #     os.system(f"systemctl disable --now speak.service &>/dev/null")
        # else:
        #     if not os.path.isfile('/usr/lib/systemd/system/speak.service'):
        #         os.system(f"wget 'https://gitlab.com/waser-technologies/technologies/say/-/raw/main/speak.service.example' &>/dev/null && mv speak.service.example /usr/lib/systemd/system/speak.service &>/dev/null")
        #     os.system(f"systemctl enable --now speak.service &>/dev/null")
        
        # Just edit toml config
        s = "tts"
        self.toggle_conf(f"{ASSISTANT_PATH}/{s}.conf", s)
    
    def do_toggle_listen(self):
        # Assistant
        #p = self.ask_password('Type your password', 'Let me check everything is ready.\nEnter your password.')
        # if os.path.isfile('/usr/lib/systemd/user/default.target/assistant.listen.service'):
        #     os.system(f"systemctl --user disable --now assistant.listen.service &>/dev/null")
        # else:
        #     if not os.path.isfile('/usr/lib/systemd/user/assistant.listen.service'):
        #         os.system(f"wget 'https://gitlab.com/waser-technologies/technologies/assistant/-/raw/main/assistant.listen.service.example' &>/dev/null && mv assistant.listen.service.example /usr/lib/systemd/user/assistant.listen.service &>/dev/null")
        #     os.system(f"systemctl --user enable --now assistant.listen.service &>/dev/null")
        # # Listen
        # if os.path.isfile('/usr/lib/systemd/system/multi-user.target.wants/listen.service'):
        #     os.system(f"systemctl disable --now listen.service &>/dev/null")
        # else:
        #     if not os.path.isfile('/usr/lib/systemd/system/listen.service'):
        #         os.system(f"wget ''https://gitlab.com/waser-technologies/technologies/say/-/raw/main/listen.service.example' &>/dev/null && mv listen.service.example /usr/lib/systemd/system/listen.service &>/dev/null")
        #     os.system(f"systemctl enable --now listen.service &>/dev/null")
        
        # Just edit toml config
        s = "stt"
        self.toggle_conf(f"{ASSISTANT_PATH}/{s}.toml", s)

    def do_open_nautilus_location(location: str):
        p = subprocess.Popen(["/usr/bin/nautilus", location],
                            stdout=subprocess.PIPE)
        # p.communicate()
        return True

    def do_open_location(self):
        return do_open_nautilus_location(PWD)

    def show_message(self, title, text):
        async def coroutine():
            dialog = MessageDialog(title, text)
            await self.show_dialog_as_float(dialog)

        ensure_future(coroutine())

    def show_single_choice(self, title, text, values):
        results = None

        async def coroutine():
            dialog = RatioListDialog(title, text, values)

            await show_dialog_as_float(dialog)

            self.state.active_menu_data = dialog
        ensure_future(coroutine())

    async def show_dialog_as_float(self, dialog):
        "Coroutine."
        float_ = Float(content=dialog)
        self.layout.container.floats.insert(0, float_)
        focused_before = self.layout.current_window
        self.layout.focus(dialog)
        result = await dialog.future
        self.layout.focus(focused_before)

        if float_ in self.layout.container.floats:
            self.layout.container.floats.remove(float_)

        return result

    def redraw_app(self):
        if self.layout.buffer_has_focus:
            self.status_bar = get_status_bar(is_assistant_up(), is_auth_to_listen(), is_allowed_to_speak())
            self.inner_scrollable_content = get_inner_scrollable_content(self.status_bar, self.buffer_window)
            self.scrollable_content = get_scrollable_content(self.inner_scrollable_content)
            self.body = get_body(self.scrollable_content)
            self.layout = get_layout(self.body, self.menu_items_list, self.float_item_list, self.bindings, self.buffer_window)
            #self.app.layout = self.layout
            #self.app.layout.focus(self.inner_scrollable_content)
            self.invalidate()
            #self.app.layout.focus(self.buffer_window)

    def pyexec(self, code):
        # Some very dangerous code here.
        # (tries to) execute python code straight from the user input
        try:
            exec('global __pyexec_global__; __pyexec_global__ = %s' % code)
            global __pyexec_global__
            return f"{__pyexec_global__}\n"
        except (
            SyntaxError,
            OverflowError,
            ValueError,
            NameError,
            Exception
        ) as error:
            return None

    def xexec(self, parsed_code):
        return self.exec_function(parsed_code)

    async def interpret_command(self, command: str):
        parse = self.parser.parse(command)
        response = None

        try:
            if is_assistant_up():
                upr = await query(command, XSH.env.get('USERNAME', os.environ.get("USERNAME", 'user')))
                if upr:
                    response = str(upr) + "\n"
                else:
                    # add to no intent
                    response = self.pyexec(command) or self.xexec(parse) or None
            else:
                response = f"Assistant: Service is unreachable.\nType:\n  systemctl --user enable --now dmt assistant\nOr manually in other shell sessions using dmt:\n  dmt --serve\n  python -m assistant.as_service\nTo enable them.\n{self.pyexec(command) or self.xexec(parse) or ''}"
        except Exception as e:
            if XSH.env.get('DEBUG', False):
                raise e
            else:
                raise e
                response = str(e) + "\n"
        
        return response

    async def cmdloop(self, intro=None):
        """Enters a loop that reads and execute input from user."""
        if intro:
            print(intro)
        auto_suggest = AutoSuggestFromHistory()
        while not __xonsh__.exit:
            try:
                line = self.singleline(auto_suggest=auto_suggest)
                if not line:
                    self.emptyline()
                elif line in exit_please:
                    e = nlp_intent_exit()
                    if e:
                        print(e)
                    __xonsh__.exit = True
                    break
                elif line == "clear":
                    clear()
                else:
                    r = await self.interpret_command(line)
                    if r and r != "None":
                        print(r, end='')
            except (KeyboardInterrupt, SystemExit):
                self.reset_buffer()
            except EOFError:
                if __xonsh__.env.get("IGNOREEOF"):
                    print('Use allowed "exit words" to leave the shell.', file=sys.stderr)
                    print(exit_please)
                else:
                    break


