from typing import Callable, Optional, Tuple, Dict, Union, Any

import grpc
import grpc.aio as async_grpc

# TODO: move to async solution like `httpx`
import requests

# TODO: get it from the metadata too?
AUTH0_DOMAIN = "dev-n2t1kjuo8uh0ddfg.us.auth0.com"
USER_AUTH_TOKEN_KEY = "auth-token"
CONTROLLER_TOKEN_KEY = "controller-token"

# This assumes certificates to be local for the Dockerfile
# TODO: Move this read operation to happen from a secret store

with open("certs/controller.key", "rb") as fh:
    SSL_PRIVATE_KEY = fh.read()

with open("certs/controller.pem", "rb") as fh:
    SSL_CERTIFICATE_CHAIN = fh.read()


def _unautenticated(message: str):
    return lambda _, ctx: ctx.abort(grpc.StatusCode.UNAUTHENTICATED, message)


class AuthInterceptor(async_grpc.ServerInterceptor):
    def __init__(
        self,
        auth_check: Callable[[Dict[str, Union[str, bytes]], str], Any],
        *,
        metadata_field: str = USER_AUTH_TOKEN_KEY,
    ):
        self._metadata_field = metadata_field
        self._auth_check = auth_check

        # Build the method handler only once since it's always the same
        self._deny = grpc.unary_unary_rpc_method_handler(
            _unautenticated(f"Invalid key in {self._metadata_field}")
        )

    async def intercept_service(self, continuation, handler_call_details):
        metadata: Dict[str, Union[str, bytes]] = dict(
            handler_call_details.invocation_metadata
        )

        try:
            self._auth_check(metadata, self._metadata_field)
            return await continuation(handler_call_details)
        except ValueError as err:
            return grpc.unary_unary_rpc_method_handler(
                lambda _, ctx, err=err: ctx.abort(grpc.StatusCode.UNAUTHENTICATED, str(err))
            )


def server_credentials() -> grpc.ServerCredentials:
    """
    Server channel credentials.

    Used to verify that this is the correct server to be talking to for a client.
    """

    return grpc.ssl_server_credentials(
        private_key_certificate_chain_pairs=[
            (SSL_PRIVATE_KEY, SSL_CERTIFICATE_CHAIN),
        ]
    )


def auth0_check(metadata: Dict[str, Union[str, bytes]], key: str) -> str:
    token: Optional[Union[str, bytes]] = metadata.get(key, None)

    if token is None:
        raise ValueError(f"Invalid value for {key}")

    userinfo_response = requests.post(
        "https://{}/userinfo".format(AUTH0_DOMAIN),
        headers={"Authorization": token},
    )

    if userinfo_response.status_code == 200:
        userinfo_data = userinfo_response.json()
        return userinfo_data["sub"]
    else:
        msg = userinfo_response.content.decode("UTF-8")
        raise ValueError(f"Invalid value for {key}: {msg}")


def user_auth_intereceptor() -> async_grpc.ServerInterceptor:
    """
    User auth.

    Authenticates sent access_token with auth0 to verify it's real.
    """
    return AuthInterceptor(auth0_check)


def worker_call_credentials_metadata(controller_auth_key: str) -> Tuple[str, str]:
    """
    Call credentials to worker
    """
    return (CONTROLLER_TOKEN_KEY, controller_auth_key)
