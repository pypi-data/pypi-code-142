from myst.client import Client
from myst.openapi.models.model_fit_result_get import ModelFitResultGet


def request_sync(client: Client, project_uuid: str, model_uuid: str, uuid: str) -> ModelFitResultGet:
    """Gets the model fit result associated with the given identifier."""

    return client.request(
        method="get",
        path=f"/projects/{project_uuid}/models/{model_uuid}/fit_results/{uuid}",
        response_class=ModelFitResultGet,
    )
