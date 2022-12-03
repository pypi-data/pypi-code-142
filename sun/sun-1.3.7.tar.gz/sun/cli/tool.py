#!/usr/bin/python3
# -*- coding: utf-8 -*-

# sun is a part of sun.

# Copyright 2015-2022 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://gitlab.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import getpass
import subprocess
from sun.utils import fetch, os_info
from sun.__metadata__ import __version__, bin_path, daemon_tool


def su():
    '''Display message when sun execute as root'''
    if getpass.getuser() == 'root':
        raise SystemExit('sun: Error: It should not be run as root')


def usage():
    '''SUN arguments'''
    args = [
        f'SUN (Slackware Update Notifier) - Version: {__version__}\n',
        'Usage: sun [OPTIONS]\n',
        'Optional arguments:',
        '  help       Display this help and exit.',
        '  start      Start sun daemon.',
        '  stop       Stop sun daemon.',
        '  restart    Restart sun daemon.',
        '  check      Check for software updates.',
        '  status     Sun daemon status.',
        '  info       Os and machine information.\n',
        'Start GTK icon from the terminal: sun start --gtk'
    ]
    for opt in args:
        print(opt)


def check_updates():
    '''Check and display upgraded packages'''
    status = daemon_status()
    if 'not running' in status:
        print(status)
        raise SystemExit(1)
    packages = fetch()
    count = len(packages)
    message = 'No news is good news!'
    if count > 0:
        message = f'{count} software updates are available\n'
    return message, packages


def daemon_status():
    '''Display sun daemon status'''
    out = subprocess.getoutput('ps -af')
    message = 'SUN not running'
    if 'sun_daemon' in out:
        message = 'SUN is running...'
    return message


def _init_check_updates():
    '''Sub function for init'''
    message, packages = check_updates()
    count = len(packages)
    if count > 0:
        print(message)
        for pkg in packages:
            print(pkg)
    else:
        print(message)


def init():
    '''Initialization, all begins from here'''
    su()
    args = sys.argv
    args.pop(0)

    start = (f'{bin_path}{daemon_tool} -frB --pidfiles=~/.run '
             f'--name=sun_daemon {bin_path}python3 {bin_path}sun_daemon')
    stop = (f'{bin_path}{daemon_tool} --pidfiles=~/.run --name=sun_daemon '
            '--stop')
    restart = (f'{bin_path}{daemon_tool} --pidfiles=~/.run --name=sun_daemon '
               '--restart')

    if len(args) == 1:
        if args[0] == 'start':
            if 'not running' in daemon_status():
                print(f'Starting SUN daemon:  {daemon_tool} &')
                subprocess.call(f'{start} &', shell=True)
            else:
                print('Daemon is already running...')

        elif args[0] == 'stop':
            print(f'Stopping SUN daemon:  {daemon_tool}')
            subprocess.call(stop, shell=True)

        elif args[0] == 'restart':
            print(f'Stopping SUN daemon:  {daemon_tool}')
            subprocess.call(restart, shell=True)
            print(f'Starting SUN daemon:  {daemon_tool} &')

        elif args[0] == 'check':
            _init_check_updates()

        elif args[0] == 'status':
            print(daemon_status())

        elif args[0] == 'help':
            usage()

        elif args[0] == 'info':
            print(os_info())
        else:
            print("try: 'sun help'")

    elif len(args) == 2 and args[0] == 'start' and args[1] == '--gtk':
        subprocess.call('sun_gtk &', shell=True)
    else:
        raise SystemExit("try: 'sun help'")
