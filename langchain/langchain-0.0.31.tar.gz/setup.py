# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['langchain',
 'langchain.agents',
 'langchain.agents.mrkl',
 'langchain.agents.react',
 'langchain.agents.self_ask_with_search',
 'langchain.chains',
 'langchain.chains.api',
 'langchain.chains.conversation',
 'langchain.chains.llm_bash',
 'langchain.chains.llm_math',
 'langchain.chains.natbot',
 'langchain.chains.pal',
 'langchain.chains.qa_with_sources',
 'langchain.chains.sql_database',
 'langchain.chains.vector_db_qa',
 'langchain.docstore',
 'langchain.embeddings',
 'langchain.llms',
 'langchain.prompts',
 'langchain.prompts.example_selector',
 'langchain.utilities',
 'langchain.vectorstores']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6,<7',
 'SQLAlchemy>=1,<2',
 'numpy>=1,<2',
 'pydantic>=1,<2',
 'requests>=2,<3']

extras_require = \
{'all': ['faiss-cpu>=1,<2',
         'wikipedia>=1,<2',
         'elasticsearch>=8,<9',
         'manifest-ml>=0.0.1,<0.0.2',
         'spacy>=3,<4',
         'nltk>=3,<4',
         'transformers>=4,<5',
         'beautifulsoup4>=4,<5'],
 'llms': ['manifest-ml>=0.0.1,<0.0.2']}

setup_kwargs = {
    'name': 'langchain',
    'version': '0.0.31',
    'description': 'Building applications with LLMs through composability',
    'long_description': '# 🦜️🔗 LangChain\n\n⚡ Building applications with LLMs through composability ⚡\n\n[![lint](https://github.com/hwchase17/langchain/actions/workflows/lint.yml/badge.svg)](https://github.com/hwchase17/langchain/actions/workflows/lint.yml) [![test](https://github.com/hwchase17/langchain/actions/workflows/test.yml/badge.svg)](https://github.com/hwchase17/langchain/actions/workflows/test.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchainai.svg?style=social&label=Follow%20%40LangChainAI)](https://twitter.com/langchainai) [![](https://dcbadge.vercel.app/api/server/6adMQxSpJS?compact=true&style=flat)](https://discord.gg/6adMQxSpJS)\n\n## Quick Install\n\n`pip install langchain`\n\n## 🤔 What is this?\n\nLarge language models (LLMs) are emerging as a transformative technology, enabling\ndevelopers to build applications that they previously could not.\nBut using these LLMs in isolation is often not enough to\ncreate a truly powerful app - the real power comes when you are able to\ncombine them with other sources of computation or knowledge.\n\nThis library is aimed at assisting in the development of those types of applications.\n\n## 📖 Documentation\n\nPlease see [here](https://langchain.readthedocs.io/en/latest/?) for full documentation on:\n- Getting started (installation, setting up environment, simple examples)\n- How-To examples (demos, integrations, helper functions)\n- Reference (full API docs)\n- Resources (high level explanation of core concepts)\n\n## 🚀 What can this help with?\n\nThere are three main areas (with a forth coming soon) that LangChain is designed to help with.\nThese are, in increasing order of complexity:\n1. LLM and Prompts\n2. Chains\n3. Agents\n4. Memory\n\nLet\'s go through these categories and for each one identify key concepts (to clarify terminology) as well as the problems in this area LangChain helps solve.\n\n### LLMs and Prompts\nCalling out to an LLM once is pretty easy, with most of them being behind well documented APIs.\nHowever, there are still some challenges going from that to an application running in production that LangChain attempts to address.\n\n**Key Concepts**\n- LLM: A large language model, in particular a text-to-text model.\n- Prompt: The input to a language model. Typically this is not simply a hardcoded string but rather a combination of a template, some examples, and user input.\n- Prompt Template: An object responsible for constructing the final prompt to pass to a LLM.\n- Examples: Datapoints that can be included in the prompt in order to give the model more context what to do.\n- Few Shot Prompt Template: A subclass of the PromptTemplate class that uses examples.\n- Example Selector: A class responsible to selecting examples to use dynamically (depending on user input) in a few shot prompt.\n\n**Problems Solved**\n- Switching costs: by exposing a standard interface for all the top LLM providers, LangChain makes it easy to switch from one provider to another, whether it be for production use cases or just for testing stuff out.\n- Prompt management: managing your prompts is easy when you only have one simple one, but can get tricky when you have a bunch or when they start to get more complex. LangChain provides a standard way for storing, constructing, and referencing prompts.\n- Prompt optimization: despite the underlying models getting better and better, there is still currently a need for carefully constructing prompts. \n\n### Chains\nUsing an LLM in isolation is fine for some simple applications, but many more complex ones require chaining LLMs - either with eachother or with other experts.\nLangChain provides several parts to help with that.\n\n**Key Concepts**\n- Tools: APIs designed for assisting with a particular use case (search, databases, Python REPL, etc). Prompt templates, LLMs, and chains can also be considered tools.\n- Chains: A combination of multiple tools in a deterministic manner.\n\n**Problems Solved**\n- Standard interface for working with Chains\n- Easy way to construct chains of LLMs\n- Lots of integrations with other tools that you may want to use in conjunction with LLMs \n- End-to-end chains for common workflows (database question/answer, recursive summarization, etc)\n\n### Agents\nSome applications will require not just a predetermined chain of calls to LLMs/other tools, but potentially an unknown chain that depends on the user input.\nIn these types of chains, there is a “agent” which has access to a suite of tools.\nDepending on the user input, the agent can then decide which, if any, of these tools to call.\n\n**Key Concepts**\n- Tools: same as above.\n- Agent: An LLM-powered class responsible for determining which tools to use and in what order.\n\n\n**Problems Solved**\n- Standard agent interfaces\n- A selection of powerful agents to choose from\n- Common chains that can be used as tools\n\n### Memory\nBy default, Chains and Agents are stateless, meaning that they treat each incoming query independently.\nIn some applications (chatbots being a GREAT example) it is highly important to remember previous interactions,\nboth at a short term but also at a long term level. The concept of "Memory" exists to do exactly that.\n\n**Key Concepts**\n- Memory: A class that can be added to an Agent or Chain to (1) pull in memory variables before calling that chain/agent, and (2) create new memories after the chain/agent finishes.\n- Memory Variables: Variables returned from a Memory class, to be passed into the chain/agent along with the user input.\n\n**Problems Solved**\n- Standard memory interfaces\n- A collection of common memory implementations to choose from\n- Common chains/agents that use memory (e.g. chatbots)\n\n## 🤖 Developer Guide\n\nTo begin developing on this project, first clone the repo locally.\n\n### Quick Start\n\nThis project uses [Poetry](https://python-poetry.org/) as a dependency manager. Check out Poetry\'s own [documentation on how to install it](https://python-poetry.org/docs/#installation) on your system before proceeding.\n\nTo install requirements:\n\n```bash\npoetry install -E all\n```\n\nThis will install all requirements for running the package, examples, linting, formatting, and tests. Note the `-E all` flag will install all optional dependencies necessary for integration testing.\n\nNow, you should be able to run the common tasks in the following section.\n\n### Common Tasks\n\n#### Code Formatting\n\nFormatting for this project is a combination of [Black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/).\n\nTo run formatting for this project:\n\n```bash\nmake format\n```\n\n#### Linting\n\nLinting for this project is a combination of [Black](https://black.readthedocs.io/en/stable/), [isort](https://pycqa.github.io/isort/), [flake8](https://flake8.pycqa.org/en/latest/), and [mypy](http://mypy-lang.org/).\n\nTo run linting for this project:\n\n```bash\nmake lint\n```\n\nWe recognize linting can be annoying - if you do not want to do it, please contact a project maintainer and they can help you with it. We do not want this to be a blocker for good code getting contributed.\n\n#### Testing\n\nUnit tests cover modular logic that does not require calls to outside apis.\n\nTo run unit tests:\n\n```bash\nmake tests\n```\n\nIf you add new logic, please add a unit test.\n\nIntegration tests cover logic that requires making calls to outside APIs (often integration with other services).\n\nTo run integration tests:\n\n```bash\nmake integration_tests\n```\n\nIf you add support for a new external API, please add a new integration test.\n\n#### Adding a Jupyter Notebook\n\nIf you are adding a Jupyter notebook example, you\'ll want to install the optional `dev` dependencies.\n\nTo install dev dependencies:\n\n```bash\npoetry install --with dev\n```\n\nLaunch a notebook:\n\n```bash\npoetry run jupyter notebook\n```\n\nWhen you run `poetry install`, the `langchain` package is installed as editable in the virtualenv, so your new logic can be imported into the notebook.\n\n#### Contribute Documentation\n\nDocs are largely autogenerated by [sphinx](https://www.sphinx-doc.org/en/master/) from the code.\n\nFor that reason, we ask that you add good documentation to all classes and methods.\n\nSimilar to linting, we recognize documentation can be annoying - if you do not want to do it, please contact a project maintainer and they can help you with it. We do not want this to be a blocker for good code getting contributed.\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.github.com/hwchase17/langchain',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
