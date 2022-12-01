# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fsm_admin_lite']

package_data = \
{'': ['*'], 'fsm_admin_lite': ['templates/admin/*']}

install_requires = \
['django-fsm>=2.8.1,<3.0.0', 'django>=3.2,<5.0']

setup_kwargs = {
    'name': 'django-fsm-admin-lite',
    'version': '0.1.0',
    'description': 'Integrate django-fsm state transitions into Django Admin.',
    'long_description': '# django-fsm-admin-lite\n\n![Generic badge](https://github.com/etchegom/django-fsm-admin-lite/actions/workflows/tests.yml/badge.svg)\n\n\nIntegrate [django-fsm](https://github.com/viewflow/django-fsm) state transitions into Django Admin.\n\nAlternative of [django-fsm-admin](https://github.com/gadventures/django-fsm-admin), with a lighter version of the frontend part.\n\nFeatures:\n- display available transitions in model admin so that user can apply them\n- mark FSM protected fields as read only\n\nLimitations:\n- transition methods parameters are not handled\n\n---\n\n## Installation\n\n```\npip install django-fsm-admin-lite\n```\nOr, for the latest git version\n```\npython -m pip install \'django-fsm-admin-lite @ git+https://github.com/etchegom/django-fsm-admin-lite.git\'\n```\n\n---\n\n## Usage\n\nMake you model admin class inherit from the mixin class `FSMAdminMixin`.\n\n```python\nfrom django.contrib import admin\nfrom fsm_admin_lite.mixins import FSMAdminMixin\n\n@admin.register(MyModel)\nclass MyModelAdmin(FSMAdminMixin, admin.ModelAdmin):\n    fsm_fields = [\n        "state",\n    ]\n```\n\n---\n\n## Configuration\n\n| Admin class attribute             | Option                                              |\n|-----------------------------------|-----------------------------------------------------|\n| `fsm_fields`                      | List of FSM fields to handle                        |\n| `fsm_transition_success_msg`      | Admin message for transition success                |\n| `fsm_transition_error_msg`        | Admin message for transition error                  |\n| `fsm_transition_not_allowed_msg`  | Admin message for transition not allowed error      |\n| `fsm_transition_not_valid_msg`    | Admin message for transition not valid error        |\n| `fsm_context_key`                 | Template context key for FSM transitions            |\n| `fsm_post_param`                  | POST parameter name for FSM transitions             |\n\n---\n\n## Run example\n\n```\nmake example\n```\n\nThen go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), login with `admin`/`password` and create a new blog post object.\n\n\n---\n\n## TODO\n- improve the default template files\n- display all the transitions (not available transition should be represented as disabled buttons)\n',
    'author': 'Matthieu Etchegoyen',
    'author_email': 'etchegom@gmail.com',
    'maintainer': 'Matthieu Etchegoyen',
    'maintainer_email': 'etchegom@gmail.com',
    'url': 'https://github.com/etchegom/django-fsm-admin-lite',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
