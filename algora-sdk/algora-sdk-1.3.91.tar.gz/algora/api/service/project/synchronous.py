from typing import Dict, Any

from algora.api.service.project.__util import _get_project_request_info, _get_project_resource_request_info
from algora.common.decorators.data import data_request
from algora.common.requests import __get_request


@data_request(transformer=lambda data: data)
def get_project(id: str) -> Dict[str, Any]:
    """
    Get project by ID.

    Args:
        id (str): Project ID

    Returns:
        Dict[str, Any]: Project response
    """
    request_info = _get_project_request_info(id)
    return __get_request(**request_info)


@data_request(transformer=lambda data: data, processor=lambda response: response.content)
def get_project_resource(id: str) -> Any:
    """
    Get project resource by ID.

    Args:
        id (str): Resource ID

    Returns:
        Any: Resource response
    """
    request_info = _get_project_resource_request_info(id)
    return __get_request(**request_info)
