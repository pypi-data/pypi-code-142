import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

DEFAULT_RETRY_STRATEGY = Retry(
    total=4,
    backoff_factor=1.5,
    allowed_methods=None,
    status_forcelist=[429, 500, 502, 503, 504],
)


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, timeout=5.0, max_retries=DEFAULT_RETRY_STRATEGY, **kwargs):
        self.timeout = timeout
        super().__init__(max_retries=max_retries, **kwargs)

    def send(self, request, **kwargs):
        if kwargs.get("timeout") is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


session_timeout_retry = requests.Session()
_adapter = TimeoutHTTPAdapter()
session_timeout_retry.mount("http://", _adapter)
session_timeout_retry.mount("https://", _adapter)
