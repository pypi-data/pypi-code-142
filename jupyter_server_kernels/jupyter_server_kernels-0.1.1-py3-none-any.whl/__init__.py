from .app import KernelsExtensionApp


__version__ = "0.1.1"


def _jupyter_server_extension_points():  # pragma: no cover
    return [
        {
            "module": "jupyter_server_kernels.app",
            "app": KernelsExtensionApp,
        },
    ]
