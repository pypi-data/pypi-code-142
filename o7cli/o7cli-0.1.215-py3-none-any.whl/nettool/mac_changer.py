"""MAC Changer for Windows, Linux and MacOS"""
import subprocess
import argparse


def get_arguments():
    """Method to get arguments from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Interface to change its MAC address', required=True)
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC address', required=True)
    return parser.parse_args()


def change_mac(interface : str, new_mac : str):
    """Method to change MAC address"""
    # Notes
    # 1. The command 'ifconfig' is used to display the current MAC address of the interface
    # In docker, container needs to run with --privileged flag
    print(f'[+] Changing MAC address for {interface} to {new_mac}')
    ret = subprocess.call(["ifconfig", interface, "down"])
    ret = subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    ret = subprocess.call(["ifconfig", interface, "up"])



if __name__ == '__main__':

    args  = get_arguments()
    change_mac(args.interface, args.new_mac)
