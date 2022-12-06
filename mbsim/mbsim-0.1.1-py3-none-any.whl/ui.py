try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points

from mbsim.mbsim import EntryPoints

_eps = entry_points()
if isinstance(_eps, dict):
    _eps = EntryPoints(_eps)


def getargs(parser):
    """
    Function that set argparser for mbsim.

    :param par: Subparser from mbsim to allow addon to add it's commands
    :return: function to call to allow mbsim to use addon
    :rtype: function
    """
    if not _eps.select(group="mbsim_ui"):
        return None

    args = parser(
        "ui",
        description="Activate UI",
    )
    args.add_argument(
        "UI",
        help="Select user interface",
        choices=[ui.name for ui in _eps.select(group="mbsim_ui")],
    )

    return run


def run(args):
    """
    Runs the function to start the user interface
    """
    _eps.select(name=args.UI).load()()
