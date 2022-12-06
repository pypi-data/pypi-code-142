# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redhat_opentelemetry_contrib']

package_data = \
{'': ['*']}

install_requires = \
['opentelemetry-api>=1.14.0,<2.0.0',
 'opentelemetry-distro>=0.35b0,<0.36',
 'opentelemetry-sdk>=1.14.0,<2.0.0',
 'setuptools>=65.6.3,<66.0.0']

entry_points = \
{'opentelemetry_instrumentor': ['__main__ = '
                                'redhat_opentelemetry_contrib.script_instrumentor:ScriptInstrumentor'],
 'opentelemetry_metrics_exporter': ['file = '
                                    'redhat_opentelemetry_contrib.file_exporters:FileMetricExporter'],
 'opentelemetry_traces_exporter': ['file = '
                                   'redhat_opentelemetry_contrib.file_exporters:FileSpanExporter']}

setup_kwargs = {
    'name': 'redhat-opentelemetry-contrib',
    'version': '0.0.0.post6.dev0',
    'description': 'OpenTelementry Python extensions written at Red Hat',
    'long_description': 'redhat-opentelemetry-python-contrib\n===================================\nOpenTelemetry Python extensions written at Red Hat\n\nThis repository includes:\n* File exporters to export OpenTelemetry data to files when using auto-instrumentation\n* Script instrumentor - Auto instrumentation plugin for wrapping an entire\n  python script run in a tracing span\n\nInstallation\n------------\n```\npip install redhat-opentelemetry-python-contrib\n```\n\nUsing the file exporters\n------------------------\nThe file exporters can be used by setting the `OTEL_*_EXPORTER` environment\nvariables to `file`, or using the equivalent arguments to\n`opentelemetry-instrument`.\n\nFor example to export span data to a file for a particular Python script:\n```\nopentelemetry-instrument --traces_exporter file python myscript.py\n```\n\nThe file to which the data will be written to can be customized using the\nenvironment variables listed below. Otherwise, the listed default value would\nbe used:\n\n| Variable                         | Used for   | Default value      |\n| -------------------------------- | ---------- | ------------------ |\n| `OTEL_FILE_SPAN_EXPORTER_NAME`   | Trace data | `otel_traces.log`  |\n| `OTEL_FILE_METRIC_EXPORTER_NAME` | Metrics    | `otel_metrics.log` |\n| `OTEL_FILE_LOG_EXPORTER_NAME`    | Logs       | `otel_logs.log`    |\n\nUsing the script instrumentor\n-----------------------------\nOnce installed, the script instrumentor will automatically wrap any Python\nscript invoked with auto instrumentation enabled in a span that would include\nthe script name, command-line arguments and exit status.\n\nThe script instrumentor attempts to propagate the tracing context from the\nenvironment it was invoked in, by trying to read environment variables that are\ncapitalized versions of the HTTP headers defined by the [W3C Trace Context\nspecification][w3c]. This typically means that if the `TRACEPARENT` environment\nvariable is defined in the environment the script runs in, the script span will\nbecome a child span of that trace. This is generally compatible with how other\ntools and systems handle things such as the [Ansible OpenTelemetry callback\nplugin][ans] and the [Jenkins OpenTelemetry plugin][jnk].\n\nThe script instrumentor can cause traces to look a bit strange for things that\nare not meant to be stand-alone Python scripts such as Django and Flask server\nprocesses. It can be disabled by setting the\n`OTEL_PYTHON_DISABLED_INSTRUMENTATIONS` environment variable:\n```\nexport OTEL_PYTHON_DISABLED_INSTRUMENTATIONS="__main__"\n```\n\n[w3c]: https://www.w3.org/TR/trace-context/\n[ans]: https://docs.ansible.com/ansible/latest/collections/community/general/opentelemetry_callback.html\n[jnk]: https://github.com/jenkinsci/opentelemetry-plugin\n',
    'author': 'Barak Korren',
    'author_email': 'bkorren@redhat.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
