from tensorfn.util.config import (
    read_config,
    preset_argparser,
    load_config,
    load_arg_config,
    add_distributed_args,
)
from tensorfn.util.ensure import ensure_tuple
from tensorfn.util.lazy_extension import LazyExtension
from tensorfn.util.logger import get_logger, create_small_table


def load_wandb():
    try:
        import wandb

    except ImportError:
        wandb = None

    return wandb


def base36encode(number, alphabet="0123456789abcdefghijklmnopqrstuvwxyz"):
    base36 = ""
    sign = ""

    if number < 0:
        sign = "-"
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


def base36decode(number):
    return int(number, 36)
