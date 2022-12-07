from typing import Dict, Any

from algora.api.service.project.__util import _get_project_request_info, _get_project_resource_request_info
from algora.common.decorators.data import async_data_request
from algora.common.requests import __async_get_request


@async_data_request(transformer=lambda data: data)
async def async_get_project(id: str) -> Dict[str, Any]:
    """
    Asynchronously get project by ID.

    Args:
        id (str): Project ID

    Returns:
        Dict[str, Any]: Project response
    """
    request_info = _get_project_request_info(id)
    return await __async_get_request(**request_info)


@async_data_request(transformer=lambda data: data, processor=lambda response: response.content)
async def async_get_project_resource(id: str) -> Any:
    """
    Asynchronously get project resource by ID.

    Args:
        id (str): Resource ID

    Returns:
        Any: Resource response
    """
    request_info = _get_project_resource_request_info(id)
    return await __async_get_request(**request_info)
