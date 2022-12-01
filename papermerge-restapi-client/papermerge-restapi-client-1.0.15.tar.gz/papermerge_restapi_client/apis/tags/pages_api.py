# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b16
    Generated by: https://openapi-generator.tech
"""

from papermerge_restapi_client.paths.api_pages_move_to_document_.post import MoveToDocument
from papermerge_restapi_client.paths.api_pages_move_to_folder_.post import MoveToFolder
from papermerge_restapi_client.paths.api_pages_.delete import MultiplePagesDelete
from papermerge_restapi_client.paths.api_pages_reorder_.post import Reorder
from papermerge_restapi_client.paths.api_pages_id_.get import Retrieve
from papermerge_restapi_client.paths.api_pages_rotate_.post import Rotate
from papermerge_restapi_client.paths.api_pages_id_.delete import SinglePageDelete


class PagesApi(
    MoveToDocument,
    MoveToFolder,
    MultiplePagesDelete,
    Reorder,
    Retrieve,
    Rotate,
    SinglePageDelete,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
