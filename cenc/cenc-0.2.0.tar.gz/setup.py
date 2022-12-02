# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cenc']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['cenc = cenc.main:app']}

setup_kwargs = {
    'name': 'cenc',
    'version': '0.2.0',
    'description': '',
    'long_description': 'Start an encoding task with passing the full ffmpeg command to the `cenc` command.\n\nA trivial example that prints the version of ffmpeg on our system:\n\n```bash\ncenc ffmpeg --help\n```\n\nA more complex example that resizes a video file hosted on a remote server:\n\n```bash\ncenc ffmpeg -i \'https://storage.googleapis.com/kapan_public_videos/SampleVideo_1280x720_1mb%20(1).mp4\' -vf scale=320:240 output.mp4\n```\n\nTask ID is returned immediately after the task is created. \nYou can use the task ID to check the status of the task.\nThe logs will be printed to the standard output until the task is finished.\n\nYou can download the outputs of the task, after the task is finished.\nThe url for the each output file will be printed to the console, such as:\n\n```\n{\n  "id": "b6c0d5607f224dc3b646068710d2e08a",\n  "output.mp4": "https://storage.googleapis.com/store/tmp/ffmpeg/b6c0d5607f224dc3b646068710d2e08a/output.mp4",\n  "returncode": "0",\n  "status": "done"\n}\n```\n\n\n## Using the API directly\n\nThe API is available at `https://ffmpeg-kopg2w5bka-ez.a.run.app`.\nYou can start a task by sending a POST request to the `/ffmpeg` endpoint with the full ffmpeg command in the params.\n\n```python\nendpoint = "https://ffmpeg-kopg2w5bka-ez.a.run.app"\ncommand = "ffmpeg -i \'https://storage.googleapis.com/kapan_public_videos/SampleVideo_1280x720_1mb%20(1).mp4\' -vf scale=320:240 output.mp4"\nresponse = requests.post(endpoint, params={"command": command})\ntask_id = response.json()["id"]\n```\n\nYou can check the status of the task by sending a GET request to the `/ffmpeg/<task_id>` endpoint.\n\n```python\nwhile True:\n    time.sleep(2)\n    response = requests.get(f"{endpoint}/ffmpeg/{task_id}")\n    if response.status_code != 200:\n        # Task has not been started processing yet\n        continue\n    \n    results = response.json()\n\n    if results.get("returncode"):\n        # Task has finished processing\n        print(results)\n        break\n```',
    'author': 'Aziz Berkay Yesilyurt',
    'author_email': 'abyesilyurt@gmail.com',
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
