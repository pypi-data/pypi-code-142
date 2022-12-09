# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toml_env_conf']

package_data = \
{'': ['*']}

install_requires = \
['mergedeep>=1.3.4,<2.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'toml-env-conf',
    'version': '0.1.2',
    'description': 'Environment specific application configuration with TOML',
    'long_description': '# `toml_env_conf`\nTOML based application configuration with support for environment-specific overrides.\n\nUseful if you want different values in some environments (local/test/prod). e.g. all environments use \nthe values base_conf.toml, but you only want some values to be different when\n`env == "prod"`\n\nAs easy as \n```python\nimport toml_env_conf\n\ntoml_env_conf.load_as_dict(path)\n# or\ntoml_env_conf.load_as_dataclass(\n    path=path,\n    data_class=MyConfigType,\n    env="prod"\n)\n```\n\nWhere the path has the following toml files\n```\n├── base_conf.toml\n└── env_prod.toml\n```\n\n## Convention\n- There ***must*** be a file named `base_conf.toml`\n- For environment overrides, the file must be called `env_[name].toml`\ne.g. for an environment called `prod`, the file is called `env_prod.toml`.\nFor an environment called `dev`, the file is called `env_dev.toml`.\n\n\n## Example\n\n### Step 1: Create some configs\n\n`base_conf.toml`\n```toml\nname = "Regular name"\nhobby_name = "laundry"\nis_fun = false\nscores = [-10, -20]\n```\n\n`env_prod.toml`\n```toml\nhobby_name = "music"\nis_fun = true\n```\n\n### Step 2: Load em up\n\n`main.py`\n```python\nfrom dataclasses import dataclass\nfrom pathlib import Path\nfrom typing import List\n\nimport toml_env_conf\n\n\n@dataclass(frozen=True)  # freeze for immutability\nclass MyConfigType:\n    name: str\n    hobby_name: str\n    is_fun: bool\n    scores: List[int]\n   \nif __name__ == "__main__":\n    conf_dir_path = Path(__file__).parent.joinpath("/path/to/config")\n    \n    config: MyConfigType = toml_env_conf.load_as_dataclass(\n        conf_dir_path, MyConfigType, env="prod"\n    )\n    \n    print(config)\n```',
    'author': 'sa-',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sa-/toml_env_conf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
