# coding: utf-8

"""
    Priceloop API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table_columns_column_data.post import AddDataColumn
from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table_columns_column_expression.post import AddFormulaColumn
from priceloop_api.paths.api_v1_0_workspaces_workspace_external_functions_function.post import CreateExternalFunction
from priceloop_api.paths.api_v1_0_workspaces_workspace_external_functions_function.delete import DeleteExternalFunction
from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table.delete import DeleteTable
from priceloop_api.paths.api_v1_0_workspaces_workspace_external_functions_function.get import GetExternalFunctions
from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table.get import GetTable
from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table_data.get import GetTableData
from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table_upload_csv_url.get import GetTableUploadCsvUrl
from priceloop_api.paths.api_v1_0_workspaces_workspace.get import GetWorkspace
from priceloop_api.paths.api_v1_0_hello.get import Hello
from priceloop_api.paths.api_v1_0_hello_auth.get import HelloAuth
from priceloop_api.paths.api_v1_0_workspaces.get import ListWorkspaces
from priceloop_api.paths.api_v1_0_workspaces_workspace_tables_table_columns_column.put import UpdateColumnPosition
from priceloop_api.paths.api_v1_0_workspaces_workspace_external_functions_function.put import UpdateExternalFunction


class DefaultApi(
    AddDataColumn,
    AddFormulaColumn,
    CreateExternalFunction,
    DeleteExternalFunction,
    DeleteTable,
    GetExternalFunctions,
    GetTable,
    GetTableData,
    GetTableUploadCsvUrl,
    GetWorkspace,
    Hello,
    HelloAuth,
    ListWorkspaces,
    UpdateColumnPosition,
    UpdateExternalFunction,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
