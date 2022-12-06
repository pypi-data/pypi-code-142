from typing import Optional

import typer
import requests
import time

from auth0.v3.authentication.token_verifier import (
    TokenVerifier,
    AsymmetricSignatureVerifier,
)

AUTH0_CLIENT_ID = "TwXR51Vz8JbY8GUUMy6EyuVR0fTO7N4N"
AUTH0_DOMAIN = "dev-n2t1kjuo8uh0ddfg.us.auth0.com"
AUTH0_SCOPE = "openid profile email offline_access"
AUTH0_ALGORITHMS = ["RS256"]


def login() -> dict:
    """
    Runs the device authorization flow and stores the user object in memory
    """
    device_code_payload = {"client_id": AUTH0_CLIENT_ID, "scope": AUTH0_SCOPE}
    device_code_response = requests.post(
        "https://{}/oauth/device/code".format(AUTH0_DOMAIN), data=device_code_payload
    )

    if device_code_response.status_code != 200:
        print("Error generating the device code")
        raise typer.Exit(code=1)

    print("Device code successful")
    device_code_data = device_code_response.json()
    print(
        "1. On your computer or mobile device navigate to: ",
        device_code_data["verification_uri_complete"],
    )
    print("2. Enter the following code: ", device_code_data["user_code"])

    token_payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        "device_code": device_code_data["device_code"],
        "client_id": AUTH0_CLIENT_ID,
    }

    while True:
        print("Checking if the user completed the flow...")
        token_response = requests.post(
            "https://{}/oauth/token".format(AUTH0_DOMAIN), data=token_payload
        )

        token_data = token_response.json()
        if token_response.status_code == 200:
            print("Authenticated!")

            validate_token(token_data["id_token"])

            return token_data

        elif token_data["error"] not in ("authorization_pending", "slow_down"):
            print(token_data["error_description"])
            raise typer.Exit(code=1)

        else:
            time.sleep(device_code_data["interval"])


def refresh(token: str) -> dict:
    token_payload = {
        "grant_type": "refresh_token",
        "client_id": AUTH0_CLIENT_ID,
        "refresh_token": token,
    }

    token_response = requests.post(
        "https://{}/oauth/token".format(AUTH0_DOMAIN), data=token_payload
    )

    token_data = token_response.json()
    if token_response.status_code == 200:
        # DEBUG: print("Authenticated!")

        validate_token(token_data["id_token"])

        return token_data
    else:
        print(token_data["error_description"])
        raise typer.Exit(code=1)


def get_user_info(access_token) -> dict:
    userinfo_response = requests.post(
        "https://{}/userinfo".format(AUTH0_DOMAIN),
        headers={"Authorization": access_token},
    )

    return userinfo_response.json()


def validate_token(id_token):
    """
    Verify the token and its precedence

    :param id_token:
    """
    jwks_url = "https://{}/.well-known/jwks.json".format(AUTH0_DOMAIN)
    issuer = "https://{}/".format(AUTH0_DOMAIN)

    sv = AsymmetricSignatureVerifier(jwks_url)
    tv = TokenVerifier(signature_verifier=sv, issuer=issuer, audience=AUTH0_CLIENT_ID)
    tv.verify(id_token)
