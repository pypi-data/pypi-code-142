# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ttp',
 'ttp.formatters',
 'ttp.group',
 'ttp.input',
 'ttp.lookup',
 'ttp.match',
 'ttp.output',
 'ttp.patterns',
 'ttp.returners',
 'ttp.utils',
 'ttp.variable']

package_data = \
{'': ['*']}

extras_require = \
{'docs:python_version >= "3.7"': ['readthedocs-sphinx-search==0.1.1',
                                  'Sphinx==4.3.0',
                                  'sphinx_rtd_theme==1.0.0',
                                  'sphinxcontrib-applehelp==1.0.1',
                                  'sphinxcontrib-devhelp==1.0.1',
                                  'sphinxcontrib-htmlhelp==2.0.0',
                                  'sphinxcontrib-jsmath==1.0.1',
                                  'sphinxcontrib-napoleon==0.7',
                                  'sphinxcontrib-qthelp==1.0.2',
                                  'sphinxcontrib-serializinghtml==1.1.5',
                                  'sphinxcontrib-spelling==7.2.1'],
 'full:python_version >= "3.7"': ['cerberus>=1.3.0,<1.4.0',
                                  'jinja2>=3.0.0,<3.1.0',
                                  'pyyaml==6.0',
                                  'deepdiff>=5.8.0,<5.9.0',
                                  'openpyxl>=3.0.0,<3.1.0',
                                  'tabulate>=0.8.0,<0.9.0',
                                  'ttp_templates<1.0.0',
                                  'yangson>=1.4.0,<1.5.0',
                                  'n2g>=0.2.0,<0.3.0']}

entry_points = \
{'console_scripts': ['ttp = ttp.ttp:cli_tool']}

setup_kwargs = {
    'name': 'ttp',
    'version': '0.9.2',
    'description': 'Template Text Parser',
    'long_description': '[![Downloads](https://pepy.tech/badge/ttp)](https://pepy.tech/project/ttp)\n[![PyPI versions](https://img.shields.io/pypi/pyversions/ttp.svg)](https://pypi.python.org/pypi/ttp/)\n[![Documentation status](https://readthedocs.org/projects/ttp/badge/?version=latest)](http://ttp.readthedocs.io/?badge=latest)\n\n# Template Text Parser\n\nTTP is a Python library for semi-structured text parsing using templates.\n\n## Why?\n\nTo save ones time on transforming raw text into structured data and beyond.\n\n## How?\n\nRegexes, regexes everywhere... but, dynamically formed out of TTP templates with added capabilities to simplify the  process of getting desired outcome.\n\n## What?\n\nIn essence TTP can help to:\n  - Prepare, sort and load text data for parsing\n  - Parse text using regexes dynamically derived out of templates\n  - Process matches on the fly using broad set of built-in or custom functions\n  - Combine match results in a structure with arbitrary hierarchy\n  - Transform results in desired format to ease consumption by humans or machines\n  - Return results to various destinations for storage or further processing\n\nReference [documentation](https://ttp.readthedocs.io) for more information.\n\nTTP [Networktocode Slack channel](https://networktocode.slack.com/archives/C018HMJQECB)\n\nCollection of [TTP Templates](https://github.com/dmulyalin/ttp_templates)\n\n## Example - as simple as it can be\n\nSimple interfaces configuration parsing example\n\n<details><summary>Code</summary>\n\n```python\nfrom ttp import ttp\nimport pprint\n\ndata = """\ninterface Loopback0\n description Router-id-loopback\n ip address 192.168.0.113/24\n!\ninterface Vlan778\n description CPE_Acces_Vlan\n ip address 2002::fd37/124\n ip vrf CPE1\n!\n"""\n\ntemplate = """\ninterface {{ interface }}\n ip address {{ ip }}/{{ mask }}\n description {{ description }}\n ip vrf {{ vrf }}\n"""\n\nparser = ttp(data, template)\nparser.parse()\npprint.pprint(parser.result(), width=100)\n\n# prints:\n# [[[{\'description\': \'Router-id-loopback\',\n#     \'interface\': \'Loopback0\',\n#     \'ip\': \'192.168.0.113\',\n#     \'mask\': \'24\'},\n#    {\'description\': \'CPE_Acces_Vlan\',\n#     \'interface\': \'Vlan778\',\n#     \'ip\': \'2002::fd37\',\n#     \'mask\': \'124\',\n#     \'vrf\': \'CPE1\'}]]]\n```\n</details>\n\n## Example - a bit more complicated\n\nFor this example lets say we want to parse BGP peerings output, but combine state with configuration data, at the end we want to get pretty looking text table printed to screen.\n\n<details><summary>Code</summary>\n\n```python\ntemplate="""\n<doc>\nThis template first parses "show bgp vrf CUST-1 vpnv4 unicast summary" commands\noutput, forming results for "bgp_state" dictionary, where peer ip is a key.\n\nFollowing that, "show run | section bgp" output parsed by group "bgp_cfg". That\ngroup uses nested groups to form results structure, including absolute path\n"/bgp_peers*" with path formatter to produce a list of peers under "bgp_peers"\npath.\n\nFor each peer "hostname" and local bgp "local_asn" added using previous matches.\nAdditionally, group lookup function used to lookup peer state from "bgp_state"\ngroup results, adding found data to peer results.\n\nFinally, "bgp_peers" section of results passed via "tabulate_outputter" to\nfrom and print this table to terminal:\n\nhostname           local_asn    vrf_name    peer_ip    peer_asn    uptime    state    description    afi    rpl_in           rpl_out\n-----------------  -----------  ----------  ---------  ----------  --------  -------  -------------  -----  ---------------  ---------------\nucs-core-switch-1  65100        CUST-1      192.0.2.1  65101       00:12:33  300      peer-1         ipv4   RPL-1-IMPORT-v4  RPL-1-EXPORT-V4\nucs-core-switch-1  65100        CUST-1      192.0.2.2  65102       03:55:01  idle     peer-2         ipv4   RPL-2-IMPORT-V6  RPL-2-EXPORT-V6\n\nRun this script with "python filename.py"\n</doc>\n\n<vars>\nhostname="gethostname"\nchain_1 = [\n    "set(\'vrf_name\')",\n    "lookup(\'peer_ip\', group=\'bgp_state\', update=True)"\n]\n</vars>\n\n<group name="bgp_state.{{ peer }}" input="bgp_state">\n{{ peer }}  4 65101      20      21       43    0    0 {{ uptime }} {{ state }}\n</group>\n\n<group name="bgp_cfg" input="bgp_config">\nrouter bgp {{ asn | record(asn) }}\n  <group name="vrfs.{{ vrf_name }}" record="vrf_name">\n  vrf {{ vrf_name }}\n    <group name="/bgp_peers*" chain="chain_1">\n    neighbor {{ peer_ip }}\n      {{ local_asn | set(asn) }}\n      {{ hostname | set(hostname) }}\n      remote-as {{ peer_asn }}\n      description {{ description }}\n      address-family {{ afi }} unicast\n        route-map {{ rpl_in }} in\n        route-map {{ rpl_out }} out\n\t</group>\n  </group>\n</group>\n\n<output\nname="tabulate_outputter"\nformat="tabulate"\npath="bgp_peers"\nreturner="terminal"\nheaders="hostname, local_asn, vrf_name, peer_ip, peer_asn, uptime, state, description, afi, rpl_in, rpl_out"\n/>\n"""\n\ndata_bgp_state = """\nucs-core-switch-1#show bgp vrf CUST-1 vpnv4 unicast summary\nNeighbor   V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd\n192.0.2.1  4 65101      32      54       42    0    0 00:12:33       300\n192.0.2.2  4 65101      11      45       99    0    0 03:55:01       idle\n"""\n\ndata_bgp_config = """\nucs-core-switch-1#show run | section bgp\nrouter bgp 65100\n  vrf CUST-1\n    neighbor 192.0.2.1\n      remote-as 65101\n      description peer-1\n      address-family ipv4 unicast\n        route-map RPL-1-IMPORT-v4 in\n        route-map RPL-1-EXPORT-V4 out\n    neighbor 192.0.2.2\n      remote-as 65102\n      description peer-2\n      address-family ipv4 unicast\n        route-map RPL-2-IMPORT-V6 in\n        route-map RPL-2-EXPORT-V6 out\n"""\n\nfrom ttp import ttp\n\nparser = ttp()\nparser.add_template(template)\nparser.add_input(data=data_bgp_state, input_name="bgp_state")\nparser.add_input(data=data_bgp_config, input_name="bgp_config")\nparser.parse()\n```\n</details>\n\n# Contributions\nFeel free to submit an issue, report a bug or ask a question, feature requests are welcomed. Or [buy](https://paypal.me/dmulyalin) Author a coffee\n\n# Additional resources\n\nList of additional resources:\n\n- Sandbox to test TTP templates - http://textfsm.nornir.tech/ by [tbotnz](https://github.com/tbotnz)\n- Videos on TTP - https://pynet.twb-tech.com/videos/ttp/ttp.html by [Kirk Byers](https://github.com/ktbyers)\n',
    'author': 'Denis Mulyalin',
    'author_email': 'd.mulyalin@gmail.com',
    'maintainer': 'Denis Mulyalin',
    'maintainer_email': 'd.mulyalin@gmail.com',
    'url': 'https://github.com/dmulyalin/ttp',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7,<4.0',
}


setup(**setup_kwargs)
