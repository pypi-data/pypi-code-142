def _get_project_request_info(id: str) -> dict:
    return {
        'endpoint': f"config/project/{id}"
    }


def _get_project_resource_request_info(id: str) -> dict:
    return {
        'endpoint': f"config/project/{id}/resource"
    }
