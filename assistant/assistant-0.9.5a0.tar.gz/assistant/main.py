#! /usr/bin/env python3.8

import os
import sys
import enum
import argparse
import builtins
import contextlib
import signal
import traceback
import asyncio

from prompt_toolkit.shortcuts import clear

from xonsh import __version__
from xonsh.timings import setup_timings
from xonsh.lazyasd import lazyobject
from xonsh.shell import Shell
from xonsh.pretty import pretty
from xonsh.execer import Execer
#from xonsh.proc import HiddenCommandPipeline
from xonsh.jobs import ignore_sigtstp
from xonsh.tools import print_color, to_bool_or_int
from xonsh.platform import HAS_PYGMENTS, ON_WINDOWS
from xonsh.codecache import run_script_with_cache, run_code_with_cache
from xonsh.xonfig import print_welcome_screen
from xonsh.xontribs import auto_load_xontribs_from_entrypoints, xontribs_load
from xonsh.lazyimps import pygments, pyghooks
from xonsh.imphooks import install_import_hooks
from xonsh.events import events
from xonsh.environ import xonshrc_context, make_args_env
from xonsh.built_ins import XonshSession, XSH

from xonsh import main as xmain

from assistant.ptk_shell import shell
from assistant import __version__ as __assistant_version__
from assistant.rasa import enable_service_now as assistant_now
from assistant.rasa.nlp import AgentRasaInterface
from assistant.cli import interactive
from assistant.as_client import nlp_intent_hello_version, nlp_intent_exit, query
#from assistant.application import AssistantInteractiveApplication
#from assistant.history import XonshJsonHistory

from datetime import date


events.transmogrify("on_post_init", "LoadEvent")
events.doc(
    "on_post_init",
    """
on_post_init() -> None
Fired after all initialization is finished and we're ready to do work.
NOTE: This is fired before the wizard is automatically started.
""",
)

events.transmogrify("on_exit", "LoadEvent")
events.doc(
    "on_exit",
    """
on_exit() -> None
Fired after all commands have been executed, before tear-down occurs.
NOTE: All the caveats of the ``atexit`` module also apply to this event.
""",
)


events.transmogrify("on_pre_cmdloop", "LoadEvent")
events.doc(
    "on_pre_cmdloop",
    """
on_pre_cmdloop() -> None
Fired just before the command loop is started, if it is.
""",
)

events.transmogrify("on_post_cmdloop", "LoadEvent")
events.doc(
    "on_post_cmdloop",
    """
on_post_cmdloop() -> None
Fired just after the command loop finishes, if it is.
NOTE: All the caveats of the ``atexit`` module also apply to this event.
""",
)

events.transmogrify("on_pre_rc", "LoadEvent")
events.doc(
    "on_pre_rc",
    """
on_pre_rc() -> None
Fired just before rc files are loaded, if they are.
""",
)

events.transmogrify("on_post_rc", "LoadEvent")
events.doc(
    "on_post_rc",
    """
on_post_rc() -> None
Fired just after rc files are loaded, if they are.
""",
)


def get_setproctitle():
    """Proxy function for loading process title"""
    try:
        from setproctitle import setproctitle as spt
    except ImportError:
        return
    return spt


def path_argument(s):
    """Return a path only if the path is actually legal
    This is very similar to argparse.FileType, except that it doesn't return
    an open file handle, but rather simply validates the path."""

    s = os.path.abspath(os.path.expanduser(s))
    if not os.path.isfile(s):
        msg = "{0!r} must be a valid path to a file".format(s)
        raise argparse.ArgumentTypeError(msg)
    return s


@lazyobject
def parser():
    p = argparse.ArgumentParser(description="Assistant: a clever shell implementation", add_help=False)
    p.add_argument(
        "-h",
        "--help",
        dest="help",
        action="store_true",
        default=False,
        help="Show help and exit.",
    )
    p.add_argument(
        "-V",
        "--version",
        dest="version",
        action="store_true",
        default=False,
        help="Show version information and exit.",
    )
    p.add_argument(
        "-c",
        help="Run a single command and exit.",
        dest="command",
        required=False,
        default=None,
    )
    p.add_argument(
        "-i",
        "--interactive",
        help="Force running in interactive mode.",
        dest="force_interactive",
        action="store_true",
        default=False,
    )
    p.add_argument(
        "-l",
        "--login",
        help="Run as a login shell.",
        dest="login",
        action="store_true",
        default=False,
    )
    p.add_argument(
        "--rc",
        help="RC files to load.",
        dest="rc",
        nargs="+",
        type=path_argument,
        default=None,
    )
    p.add_argument(
        "--no-rc",
        help="Do not load any rc files.",
        dest="norc",
        action="store_true",
        default=False,
    )
    p.add_argument(
        "--no-script-cache",
        help="Do not cache scripts as they are run.",
        dest="scriptcache",
        action="store_false",
        default=True,
    )
    p.add_argument(
        "--cache-everything",
        help="Use a cache, even for interactive commands.",
        dest="cacheall",
        action="store_true",
        default=False,
    )
    p.add_argument(
        "-D",
        dest="defines",
        help="Define an environment variable, in the form of "
        "-DNAME=VAL. May be used many times.",
        metavar="ITEM",
        action="append",
        default=None,
    )
    p.add_argument(
        "--shell-type",
        help="What kind of shell should be used. "
        "Possible options: readline, prompt_toolkit, random. "
        "Warning! If set this overrides $SHELL_TYPE variable.",
        dest="shell_type",
        choices=tuple(Shell.shell_type_aliases.keys()),
        default=None,
    )
    p.add_argument(
        "--timings",
        help="Prints timing information before the prompt is shown. "
        "This is useful while tracking down performance issues "
        "and investigating startup times.",
        dest="timings",
        action="store_true",
        default=None,
    )
    p.add_argument(
        "file",
        metavar="script-file",
        help="If present, execute the script in script-file or (if not present) execute as a command" " and exit.",
        nargs="?",
        default=None,
    )
    p.add_argument(
        "args",
        metavar="args",
        help="Additional arguments to the script (or command) specified " "by script-file.",
        nargs=argparse.REMAINDER,
        default=[],
    )
    return p

def _pprint_displayhook(value):
    if value is None:
        return
    builtins._ = None  # Set '_' to None to avoid recursion
    #if isinstance(value, HiddenCommandPipeline):
    #    builtins._ = value
    #    return
    env = XSH.env
    printed_val = None
    if env.get("PRETTY_PRINT_RESULTS"):
        printed_val = pretty(value)
    if not isinstance(printed_val, str):
        # pretty may fail (i.e for unittest.mock.Mock)
        printed_val = repr(value)
    if HAS_PYGMENTS and env.get("COLOR_RESULTS"):
        tokens = list(pygments.lex(printed_val, lexer=pyghooks.XonshLexer()))
        end = "" if env.get("SHELL_TYPE") == "prompt_toolkit" else "\n"
        print_color(tokens, end=end)
    else:
        print(printed_val)  # black & white case
    builtins._ = value


class XonshMode(enum.Enum):
    single_command = 0
    script_from_file = 1
    script_from_stdin = 2
    interactive = 3

def _get_rc_files(shell_kwargs: dict, args, env):
    # determine which RC files to load, including whether any RC directories
    # should be scanned for such files
    rc_cli = shell_kwargs.get("rc")
    if shell_kwargs.get("norc") or (
        args.mode != XonshMode.interactive
        and not args.force_interactive
        and not args.login
    ):
        # if --no-rc was passed, or we're not in an interactive shell and
        # interactive mode was not forced, then disable loading RC files and dirs
        return (), ()

    if rc_cli:
        # if an explicit --rc was passed, then we should load only that RC
        # file, and nothing else (ignore both XONSHRC and XONSHRC_DIR)
        rc = tuple(r for r in rc_cli if os.path.isfile(r))
        rcd = tuple(r for r in rc_cli if os.path.isdir(r))
        return rc, rcd

    # otherwise, get the RC files from XONSHRC, and RC dirs from XONSHRC_DIR
    rc = env.get("XONSHRC")
    rcd = env.get("XONSHRC_DIR")
    return rc, rcd

def _load_rc_files(shell_kwargs: dict, args, env, execer, ctx):
    events.on_pre_rc.fire()
    # load rc files
    login = shell_kwargs.get("login", True)
    rc, rcd = _get_rc_files(shell_kwargs, args, env)
    XSH.rc_files = xonshrc_context(
        rcfiles=rc, rcdirs=rcd, execer=execer, ctx=ctx, env=env, login=login
    )
    events.on_post_rc.fire()

def _autoload_xontribs(env):
    events.on_timingprobe.fire(name="pre_xontribs_autoload")
    disabled = env.get("XONTRIBS_AUTOLOAD_DISABLED", False)
    if disabled is True:
        return
    blocked_xontribs = disabled or ()
    auto_load_xontribs_from_entrypoints(
        blocked_xontribs, verbose=bool(env.get("XONSH_DEBUG", False))
    )
    events.on_xontribs_loaded.fire()
    events.on_timingprobe.fire(name="post_xontribs_autoload")

def start_services(shell_kwargs, args, pre_env=None):
    """Starts up the essential services in the proper order.
    This returns the environment instance as a convenience.
    """
    if pre_env is None:
        pre_env = {}
    # create execer, which loads builtins
    ctx = shell_kwargs.get("ctx", {})
    debug = to_bool_or_int(os.getenv("XONSH_DEBUG", "0"))
    events.on_timingprobe.fire(name="pre_execer_init")
    execer = Execer(
        filename="<stdin>",
        debug_level=debug,
        scriptcache=shell_kwargs.get("scriptcache", True),
        cacheall=shell_kwargs.get("cacheall", False),
    )
    XSH.load(ctx=ctx, execer=execer)
    events.on_timingprobe.fire(name="post_execer_init")

    install_import_hooks(execer)

    env = XSH.env
    for k, v in pre_env.items():
        env[k] = v

    #_autoload_xontribs(env)
    #_load_rc_files(shell_kwargs, args, env, execer, ctx)
    # create shell
    XSH.shell = Shell(execer=execer, **shell_kwargs)
    ctx["__name__"] = "__main__"
    return env

def premain(argv=None):
    """Setup for main xonsh entry point. Returns parsed arguments."""
    if argv is None:
        argv = sys.argv[1:]
    XSH = XonshSession()
    setup_timings(argv)
    setproctitle = get_setproctitle()
    if setproctitle is not None:
        setproctitle(" ".join(["xonsh"] + argv))
    args = parser.parse_args(argv)
    if args.help:
        parser.print_help()
        parser.exit()
    
    assistant_now()
    if args.version:
        from prompt_toolkit import print_formatted_text
        from assistant.rasa import nlp
        from assistant.strformat_utils import get_ftext_banner
        
        xonsh_version = "/".join(("xonsh", __version__))
        version = "#".join(("assistant", __assistant_version__))
        rasa_version = nlp_intent_hello_version()
        print_formatted_text(get_ftext_banner())
        if rasa_version:
            print(rasa_version)
        print(xonsh_version)
        print(version)
        print()
        print(f"Copyright © {str(date.today().year)}, Danny Waser")
        parser.exit()
    shell_kwargs = {
        "shell_type": args.shell_type,
        "completer": False,
        "login": False,
        "scriptcache": args.scriptcache,
        "cacheall": args.cacheall,
        "ctx": XSH.ctx,
    }
    if args.login or sys.argv[0].startswith("-"):
        args.login = True
        shell_kwargs["login"] = True
    if args.norc:
        shell_kwargs["rc"] = ()
    elif args.rc:
        shell_kwargs["rc"] = args.rc
    setattr(sys, "displayhook", _pprint_displayhook)
    if args.command is not None:
        args.mode = XonshMode.single_command
        shell_kwargs["shell_type"] = "none"
    elif args.file is not None:
        args.mode = XonshMode.script_from_file
        shell_kwargs["shell_type"] = "none"
    elif not sys.stdin.isatty() and not args.force_interactive:
        args.mode = XonshMode.script_from_stdin
        shell_kwargs["shell_type"] = "none"
    else:
        args.mode = XonshMode.interactive
        shell_kwargs["completer"] = True
        shell_kwargs["login"] = True

    env = start_services(shell_kwargs, args)
    env["XONSH_LOGIN"] = shell_kwargs["login"]
    if args.defines is not None:
        env.update([x.split("=", 1) for x in args.defines])
    env["XONSH_INTERACTIVE"] = args.force_interactive or (
        args.mode == XonshMode.interactive
    )
    return args

async def main(argv=None):
    #xmain.setup()
    #print(builtins.__xonsh__.shell)
    args = premain(argv)
    XSH.shell.shell = shell.AssistantShell()
    sys.exit(await main_assistant(args))
    #realshell = builtins.__xonsh__.shell
    #import aish.shell
    #return main_aish(args)
    ##except Exception as err:
    ##    _failback_to_other_shells(args, err)


async def main_assistant(args):
    """Main entry point for assistant; replaces xonsh.main.main_xonsh"""
    if not ON_WINDOWS:
        def func_sig_ttin_ttou(n, f):
            pass
        signal.signal(signal.SIGTTIN, func_sig_ttin_ttou)
        signal.signal(signal.SIGTTOU, func_sig_ttin_ttou)

    events.on_post_init.fire()

    env = XSH.env
    shell = XSH.shell
    
    env['XONSH_CAPTURE_ALWAYS'] = True
    env['XONSH_STORE_STDOUT'] = True
    #env['XONSH_HISTORY_BACKEND'] = XonshJsonHistory

    #env['USERNAME'] = env.get('USERNAME', os.environ.get('USERNAME', 'Unknown'))
    #env['LOGNAME'] = env.get('LOGNAME', os.environ.get('LOGNAME', 'anymus'))
    #env['HOME'] = "/home/%s" % env.get('USERNAME')
    #env['PWD'] = os.environ.get('PWD', env.get('HOME'))
    env['ASSISTANT_PATH'] = env.get('HOME') + "/.assistant"
    env['SETTINGS_PATH'] = env.get('ASSISTANT_PATH')[0] + "/settings.tml"
    env['I18N'], env['L10N'] = (x for x in env.get('LANG', os.environ.get('LANG', "en_EN.UTF-8")).split(".")[0].split("_"))
    env['ASSISTANT_NLP_HOST'] = env.get('ASSISTANT_NLP_HOST', os.environ.get('ASSISTANT_NLP_HOST', 'localhost'))
    env['ASSISTANT_NLP_PORT'] = env.get('ASSISTANT_NLP_PORT', os.environ.get('ASSISTANT_NLP_PORT', '5005'))
    env['ASSISTANT_ACTION_HOST'] = env.get('ASSISTANT_ACTION_HOST', os.environ.get('ASSISTANT_ACTION_HOST', 'localhost'))
    env['ASSISTANT_ACTION_PORT'] = env.get('ASSISTANT_ACTION_PORT', os.environ.get('ASSISTANT_ACTION_PORT', '5055'))
    #env['XONSH_DATA_DIR'] = os.environ.get('XONSH_DATA_DIR', f'{HOME}/.local/share/xonsh')
    
    history = XSH.history

    exit_code = 0

    #if shell and not env["XONSH_INTERACTIVE"]:
        #shell.ctx.update({"exit": sys.exit})

    # store a sys.exc_info() tuple to record any exception that might occur in the user code that we are about to execute
    # if this does not change, no exceptions were thrown. Otherwise, print a traceback that does not expose xonsh internals
    #exc_info = (None, None, None)
    
    try:
        if args.mode == XonshMode.interactive:
            # enter the shell

            try:
                wxh = os.get_terminal_size()
                env['is_terminal_simated'] = False
                env["XONSH_INTERACTIVE"] = True # Setted again here because it is possible to call main_assistant() without calling premain(), namely in the tests.
                env['WIDTH'] = int(wxh.columns)
                env['HEIGTH'] = int(wxh.lines)
            except OSError as ose:
                print("You asked for an interactive session, yet your terminal has no size according to your OS:")
                raise ose
                exit(ose.exit_code)
            
            ignore_sigtstp()
            # if (
            #       env['XONSH_INTERACTIVE'] 
            #       and not any(os.path.isfile(i) for i in env['XONSHRC'])
            #       and not any(os.path.isdir(i) for i in env["XONSHRC_DIR"])
            #    ):
            #    pass
            #    print_welcome_screen()
            events.on_pre_cmdloop.fire()
            try:
                # if shell.shell.kernel_interface.is_nlp_server_up():
                #     await shell.shell.cmdloop(intro=shell.shell.kernel_interface.nlp_intent_hello())
                # else:
                #     await shell.shell.cmdloop()
                await interactive()
            except (KeyboardInterrupt, Exception):
                XSH.exit = True
            finally:
                events.on_post_cmdloop.fire()
        elif args.mode == XonshMode.single_command:
            # run a single command and exit
            command = args.command.lstrip()
            nlp = await query(command, XSH.env.get("USERNAME", os.environ.get('USERNAME', 'user'))) #shell.shell.kernel_interface.interpret_nlp(command)
            if nlp:
                print(nlp)
                exit_code = 0
            else:
                run_code_with_cache(command, shell.execer, glb=shell.ctx, mode='single')
                if history is not None and history.last_cmd_rtn is not None:
                    exit_code = history.last_cmd_rtn
        elif args.mode == XonshMode.script_from_file:
            # run a script contained in a file
            # TODO: Enable NLP inside script files
            path = os.path.abspath(os.path.expanduser(args.file))
            if os.path.isfile(path):
                sys.argv = [args.file] + args.args
                env['ARGS'] = sys.argv[:]  # $ARGS is not sys.argv
                env['XONSH_SOURCE'] = path
                shell.ctx.update({'__file__': args.file, '__name__': '__main__'})
                run_script_with_cache(args.file, shell.execer, glb=shell.ctx,
                                      loc=None, mode='exec')
            else:
            # interpret as command instead
            #   print('xonsh: {0}: No such file or directory.'.format(args.file))
                command = f"{str(args.file)} {str(' '.join(args.args))}".lstrip()
                nlp = await query(command, XSH.env.get("USERNAME", os.environ.get('USERNAME', 'user')))#shell.shell.kernel_interface.interpret_nlp(command)
                if nlp:
                    print(nlp)
                    exit_code = 0
                else:
                    run_code_with_cache(command, shell.execer, glb=shell.ctx, mode='single')
                    if history is not None and history.last_cmd_rtn is not None:
                        exit_code = history.last_cmd_rtn
        elif args.mode == XonshMode.script_from_stdin:
            # run a script given on stdin
            code = sys.stdin.read()
            # We should not use the shell loop here; creates
            ## Warning: Input is not to a terminal (fd=0).
            # It's missing tty for prompt_toolkit.
            # TODO: add custom nlp_interpreter for stdin (no TTY, no prompt_toolkit)
            nlp = AgentRasaInterface().interpret_nlp_using_server(str(code))
            if nlp:
                print(nlp)
                exit_code = 0
            else:
                run_code_with_cache(code, shell.execer, glb=shell.ctx, loc=None,
                                    mode='exec')
    finally:
        events.on_exit.fire()
    
    xmain.postmain(args)
    
    return exit_code


def setup(
    ctx=None,
    shell_type="none",
    env=(("RAISE_SUBPROC_ERROR", True),),
    aliases=(),
    xontribs=(),
    threadable_predictors=(),
):
    """Starts up a new xonsh shell. Calling this in function in another
    packages ``__init__.py`` will allow xonsh to be fully used in the
    package in headless or headed mode. This function is primarily indended to
    make starting up xonsh for 3rd party packages easier.
    Here is example of using this at the top of an ``__init__.py``::
        from xonsh.main import setup
        setup()
        del setup
    Parameters
    ----------
    ctx : dict-like or None, optional
        The xonsh context to start with. If None, an empty dictionary
        is provided.
    shell_type : str, optional
        The type of shell to start. By default this is 'none', indicating
        we should start in headless mode.
    env : dict-like, optional
        Environment to update the current environment with after the shell
        has been initialized.
    aliases : dict-like, optional
        Aliases to add after the shell has been initialized.
    xontribs : iterable of str, optional
        Xontrib names to load.
    threadable_predictors : dict-like, optional
        Threadable predictors to start up with. These overide the defaults.
    """
    ctx = {} if ctx is None else ctx
    # setup xonsh ctx and execer
    if not hasattr(builtins, "__xonsh__"):
        execer = Execer(filename="<stdin>")
        __xonsh__.load(ctx=ctx, execer=execer)
        __xonsh__.shell = shell.AssistantShell(execer, ctx=ctx, shell_type=shell_type)
    __xonsh__.env.update(env)
    install_import_hooks(__xonsh__.execer)
    __xonsh__.aliases.update(aliases)
    if xontribs:
        xontribs_load(xontribs)
    tp = XSH.commands_cache.threadable_predictors
    tp.update(threadable_predictors)
