# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pywirelessmbus',
 'pywirelessmbus.devices',
 'pywirelessmbus.exceptions',
 'pywirelessmbus.sticks',
 'pywirelessmbus.utils']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pyserial-asyncio>=0.6,<0.7', 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'pywirelessmbus',
    'version': '1.5.3',
    'description': 'A tool to receive and send Wireless-M-Bus messages.',
    'long_description': '# pyWirelessMbus\n\nThis module can decode messages from wireless M-Bus devices. The messages must received from a usb-uart stick. At this moment only the [iM871A-USB from IMST](https://shop.imst.de/wireless-modules/usb-radio-products/10/im871a-usb-wireless-m-bus-usb-adapter-868-mhz) is usable. Maybe somebody can add a alternative.\n\nOn the device side pyWirelessMbus reads the messages from the Temp/Hum Sensor [Munia from Weptech](https://www.weptech.de/en/wireless-m-bus/humidity-temperature-sensor-munia.html) and the [EnergyCam from Q-loud](https://www.q-loud.de/energycam).\n\n## Requirements\n\nPython >= 3.8\n\n## Installation\n\n```\npip install pywirelessmbus\n```\n\n## Development\n\nFor testing you can install all deps and start the module with that commands.\n\n```\npoetry install\npoetry shell\npython examples/monitor.py\n```\n\n## Plans\n\n- Add more devices\n- Add tests\n- Send messages\n',
    'author': 'Karl Wolffgang',
    'author_email': 'karl_eugen.wolffgang@tu-dresden.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gewv-tu-dresden/pyWirelessMbus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
