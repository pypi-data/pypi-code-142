# Copyright 2015-2021 Laszlo Attila Toth
# Distributed under the terms of the GNU Lesser General Public License v3

import os
import sys

from dewi_core.application import Application


def main():
    app = Application('dewi')
    app.load_plugins(os.getenv('DEWI_PLUGINS', 'dewi.DewiPlugin').split(','))
    app.run(sys.argv[1:])


if __name__ == '__main__':
    main()
