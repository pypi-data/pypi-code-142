# -*- coding: utf-8 -*-

from typing import Callable, List, Optional

from t3.arguments import get_default_arguments
from t3.context.context import run_context
from t3.logging.logging import (
    SEVERITY_NAME_DEBUG,
    logger,
    set_default_logging_config,
    set_root_level,
    set_simple_logging_config,
)


def main(
    cmdline: Optional[List[str]] = None,
    printer: Callable[..., None] = print,
) -> int:
    args = get_default_arguments(cmdline)

    if args.default_logging and args.simple_logging:
        printer(
            "The 'default_logging' flag and the 'simple_logging' flag cannot coexist"
        )
        return 1

    default_logging = args.default_logging
    simple_logging = args.simple_logging
    severity = args.severity
    fullscreen = args.fullscreen
    fps = args.fps
    vsync = args.vsync
    debug = args.debug
    verbose = args.verbose

    assert isinstance(default_logging, bool)
    assert isinstance(simple_logging, bool)
    assert isinstance(severity, str)
    assert isinstance(fullscreen, bool)
    assert isinstance(fps, int)
    assert isinstance(vsync, bool)
    assert isinstance(debug, bool)
    assert isinstance(verbose, int)

    if default_logging:
        set_default_logging_config()
    elif simple_logging:
        set_simple_logging_config()

    if debug:
        set_root_level(SEVERITY_NAME_DEBUG)
    else:
        set_root_level(severity)

    logger.debug(f"Arguments: {args}")

    try:
        run_context(
            fullscreen=fullscreen,
            resizable=False,
            fps=fps,
            antialiasing=True,
            vsync=vsync,
            center_window=False,
            debug=debug,
            verbose=verbose,
        )
    except BaseException as e:
        logger.exception(e)
        return 1
    else:
        return 0


if __name__ == "__main__":
    exit(main())
