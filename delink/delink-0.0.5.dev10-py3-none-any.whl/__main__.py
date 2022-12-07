import argparse

from _version import __version__, PROGRAM_NAME
from delink.ios_watchdog import connect_ios_device, disconnect_ios_device, stop


def cmd_version(args: argparse.Namespace):
    """
    打印版本号
    """
    print(PROGRAM_NAME, "version", __version__)


def cmd_conn_remote_ios_device(args: argparse.Namespace):
    address = args.address
    port = args.port
    udid = args.udid
    connect_ios_device(udid, address, port)


def cmd_disconnect_remote_ios_device(args: argparse.Namespace):
    udid = args.udid
    if not udid:
        print("udid异常")
        return
    disconnect_ios_device(udid)
    print("目前已经断开设备{}的链接了".format(udid))


def cmd_stop(args: argparse.Namespace):
    stop()
    print("停止指令已经发出")


_commands = [
    dict(action=cmd_version, command="version", help="查看版本号"),
    dict(action=cmd_stop, command="stop", help="停止服务"),
    dict(action=cmd_disconnect_remote_ios_device, command="disconnect", help="断开链接"),
    dict(action=cmd_conn_remote_ios_device,
         command="conn",
         flags=[dict(args=['-A', '--address'],
                     help='远程代理地址',
                     required=True,
                     ),
                dict(args=['-P', '--port'],
                     help='远程代理端口',
                     type=int,
                     required=True)],
         help="链接设备")
]


def main():
    # yapf: disable
    parser = argparse.ArgumentParser(
        description="ios远程调试客户端,version {}".format(
            __version__),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="store_true", help="工具版本号"),
    parser.add_argument("-u", "--udid", help="需要控制的设备uuid")

    subparser = parser.add_subparsers(dest='subparser')
    actions = {}
    for c in _commands:
        cmd_name = c['command']
        actions[cmd_name] = c['action']
        sp = subparser.add_parser(cmd_name, help=c.get('help'),
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        for f in c.get('flags', []):
            args = f.get('args')
            if not args:
                args = ['-' * min(2, len(n)) + n for n in f['name']]
            kwargs = f.copy()
            kwargs.pop('name', None)
            kwargs.pop('args', None)
            sp.add_argument(*args, **kwargs)

    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    if not args.subparser:
        parser.print_help()
        # show_upgrade_message()
        return

    # 具体运行
    actions[args.subparser](args)


if __name__ == "__main__":
    main()
