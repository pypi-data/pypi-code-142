# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smol_k8s_lab',
 'smol_k8s_lab.k8s_apps',
 'smol_k8s_lab.k8s_distros',
 'smol_k8s_lab.k8s_tools']

package_data = \
{'': ['*'], 'smol_k8s_lab': ['config/*']}

install_requires = \
['bcrypt>=4.0.1,<5.0.0',
 'click>=8.1.3,<9.0.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['smol-k8s-lab = smol_k8s_lab:main']}

setup_kwargs = {
    'name': 'smol-k8s-lab',
    'version': '0.10.0',
    'description': 'bootstrap simple projects on kubernetes with kind and k3s',
    'long_description': '## ☁️ *smol k8s lab* 🧸\n\nA project aimed at getting up and running **quickly** with slimmer k8s distros in one small command line tool.\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/screenshots/help_text.svg">\n      <img src="./docs/screenshots/help_text.svg" alt="Output of smol-k8s-lab --help after cloning the directory and installing the prerequisites.">\n  </a>\n</p>\n\n\n## Docs\n\n### Quick Start\nIf you\'ve already got Python3.11 and brew installed, you should be able to:\n\n```bash\npip3.11 install smol-k8s-lab\n```\n\nWe\'ve also got a [Quickstart guide](https://jessebot.github.io/smol-k8s-lab/quickstart) for you to jump right in!\n\nThere\'s also full tutorials to manually set up different distros in the [docs we maintain](https://jessebot.github.io/smol-k8s-lab/distros) as well as BASH scripts for basic automation of each k8s distro in:\n\n`./distro/{NAME_OF_K8S_DISTRO}/bash_full_quickstart.sh`\n\n## Under the hood\n### Currently supported k8s distros\n\n- [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/k3s_icon.ico" width="26">&nbsp;&nbsp;k3s](https://k3s.io/)\n- [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/kind_icon.png" width="32">&nbsp;KinD](https://kind.sigs.k8s.io/)\n- [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/k0s-logo.svg" width="32">&nbsp;k0s](https://k0sproject.io/)\n\nWe tend to test first on k3s and then kind.\n\n\n### Stack We Install on K8s\n\n|           Application           |                      Description                      |\n|:-------------------------------:|:------------------------------------------------------|\n| 🐄</br>[Local Path Provisioner] | Default simple local file storage for persistent data |\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/metallb_icon.png" width="32px" alt="metallb logo, blue arrow pointing up, with small line on one leg of arrow to show balance">][metallb]</br> [metallb] | loadbalancer for metal, since we\'re mostly selfhosting |\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/nginx.ico" width="32px" alt="nginx logo, white letter N with green background">][nginx-ingress]</br>[nginx-ingress] | The ingress controller allows access to the cluster remotely, needed for web traffic |\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/cert-manager_icon.png" width="32px" alt="cert manager logo">][cert-manager]</br>[cert-manager] | For SSL/TLS certificates |\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/k9s_icon.png" alt="k9s logo, outline of dog with ship wheels for eyes" width="32px">][k9s]</br>[k9s] | Terminal based dashboard for kubernetes |\n\n**Current versions**\ncert-manager  v1.10.1\ningress-nginx 4.4.0\n\n\n#### Optionally installed\n\n| Application/Tool | Description |\n|:----------------:|:------------|\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/eso_icon.png" width="32" alt="ESO logo, outline of robot with astricks in a screen in it\'s belly">][ESO]</br>[ESO]  | external-secrets-operator integrates external secret management systems like GitLab|\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/argo_icon.png" width="32" alt="argo CD logo, an organer squid wearing a fishbowl helmet">][Argo CD]</br>[Argo CD] | Gitops - Continuous Deployment |\n| [<img src="https://raw.githubusercontent.com/jessebot/smol-k8s-lab/main/docs/icons/kyverno_icon.png"  width="32" alt="kyvero logo">][Kyverno]</br>[Kyverno] | Kubernetes native policy management to enforce policies on k8s resources |\n\n**Current versions**\nargo-cd          5.16.2\nexternal-secrets 0.6.1\n\nIf you install argocd, and you use bitwarden, we\'ll generate an admin password and automatically place it in your vault if you pass in the `-p` option. Curently only works with Bitwarden.\n\nWant to get started with argocd? If you\'ve installed it via smol-k8s-lab, then you can jump [here](https://github.com/jessebot/argo-example#argo-via-the-gui). Otherwise, if you want to start from scratch, start [here](https://github.com/jessebot/argo-example#argocd)\n\n\n### Tooling Used for the script itself and interface\n\n[![made-with-python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)\n\n- rich (this is what makes all the pretty formatted text)\n- PyYAML (to handle the k8s yamls and configs)\n- bcrypt (to pass a password to argocd and automatically update your bitwarden)\n- click (handles arguments for the script)\n\n\n## Troubleshooting\nIf you\'re stuck, checkout the [Notes](https://jessebot.github.io/smol-k8s-lab/notes) to see if we also got stuck on the same thing at some point :) Under each app or tool, we\'ll have notes on how to learn more about it, as well as any errors we\'ve already battled.\n\n\n## Other Notes\nCheck out the [`optional`](optional) directory for quick examples on apps this script does not default install.\n\ne.g. for postgres, go to [`./optional/postgres`](./optional/postgres)\n\n# Status\nThis is still in later alpha, as we figure out all the distros we want to support,\nand pin all the versions, but if you\'d like to contribute or just found a :bug:,\nfeel free to open an issue (or pull request), and we\'ll take a look! We\'ll try\nto get back to you asap!\n\n## Contributors\n\n<!-- readme: contributors -start -->\n<table>\n<tr>\n    <td align="center">\n        <a href="https://github.com/jessebot">\n            <img src="https://avatars.githubusercontent.com/u/2389292?v=4" width="100;" alt="jessebot"/>\n            <br />\n            <sub><b>JesseBot</b></sub>\n        </a>\n    </td>\n    <td align="center">\n        <a href="https://github.com/cloudymax">\n            <img src="https://avatars.githubusercontent.com/u/84841307?v=4" width="100;" alt="cloudymax"/>\n            <br />\n            <sub><b>Max!</b></sub>\n        </a>\n    </td></tr>\n</table>\n<!-- readme: contributors -end -->\n\n<!-- link references -->\n[metallb]: https://github.io/metallb/metallb "metallb"\n[Local Path Provisioner]: https://github.com/rancher/local-path-provisioner\n[nginx-ingress]: https://github.io/kubernetes/ingress-nginx\n[cert-manager]: https://cert-manager.io/docs/\n[k9s]: https://k9scli.io/topics/install/\n\n[ESO]: https://external-secrets.io/v0.5.9/\n[Argo CD]: https://github.io/argoproj/argo-helm\n[Kyverno]: https://github.com/kyverno/kyverno/\n',
    'author': 'Jesse Hitch',
    'author_email': 'jessebot@linux.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://jessebot.github.io/smol-k8s-lab',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0.0',
}


setup(**setup_kwargs)
