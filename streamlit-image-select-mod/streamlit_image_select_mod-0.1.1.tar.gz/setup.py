# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['streamlit_image_select_mod']

package_data = \
{'': ['*'],
 'streamlit_image_select_mod': ['frontend/*',
                                'frontend/build/*',
                                'frontend/build/static/js/*',
                                'frontend/public/*',
                                'frontend/src/*',
                                '~/*']}

install_requires = \
['streamlit>=1.12.0,<2.0.0']

setup_kwargs = {
    'name': 'streamlit-image-select-mod',
    'version': '0.1.1',
    'description': '🖼️ An image select component for Streamlit',
    'long_description': "# streamlit-image-select-mod 🖼️\n\n**A modded image select component for Streamlit.**\n\nThis custom component works just like `st.selectbox` but with images. It's a great option\nif you want to let the user select an example image, e.g. for a computer vision app!\n",
    'author': 'Johannes Rieke',
    'author_email': 'johannes.rieke@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
