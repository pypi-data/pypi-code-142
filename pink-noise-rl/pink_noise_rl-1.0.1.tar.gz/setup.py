# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pink']

package_data = \
{'': ['*']}

install_requires = \
['numpy']

setup_kwargs = {
    'name': 'pink-noise-rl',
    'version': '1.0.1',
    'description': 'Pink noise for exploration in reinforcement learning',
    'long_description': '# Colored Action Noise for Deep RL\n\nThis repository contains easy-to-use implementations of pink noise and general colored noise for use as action noise in deep reinforcement learning. Included are the following classes:\n- `ColoredNoiseProcess` and `PinkNoiseProcess` for general use, based on the [colorednoise](https://github.com/felixpatzelt/colorednoise) library\n- `ColoredActionNoise` and `PinkActionNoise` to be used with deterministic policy algorithms like DDPG and TD3 in Stable Baselines3, both are subclasses of `stable_baselines3.common.noise.ActionNoise`\n- `ColoredNoiseDist`, `PinkNoiseDist` to be used with stochastic policy algorithms like SAC in Stable Baselines3\n- `MPO_CN` for using colored noise (incl. pink noise) with MPO using the Tonic RL library.\n\nFor more information, please see our paper: [Pink Noise Is All You Need: Colored Noise Exploration in Deep Reinforcement Learning](https://bit.ly/pink-noise-rl).\n\n## Installation\nYou can install the library via pip:\n```\npip install pink-noise-rl\n```\nNote: In Python, the import statement is simply `import pink`.\n\n## Usage\nWe provide minimal examples for using pink noise on SAC, TD3 and MPO below. An example comparing pink noise with the default action noise of SAC is included in the `examples` directory.\n\n### Stable Baselines3: SAC, TD3\n```python\nimport gym\nfrom stable_baselines3 import SAC, TD3\n\n# All classes mentioned above can be imported from `pink`\nfrom pink import PinkNoiseDist, PinkActionNoise\n\n# Initialize environment\nenv = gym.make("MountainCarContinuous-v0")\naction_dim = env.action_space.shape[-1]\nseq_len = env._max_episode_steps\n```\n\n#### SAC\n```python\n# Initialize agent\nmodel = SAC("MlpPolicy", env)\n\n# Set action noise\nmodel.actor.action_dist = PinkNoiseDist(action_dim, seq_len)\n\n# Train agent\nmodel.learn(total_timesteps=10_000)\n```\n\n#### TD3\n```python\n# Initialize agent\nmodel = TD3("MlpPolicy", env)\n\n# Set action noise\nnoise_scale = 0.3*np.ones(action_dim)\nmodel.action_noise = PinkActionNoise(noise_scale, seq_len)\n\n# Train agent\nmodel.learn(total_timesteps=10_000)\n```\n\n### Tonic: MPO\n```python\nimport gym\nfrom tonic import Trainer\nfrom pink import MPO_CN\n\n# Initialize environment\nenv = gym.make("MountainCarContinuous-v0")\nseq_len = env._max_episode_steps\n\n# Initialize agent with pink noise\nbeta = 1\nmodel = MPO_CN()\nmodel.initialize(beta, seq_len, env.observation_space, env.action_space)\n\n# Train agent\ntrainer = tonic.Trainer(steps=10_000)\ntrainer.initialize(model, env)\ntrainer.run()\n```\n\n\n## Citing\nIf you use this code in your research, please cite our paper:\n```bibtex\n@misc{eberhard-2022-pink,\n  title = {Pink {{Noise Is All You Need}}: {{Colored Noise Exploration}} in {{Deep Reinforcement Learning}}},\n  author = {Eberhard, Onno and Hollenstein, Jakob and Pinneri, Cristina and Martius, Georg},\n  date = {2022},\n  howpublished = {NeurIPS Deep RL Workshop 2022}\n}\n```\n\nIf there are any problems, or you have a question, don\'t hesitate to open an issue here on GitHub.\n',
    'author': 'Onno Eberhard',
    'author_email': 'onnoeberhard@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/martius-lab/pink-noise-rl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
