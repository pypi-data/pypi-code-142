from cerebrium.flow import CerebriumFlow, ModelType, _flow_string, _check_flow_type
from cerebrium.errors import CerebriumDeploymentError
from cerebrium.conduit import Conduit
from cerebrium.requests import _cerebrium_request
from cerebrium.utils import _convert_input_data

import requests
import json
from typing import Union
from yaspin import yaspin
from yaspin.spinners import Spinners
from tenacity import retry, stop_after_delay, wait_fixed

from numpy import ndarray
from torch import Tensor


def model_api_request(
    model_endpoint: str,
    data: Union[list, ndarray, Tensor],
    api_key: str,
) -> dict:
    """
    Make a request to the Cerebrium model API.

    Args:
        model_endpoint (str): The endpoint of the model to make a request to.
        data (list): The data to send to the model.

    Returns:
        dict ('status_code': int, 'data': dict): The response code and data.
    """

    payload = _convert_input_data(data)
    headers = {"Authorization": api_key}
    response = requests.request(
        "POST", model_endpoint, headers=headers, data=json.dumps(payload), timeout=30
    )
    return {"status_code": response.status_code, "data": json.loads(response.text)}


@retry(stop=stop_after_delay(60), wait=wait_fixed(2))
def _poll_deployment_status(conduit_name: str, api_key: str) -> str:
    """
    Poll the deployment status of a conduit.

    Args:
        conduit_name (str): The name of the conduit to check the status of.
        api_key (str): The API key for the Cerebrium account.

    Returns:
        str: The endpoint of the deployed model.
    """
    # Check the status of the deployment by polling the Cerebrium API for deployment status
    with yaspin(
        spinner=Spinners.arc, text="Checking deployment status...", color="magenta"
    ) as spinner:
        response = _cerebrium_request(
            "checkDeploymentStatus",
            api_key,
            payload={"arguments": {"name": conduit_name}},
        )
    if response["data"]["status"] == "deployed":
        endpoint = response["data"]["endpoint"] + "/predict"
        print("✅ Conduit deployed!")
        return endpoint
    elif response["data"]["status"] == "failed":
        print("❌ Conduit deployment failed.")
        raise CerebriumDeploymentError(response["data"]["failureMessage"])
    else:
        print("⏳ Conduit deployment in progress...")
        raise CerebriumDeploymentError(
            "Deployment Not Complete. Your conduit might be large and take longer to deploy. Please try again later."
        )


def deploy(
    model_flow: CerebriumFlow,
    name: str,
    api_key: str,
    dry_run=False,
) -> str:
    """
    Deploy a model to Cerebrium.

    Args:
        model_flow (CerebriumFlow): The flow to deploy. This is a list of ModelType, model path and postprocessor tuples, as such:
            [(ModelType.TORCH, "model.pt", postprocess_f)]
        name (str): The name to deploy the flow under.
        api_key (str): The API key for the Cerebrium account.
        description (str): An optional description of the model or flow.
        dry_run (bool): Whether to run the deployment in dry-run mode.
            If True, the model will not be deployed, and deploy will return a flow function which can be used to test with.

    Returns:
        str: The newly deployed REST endpoint. If dry_run is True, a flow function will be returned instead.
    """
    # Check that the flow is valid and create the Conduit
    model_flow = _check_flow_type(model_flow)
    conduit = Conduit(name, api_key, model_flow)

    # Deploy the conduit
    if not dry_run:
        # Check that the user is authenticated
        upload_url_response = _cerebrium_request(
            "getUploadUrl",
            api_key,
            payload={"name": name},
            enable_spinner=(
                True,
                ("Authenticating...", "Authenticated with Cerebrium!"),
            ),
        )
        upload_url = upload_url_response["data"]["uploadUrl"]

        # If Prebuilt model, register with modal
        if model_flow[0][0] == ModelType.PREBUILT:
            print("Registering with Cerebrium...")
            prebuilt_model_response = _cerebrium_request(
                "pre-built-model",
                api_key,
                payload={
                    "arguments": {
                        "name": name,
                        "externalId": model_flow[0][1],
                        "modelType": _flow_string(model_flow),
                    }
                },
                enable_spinner=(
                    True,
                    ("Registering with Cerebrium...", "Registered with Cerebrium!"),
                ),
            )
            endpoint = prebuilt_model_response["data"]["internalEndpoint"]
            print("🌍 Endpoint:", endpoint)
            return endpoint
        else:
            # Upload the conduit artefacts to Cerebrium
            print("⬆️  Uploading conduit artefacts...")
            conduit._upload(upload_url)
            print("✅ Conduit artefacts uploaded successfully.")
            endpoint = _poll_deployment_status(name, api_key)
            print("🌍 Endpoint:", endpoint)
            return endpoint
    else:
        if model_flow[0][0] == ModelType.PREBUILT:
            raise NotImplementedError("Dry run not supported for prebuilt models")
        conduit.load(direct_from_flow=True)
        return conduit
