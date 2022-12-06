from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO, WARNING, basicConfig, getLogger
from typing import Any, Callable, Generator, List, TypedDict, Union
from typing_extensions import Unpack
from wasmtime import Store, Module, Instance, Func, FuncType, ValType

from wasm_cli_runner.version import get_version


NAME = "WASM CLI Runner"

DEFAULT_LOG_LEVEL = WARNING
WASM_BINARY_MAGIC = (0x00, 0x61, 0x73, 0x6d)
WASM_BINARY_MAGIC_STR = "".join(("{:x}".format(b) for b in WASM_BINARY_MAGIC))


logger = getLogger(NAME)


class ParserArgs(TypedDict, total=False):
    wasm_file: str


def log(value: Any) -> None:
    logger.log(INFO, f"WASM Log: {value}")


def convert_str_to_bytes_by_literals(text: str) -> bytes:
    """Convert a string to its bytes by the literal chars included in the string.

    Example:
    ```
    >>> convert_str_to_bytes_by_literals("abcd")
    b'\xab\xcd'
    >>> convert_str_to_bytes_by_literals("abcd") == bytes([0xab, 0xcd])
    True
    >>> "abcd".encode("ascii")
    b'abcd'
    >>> "abcd".encode("ascii") == bytes([0x61, 0x62, 0x63, 0x64])
    True
    """
    return bytes((int(text[i:i+2], 16)) for i in range(0, len(text), 2))


def get_wasm_code_from_str(code: str) -> Union[bytes, str]:
    trimmed_code = code.strip(" \t\n\"'")

    if trimmed_code.startswith(WASM_BINARY_MAGIC_STR):
        return convert_str_to_bytes_by_literals(trimmed_code)
    else:
        return trimmed_code


def get_wasm_file_content(file_path: str) -> Union[str, bytes]:
    with open(file_path, "rb") as f:
        content = f.read()
        if content[:4] == WASM_BINARY_MAGIC:
            logger.debug("Assuming WebAssembly Binary due to first 4 bytes.")
            return content
        else:
            logger.debug("Assuming WebAssembly Text due missing WASM_BINARY_MAGIC.")
            return content.decode("utf-8")


def get_wasm_function_signatures(funcs: List[Func]) -> Generator[str, None, None]:
    for func in funcs:
        yield f"{func._func.__name__}()"


def add_wasm_function(
    store: Store, params: List[ValType], results: List[ValType], func: Callable
) -> Func:
    str_params = (f"(param {str(p)})" for p in params)
    str_results = (f"(result {str(p)})" for p in params)
    logger.debug(
        f"Adding ({func.__name__} {' '.join(str_params)} {' '.join(str_results)})"
    )
    return Func(store, FuncType(params, results), func)


def get_wasm_functions(store: Store) -> List[Func]:
    return [
        add_wasm_function(store, [ValType.i32()], [], print),
        # add_wasm_function(store, [ValType.i32()], [], log)
    ]


def run(args: Namespace) -> None:
    store = Store()
    if args.inline:
        wasm_code = get_wasm_code_from_str(args.wasm_file)
    else:
        wasm_code = get_wasm_file_content(args.wasm_file)

    logger.debug("Creating WASM module from code.")
    module = Module(store.engine, wasm_code)

    logger.debug("Creating WASM instance")
    instance = Instance(store, module, get_wasm_functions(store))

    start_functions = ["run", "main", "start"]
    for start_function_name in start_functions:
        try:
            func = instance.exports(store)[start_function_name]

            if isinstance(func, Func):
                logger.debug(f"Running WASM function {start_function_name}.")
                func(store)
                break
        except (KeyError, IndexError):
            pass


def get_arg_parser() -> ArgumentParser:
    parser = ArgumentParser(prog=NAME)

    parser.add_argument(
        "--version", "-V", action="version", version=f"{NAME}, version {get_version()}"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="log_level",
        help="Set the loglevel to INFO",
        action="store_const",
        const=INFO,
        default=DEFAULT_LOG_LEVEL
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="log_level",
        help="Set the loglevel to DEBUG",
        action="store_const",
        const=DEBUG,
    )
    parser.add_argument(
        "--inline",
        "-i",
        dest="inline",
        help=(
            "Use this flag to interpret the WASM_FILE as the content of a file"
            " (interpret the argument directly)"
        ),
        action="store_true",
        default=False
    )
    parser.add_argument(
        "wasm_file",
        help="The WebAssembly binary or text file path",
        type=str
    )

    return parser


def init_logging(args: Namespace) -> None:
    if args.log_level < INFO:
        log_format = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    else:
        log_format = "%(levelname)s: %(message)s"

    basicConfig(
        level=args.log_level, format=log_format, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(**kwargs: Unpack[ParserArgs]) -> None:
    parser = get_arg_parser()
    if len(kwargs) > 0:
        args = Namespace(**kwargs)
    else:
        args = parser.parse_args()

    init_logging(args)

    run(args)


if __name__ == '__main__':
    main()
