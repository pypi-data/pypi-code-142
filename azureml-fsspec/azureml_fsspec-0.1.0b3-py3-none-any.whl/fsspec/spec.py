# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Contains fsspec api implementation for aml uri
"""
from __future__ import absolute_import, division, print_function

from fsspec.asyn import (
    AsyncFileSystem,
    get_loop,
    sync
)

import re
import azureml.dataprep as _dprep
from azureml.dataprep.api._loggerfactory import track, _LoggerFactory
from azureml.dataprep.api._constants import ACTIVITY_INFO_KEY, ERROR_CODE_KEY, \
    COMPLIANT_MESSAGE_KEY, OUTER_ERROR_CODE_KEY
from azureml.dataprep.api.functions import get_stream_properties
from azureml.dataprep.rslex import StreamInfo, CachingOptions, BufferingOptions, Downloader
from fsspec.utils import infer_storage_options


_PUBLIC_API = 'PublicApi'
_APP_NAME = 'azureml-fsspec'
_logger = None


def _get_logger():
    global _logger
    if _logger is None:
        _logger = _LoggerFactory.get_logger(__name__)
    return _logger


class AzureMachineLearningFileSystem(AsyncFileSystem):
    """
    Access Azure Machine Learning defined URI as if it were a file system.
    This exposes a filesystem-like API on top of Azure Machine Learning defined URI

    .. remarks::
        This will enable pandas/dask to load Azure Machine Learning defined URI.

        .. code-block:: python
            # list all the files from a folder
            datastore_uri_fs = AzureMachineLearningFileSystem(uri=
                'azureml://subscriptions/{sub_id}/resourcegroups/{rs_group}/'
                'workspaces/{ws}/datastores/{my_datastore}/paths/folder/')
            datastore_uri_fs.ls()

            # load parquet file to pandas
            import pandas
            df = pandas.read_parquet('azureml://subscriptions/{sub_id}/resourcegroups/{rs_group}/workspaces/{ws}'
                                     '/datastores/workspaceblobstore/paths/myfolder/mydata.parquet')

            # load csv file to pandas
            import pandas
            df = pandas.read_csv('azureml://subscriptions/{sub_id}/resourcegroups/{rs_group}/workspaces/{ws}'
                                 '/datastores/workspaceblobstore/paths/myfolder/mydata.csv')

            # load parquet file to dask
            import dask.dataframe as dd
            df = dd.read_parquet('azureml://subscriptions/{sub_id}/resourcegroups/{rs_group}/workspaces/{ws}'
                                 '/datastores/workspaceblobstore/paths/myfolder/mydata.parquet')

            # load csv file to dask
            import dask.dataframe as dd
            df = dd.read_csv('azureml://subscriptions/{sub_id}/resourcegroups/{rs_group}/workspaces/{ws}'
                             '/datastores/workspaceblobstore/paths/myfolder/mydata.csv')

    :param uri: Azure Machine Learning defined URI
        Currently we support datastore uri, "azureml://subscriptions/([^\/]+)/resourcegroups/([^\/]+)/
        (?:Microsoft.MachineLearningServices/)?workspaces/([^\/]+)/datastores/([^\/]+)/paths/(.*)"
    :type uri: str
    """

    protocol = "azureml"

    @track(_get_logger, custom_dimensions={'app_name': _APP_NAME})
    def __init__(
            self,
            uri: str = None,
            **kwargs):
        """
        Initialize a new AzureMachineLearningFileSystem object

        :param uri: the uri to initialize AzureMachineLearningFileSystem.
        :type uri: str

        """
        super().__init__(
            asynchronous=False, loop=get_loop()
        )

        subscription_id, resource_group, workspace_name, datastore_name, datastore_path = \
            AzureMachineLearningFileSystem._infer_storage_options(uri)
        dataflow = _dprep.Dataflow(_dprep.api.engineapi.api.get_engine_api())
        dataflow = dataflow.add_step(
            'Microsoft.DPrep.GetDatastoreFilesBlock',
            {'datastores': [{
                'subscription': subscription_id,
                'resourceGroup': resource_group,
                'workspaceName': workspace_name,
                'datastoreName': datastore_name,
                'path': datastore_path
            }]})

        self._workspace_context = {
            'subscription': subscription_id,
            'resource_group': resource_group,
            'workspace_name': workspace_name
        }
        _LoggerFactory.trace(_get_logger(), "__init__", self._workspace_context)

        stream_properties_expression = get_stream_properties(dataflow['Path'])
        dataflow = dataflow._add_columns_from_record(stream_properties_expression)
        records = dataflow._to_pyrecords()
        if len(records) < 1:
            raise ValueError(f'No files found for {uri}')
        else:
            self._stream_infos = {}
            for r in records:
                si = StreamInfo(r['Path'].handler, r['Path'].resource_identifier, r['Path'].arguments)
                name = r['Path'].resource_identifier
                size = r['Size']
                self._stream_infos[name] = {'stream_info': si, 'info': {'name': name, 'size': size, 'type': 'file'}}

    @track(_get_logger, custom_dimensions={'app_name': _APP_NAME})
    def info(self, path):
        """
        Info api

        :param path: the path to return info for.
        :type path: str
        :return: A dictionary of file details
        :rtype: dict
        """
        return sync(self.loop, self._info, path)

    async def _info(self, path):
        """ needed by dask dataframe loading with globbing pattern
        """
        if len(self._stream_infos) == 1:
            return list(self._stream_infos.values())[0]['info']
        return self._stream_infos[path]['info']

    @track(_get_logger, custom_dimensions={'app_name': _APP_NAME})
    def ls(self, path=None, **kwargs):
        """
        List uri, this will return the full list of files iteratively.

        :param path: not needed in list logic, but api signature needed by other library like torchdata
        :type path: str
        :return: A list of file paths
        :rtype: list[str]
        """
        return list(self._stream_infos.keys())

    @track(_get_logger, custom_dimensions={'app_name': _APP_NAME})
    def glob(self, path=None, **kwargs):
        """
        globbing result for the uri

        :param path: path is not used in the logic, always globbing the uri of the file system, required by dask
        :type path: str
        :return: A list of file paths
        :rtype: list[str]
        """
        return list(self._stream_infos.keys())

    def open(
        self,
        path: str = None,
        mode: str = 'rb',
        **kwargs,
    ):
        """
        Open a file from a datastore uri

        :param path: the path to open, default to the first file
        :type path: str
        :param mode: mode to open the file, supported modes are ['r', 'rb'], both means read byte
        :type mode: str
        :return: OpenFile
        :rtype: OpenFile
        """

        """Open a file from a datastore uri

        Parameters
        ----------
        path: str
            Path to file to open, result returned from ls() or glob()
        """
        custom_dimensions = {'app_name': _APP_NAME}
        custom_dimensions.update(self._workspace_context)

        with _LoggerFactory.track_activity(_get_logger(), 'open', _PUBLIC_API,
                                           custom_dimensions) as activityLogger:
            try:
                from azureml.dataprep.api._rslex_executor import get_rslex_executor
                get_rslex_executor()

                downloader = Downloader(block_size=8 * 1024 * 1024, read_threads=64,
                                        caching_options=CachingOptions(memory_cache_size=2 * 1024 * 1024 * 1024))

                self._validate_args_for_open(path, mode)
                if len(self._stream_infos) == 1 or path is None:
                    return list(self._stream_infos.values())[0]['stream_info'].open(
                        buffering_options=BufferingOptions(64, downloader))
                return self._stream_infos[path]['stream_info'].open(buffering_options=BufferingOptions(64, downloader))
            except Exception as e:
                if hasattr(activityLogger, ACTIVITY_INFO_KEY):
                    activityLogger.activity_info['error_code'] = getattr(e, ERROR_CODE_KEY, '')
                    activityLogger.activity_info['message'] = getattr(e, COMPLIANT_MESSAGE_KEY, str(e))
                    activityLogger.activity_info['outer_error_code'] = getattr(e, OUTER_ERROR_CODE_KEY, '')

                raise

    @track(_get_logger, custom_dimensions={'app_name': _APP_NAME})
    def _validate_args_for_open(self, path, mode):
        if path is not None and len(self._stream_infos) > 1 and path not in self._stream_infos.keys():
            raise KeyError(f'Invalid path {path}, list of paths are {self._stream_infos.keys()}')

        supported_modes = ['r', 'rb']
        if mode not in supported_modes:
            raise ValueError(f'Invalid mode {mode}, supported modes are {supported_modes}, '
                             'both means read as byte array')

    @staticmethod
    def _infer_storage_options(path):
        _datastore_uri_regex_pattern = re.compile(
            r'^azureml://subscriptions/([^\/]+)/resourcegroups/([^\/]+)/'
            r'(?:providers/Microsoft.MachineLearningServices/)?workspaces/([^\/]+)/datastores/([^\/]+)/paths/(.*)',
            re.IGNORECASE)

        datastore_uri_match = _datastore_uri_regex_pattern.match(path)
        if datastore_uri_match:
            return \
                datastore_uri_match[1], datastore_uri_match[2], datastore_uri_match[3], \
                datastore_uri_match[4], datastore_uri_match[5]
        else:
            raise ValueError(f'{path} is not a valid datastore uri: '
                             f'azureml://subscriptions/([^\/]+)/resourcegroups/([^\/]+)/'
                             f'(?:Microsoft.MachineLearningServices/)?workspaces/([^\/]+)/'
                             f'datastores/([^\/]+)/paths/(.*)')

    @staticmethod
    def _get_kwargs_from_urls(path):
        """ Directly return the path """
        out = {}
        out["uri"] = path
        return out

    @classmethod
    def _strip_protocol(cls, path):
        ops = infer_storage_options(path)
        return ops["path"]
