# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hardeneks',
 'hardeneks.cluster_wide',
 'hardeneks.cluster_wide.reliability',
 'hardeneks.cluster_wide.security',
 'hardeneks.namespace_based',
 'hardeneks.namespace_based.reliability',
 'hardeneks.namespace_based.security']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.2,<2.0.0',
 'kubernetes>=25.3.0,<26.0.0',
 'pre-commit>=2.20.0,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['hardeneks = hardeneks:app']}

setup_kwargs = {
    'name': 'hardeneks',
    'version': '0.1.5',
    'description': '',
    'long_description': '# Hardeneks\n\n#### This is not an officially supported AWS product.\n\n[![PyPI version](https://badge.fury.io/py/hardeneks.svg)](https://badge.fury.io/py/hardeneks)\n[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/hardeneks.svg)](https://pypi.python.org/pypi/hardeneks/)\n[![Python package](https://github.com/dorukozturk/hardeneks/actions/workflows/ci.yaml/badge.svg)](https://github.com/dorukozturk/hardeneks/actions/workflows/ci.yaml)\n[![codecov](https://codecov.io/gh/dorukozturk/hardeneks/branch/main/graph/badge.svg?token=jrB7uWUHdr)](https://codecov.io/gh/dorukozturk/hardeneks)\n\n\nRuns checks to see if an EKS cluster follows [EKS Best Practices](https://aws.github.io/aws-eks-best-practices/).\n\n**Quick Start**:\n\n```\npython3 -m venv /tmp/.venv\nsource /tmp/.venv/bin/activate\npip install hardeneks\nhardeneks --context <K8S_CONTEXT> --cluster <CLUSTER_NAME> --region <AWS_REGION>\n```\n\n![alt text](https://github.com/dorukozturk/hardeneks/blob/e9168a857a57a13cee8fae870e33d585d8bd3be1/docs/hardeneks.png)\n\n- <b><K8S_CONTEXT><b> \n  \n    You can get the contexts by running:\n    ```\n    kubectl config get-contexts\n    ```\n    or get the current context by running:\n    ```\n    kubectl config current-context\n    ```\n\n- <b><CLUSTER_NAME><b>\n  \n    You can get the cluster names by running:\n    ```\n    aws eks list-clusters --region us-east-1\n    ```\n  \n**Configuration File**:\n\nDefault behavior is to run all the checks. If you want to provide your own config file to specify list of rules to run, you can use the --config flag.You can also add namespaces to be skipped. \n\nFollowing is a sample config file:\n\n```yaml\n---\nignore-namespaces:\n  - kube-node-lease\n  - kube-public\n  - kube-system\n  - kube-apiserver\nrules: \n  cluster_wide:\n    security:\n      iam:\n        - disable_anonymous_access_for_cluster_roles\n        - check_endpoint_public_access\n        - check_aws_node_daemonset_service_account\n        - check_access_to_instance_profile\n        - restrict_wildcard_for_cluster_roles\n      multi_tenancy:\n        - ensure_namespace_quotas_exist\n      detective_controls:\n        - check_logs_are_enabled\n      network_security:\n        - check_vpc_flow_logs\n        - check_awspca_exists\n        - check_default_deny_policy_exists\n      encryption_secrets:\n        - use_encryption_with_ebs\n        - use_encryption_with_efs\n        - use_efs_access_points\n      infrastructure_security:\n        - deploy_workers_onto_private_subnets\n        - make_sure_inspector_is_enabled\n      pod_security:\n        - ensure_namespace_psa_exist\n      image_security:\n        - use_immutable_tags_with_ecr\n    reliability:\n      applications:\n        - check_metrics_server_is_running\n        - check_vertical_pod_autoscaler_exists\n  namespace_based:\n    security: \n      iam:\n        - disable_anonymous_access_for_roles\n        - restrict_wildcard_for_roles\n        - disable_service_account_token_mounts\n        - disable_run_as_root_user\n        - use_dedicated_service_accounts_for_each_deployment\n        - use_dedicated_service_accounts_for_each_stateful_set\n        - use_dedicated_service_accounts_for_each_daemon_set\n      pod_security:\n        - disallow_container_socket_mount\n        - disallow_host_path_or_make_it_read_only\n        - set_requests_limits_for_containers\n        - disallow_privilege_escalation\n        - check_read_only_root_file_system\n      network_security:\n        - use_encryption_with_aws_load_balancers\n      encryption_secrets:\n        - disallow_secrets_from_env_vars    \n      runtime_security:\n        - disallow_linux_capabilities\n    reliability:\n      applications:\n        - check_horizontal_pod_autoscaling_exists\n        - schedule_replicas_across_nodes\n        - run_multiple_replicas\n        - avoid_running_singleton_pods\n```\n  \n\n## For Developers\n\n**Prerequisites**:\n\n* This cli uses poetry. Follow instructions that are outlined [here](https://python-poetry.org/docs/) to install poetry.\n\n\n**Installation**:\n\n```console\ngit clone git@github.com:dorukozturk/hardeneks.git\ncd hardeneks\npoetry install\n```\n\n**Running Tests**:\n\n```console\npoetry shell\npytest --cov=hardeneks tests/ --cov-report term-missing\n```\n',
    'author': 'Doruk Ozturk',
    'author_email': 'dozturk@amazon.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
