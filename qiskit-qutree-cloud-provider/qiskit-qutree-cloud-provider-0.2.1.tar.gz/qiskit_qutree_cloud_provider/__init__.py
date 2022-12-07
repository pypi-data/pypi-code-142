from qiskit.providers import ProviderV1 as Provider
from qiskit.providers.providerutils import filter_backends

from .backend import QuTreeCloudBackend
from ._version import __version__

QUTREE_CLOUD_ENDPOINT = "qutree-rpc-4scod3qrja-uw.a.run.app:443"


class QuTreeCloudProvider(Provider):
    def __init__(self, addr=QUTREE_CLOUD_ENDPOINT):
        super().__init__()
        self._backends = [QuTreeCloudBackend(addr)]

    def backends(self, name=None, filters=None, **kwargs):
        _backends = self._backends
        if name:
            _backends = [backend for backend in _backends if backend.name() == name]
        return filter_backends(_backends, filters=filters, **kwargs)
