import os
import socket
import sys
import time

import click
from rich import print

from mifa import (
    AVDConfig,
    Configure,
    EmulatorManager,
    MitmproxyManager,
    SDKManager,
    __home__,
    is_win,
    run_cmd,
)

cfg = Configure()
adb_path = os.path.join(
    cfg.android_sdk_path,
    "platform-tools",
    "adb.exe" if is_win else "adb",
)


@click.command()
@click.option("-a", "--android-sdk-path", help="The path of the Android SDK.")
@click.option("-m", "--mitmproxy-path", help="The path of the mitmproxy.")
@click.option(
    "-p",
    "--package",
    help="Package path of the system image for this AVD (e.g. 'system-images;android-19;google_apis;x86').",
)
@click.option("-n", "--name", help="Name of the new AVD.")
def init(android_sdk_path, mitmproxy_path, package, name):
    """init datas"""

    if android_sdk_path:
        cfg.android_sdk_path = android_sdk_path
        cfg.save()
    if mitmproxy_path:
        cfg.mitmproxy_path = mitmproxy_path
        cfg.save()
    if package:
        cfg.package = package
        cfg.save()
    if name:
        cfg.name = name
        cfg.save()

    cfg.show()


@click.command("cfg")
def configure():
    """配置环境"""
    name = cfg.avd_name
    avd_package = cfg.avd_package

    sdkm = SDKManager()
    installed_packages = sdkm.list_installed()
    if avd_package not in installed_packages:
        print(":x: {} is not installed yet.".format(avd_package))
        sdkm.install(avd_package)

    else:
        print(":white_check_mark: {} has been installed.".format(avd_package))

    em = EmulatorManager()
    if em.has_avd(name):
        print(":white_check_mark: \[{}] already exists.".format(name))
    else:
        print(
            ":white_check_mark: Creating a new Android Virtual Device \[{}] ...".format(
                name
            )
        )
        em.create_avd(avd_package, name)
        if em.has_avd(name):
            print(":white_check_mark: \[{}] is created successfully.".format(name))

    avd_cfg = AVDConfig(name)
    avd_cfg.update_config()
    print(":white_check_mark: Configure AVD \[{}].".format(name))

    em.start_avd(name)
    print(":white_check_mark: \[{}] is ready.".format(name))

    mcm = MitmproxyManager()
    path = mcm.gen_android_cert()

    em.install_cert(path)
    while True:
        if em.check_cert(os.path.basename(path)):
            break
        print(":x: Certificate installation failed and is about to try again.")
        em.install_cert(path)
    print(
        ":white_check_mark: Certificate installation is successful.".format(
            os.path.basename(path)
        )
    )
    em.close()

    cfg.mitmproxy_cacert_name = os.path.basename(path)
    cfg.save()


@click.command()
def run():
    """start capture"""
    if cfg.mitmproxy_cacert_name:
        print(
            ":white_check_mark: mitmproxy cacert is {}.".format(
                cfg.mitmproxy_cacert_name
            )
        )
    else:
        print(
            ":x: mitmproxy cacert is not being installed yet, please run `mifa cfg`.".format(
                cfg.mitmproxy_cacert_name
            )
        )
        return

    mm = MitmproxyManager()
    mm.run_mitmweb()

    time.sleep(3)

    name = cfg.avd_name
    em = EmulatorManager()

    IP = socket.gethostbyname(socket.gethostname())
    em.start_avd(name, "http://{}:8080".format(IP))

    if em.check_cert(cfg.mitmproxy_cacert_name):
        print(
            ":white_check_mark: The CA cert {} is already installed.".format(
                cfg.mitmproxy_cacert_name
            )
        )
    else:
        print(
            ":x: The CA cert {} does not exist, please run `mifa cfg`".format(
                cfg.mitmproxy_cacert_name
            )
        )
        em.close()
        mm.kill_mitmweb()
        exit()

    while True:
        command = input("按q退出:")
        if command == "q":
            em.close()
            mm.kill_mitmweb()
            break


@click.group()
# @click.pass_context
def main():
    """mitmproxy for android"""
    return 0


main.add_command(init)
main.add_command(configure)
main.add_command(run)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
