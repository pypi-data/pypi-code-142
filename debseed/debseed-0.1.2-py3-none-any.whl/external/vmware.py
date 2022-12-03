from __future__ import annotations
import logging, io, atexit, re, ssl, os
from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pathlib import Path
from collections import namedtuple
from typing import TypeVar
from pyVmomi import vim, vmodl
from pyVim import connect
from ..settings import config
from ..utils import ElementInfo
from .interface import IExternal

logger = logging.getLogger(__name__)


class VmwareExternal(IExternal):
    def __init__(self):
        self.vc_kwargs: VcenterConnection = None

        self.datastore_name = config.get('debseed', 'vmware_datastore_name', fallback=None)
        self.datastore_dir = config.get('debseed', 'vmware_datastore_dir', fallback=None)

        if not (self.datastore_name and self.datastore_dir):
            return # VMWare not configured
   
        host = config.get('debseed', 'vmware_host', fallback=None)
        if not host:
            return # VMWare not configured

        self.vc_kwargs = {
            'host': host,
            'username': config.get('debseed', 'vmware_username', fallback=None),
            'password': config.get('debseed', 'vmware_password', fallback=None),
            'disable_ssl_verify': config.get('debseed', 'vmware_disable_ssl_verify', fallback=False),
        }


    def __str__(self):
        return f"VMWare: [{self.datastore_name}] {self.datastore_dir}"

    @property
    def is_enabled(self):
        return self.vc_kwargs is not None

    @property
    def vc(self):
        try:
            return self._vc
        except AttributeError:
            self._vc = VcenterConnection(**self.vc_kwargs)
            atexit.register(self._vc.__exit__)
            return self._vc


    def find(self) -> list[ElementInfo]:
        return datastore_find(self.vc, self.datastore_name, self.datastore_dir, search="*.iso", recurse=True)


    def exists(self, local: Path) -> str|None:     
        target_path = f"{self.datastore_dir}/{local.name}" if self.datastore_dir else local.name
        datastore = self.vc.find_obj(self.datastore_name, vim.Datastore)

        if found := datastore_exists(self.vc, datastore, target_path):
            return found
        
        archive_path = f"{self.datastore_dir}/archives/{local.name}" if self.datastore_dir else local.name
        if found := datastore_exists(self.vc, datastore, archive_path):
            return found

        return None


    def publish(self, local: Path, force: bool = False) -> bool:
        target_path = f"{self.datastore_dir}/{local.name}" if self.datastore_dir else local.name

        with open(local, "rb") as file:
            datastore_upload(self.vc, self.datastore_name, file, target_path)


T_Obj = TypeVar("T_Obj", bound=vim.ManagedEntity)


class VcenterConnection:
    def __init__(self, host: str, username: str, password: str, disable_ssl_verify: bool = False):
        self.host = host
        self.disable_ssl_verify = disable_ssl_verify        
        self.si: vim.ServiceInstance = connect.SmartConnect(host=host, user=username, pwd=password, disableSslCertValidation=disable_ssl_verify)
        self.datacenter_name: str|None = None


    def __enter__(self):
        return self

    def __exit__(self, *args):
        connect.Disconnect(self.si)

    @property
    def cookie(self):
        return self.si._stub.cookie

    @property
    def content(self):
        if not hasattr(self, "_content"):
            self._content = self.si.RetrieveContent()
        return self._content


    def wait_for_tasks(self, tasks):
        """
        Given a service instance and tasks, return after all the tasks are complete.
        """
        property_collector = self.si.content.propertyCollector
        task_list = [str(task) for task in tasks]
        # Create filter
        obj_specs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task) for task in tasks]
        property_spec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task, pathSet=[], all=True)
        filter_spec = vmodl.query.PropertyCollector.FilterSpec()
        filter_spec.objectSet = obj_specs
        filter_spec.propSet = [property_spec]
        pc_filter = property_collector.CreateFilter(filter_spec, True)
        try:
            version, state = None, None
            # Loop looking for updates till the state moves to a completed state.
            while task_list:
                update = property_collector.WaitForUpdates(version)
                for filter_set in update.filterSet:
                    for obj_set in filter_set.objectSet:
                        task = obj_set.obj
                        for change in obj_set.changeSet:
                            if change.name == 'info':
                                state = change.val.state
                            elif change.name == 'info.state':
                                state = change.val
                            else:
                                continue

                            if not str(task) in task_list:
                                continue

                            if state == vim.TaskInfo.State.success:
                                # Remove task from taskList
                                task_list.remove(str(task))
                            elif state == vim.TaskInfo.State.error:
                                raise task.info.error
                # Move to next version
                version = update.version
        finally:
            if pc_filter:
                pc_filter.Destroy()


    def enumerate_objs(self, names:list[str]|str=[], vim_types:list[type[T_Obj]]|type[T_Obj]=[]):
        if not names:
            names = []
        elif not isinstance(names, list):
            names = [names]

        if not vim_types:
            vim_types = []
        elif not isinstance(vim_types, list):
            vim_types = [vim_types]

        # Create view
        dc_view = None
        try:
            dc_view = self.content.viewManager.CreateContainerView(self.content.rootFolder, [vim.Datacenter], True)
            for dc_obj in dc_view.view:
                if self.datacenter_name:
                    if dc_obj.name != self.datacenter_name:
                        continue
                else:
                    self.datacenter_name = dc_obj.name

                view = None
                try:
                    view = self.content.viewManager.CreateContainerView(dc_obj, vim_types, True)

                    # Search for objects
                    for obj in view.view:
                        found = None
                        if names:
                            if obj.name in names:
                                found = obj
                        else:
                            found = obj
                        
                        if found:
                            yield obj
                finally:
                    if view:              
                        view.Destroy()

        finally:
            if dc_view:
                dc_view.Destroy()


    def find_obj(self, name:str, vim_type:type[T_Obj], default="__raise") -> T_Obj:
        generator = self.enumerate_objs(names=name, vim_types=vim_type)
        try:
            if default == "__raise":
                return next(generator)
            else:
                return next(generator, default)
        except StopIteration:
            raise KeyError(f"not found: {name} (vim_type: {vim_type.__name__})")


class DatastoreElementInfo(ElementInfo):    
    _datastore_folderpath_pattern = re.compile(r'^\[(?P<datastore>[^\]]+)\](?: (?P<folder>.+))?$')

    def __init__(self, datastore: vim.Datastore, folderPath: str, element, relative_to: str|Path = None):
        # Parse folderPath and element path
        if m := DatastoreElementInfo._datastore_folderpath_pattern.match(folderPath):
            folderpath_datastore = m.group('datastore')
            if folderpath_datastore != datastore.name:
                logger.warning(f"folderPath \"{folderPath}\" does not match datastore \"{datastore.name}\"")
            folder = m.group('folder') or ''
        else:
            logger.warning(f"folderPath \"{folderPath}\" does not match expected regex")
            folder = folderPath

        self.datastore_name = datastore.name
        self.path = f"{folder}{element.path}"
        
        if relative_to is not None:
            if not isinstance(relative_to, Path):
                relative_to = Path(relative_to)
            self.relative_path = Path(self.path).relative_to(relative_to)
        else:
            self.relative_path = self.path

        self.is_dir = isinstance(element, vim.host.DatastoreBrowser.FolderInfo)
        self.is_file = isinstance(element, vim.host.DatastoreBrowser.FileInfo)

        self.size = int(element.fileSize)
        self.last_modified = element.modification
        self.owner = element.owner


def datastore_exists(vc: VcenterConnection, datastore: vim.Datastore|str, path: str = None) -> str|None:
    elements = datastore_find(vc, datastore, dirpath=os.path.dirname(path), search=os.path.basename(path), case_insensitive=True)
    return f"[{elements[0].datastore_name}] {elements[0].path}" if elements else None


def datastore_find(vc: VcenterConnection, datastore: vim.Datastore|str, dirpath: str = None, search: str = None, recurse: bool = False, case_insensitive: bool = None) -> list[DatastoreElementInfo]:    
    if not isinstance(datastore, vim.Datastore):
        datastore = vc.find_obj(datastore, vim.Datastore)
        
    if dirpath:
        dirpath = dirpath.strip("/\\")
        dirfullpath = f"[{datastore.name}] {dirpath}"
    else:
        dirfullpath = f"[{datastore.name}]"

    search_specs = {}

    if case_insensitive is not None:
        search_specs["searchCaseInsensitive"] = case_insensitive

    details = vim.host.DatastoreBrowser.FileInfo.Details()
    details.fileSize = True
    details.fileOwner = True
    details.modification = True
    search_specs["details"] = details

    if search == "#folders":
        search_specs["query"] = [vim.host.DatastoreBrowser.FolderQuery()]
    elif search:
        search_specs["matchPattern"] = [search]
    
    spec = vim.host.DatastoreBrowser.SearchSpec(**search_specs)

    found: list[DatastoreElementInfo] = []

    if recurse:
        task = datastore.browser.SearchDatastoreSubFolders_Task(dirfullpath, spec)
        vc.wait_for_tasks([task])            
        for result in task.info.result:
            for element in result.file:                
                found.append(DatastoreElementInfo(datastore, result.folderPath, element, dirpath))
    else:
        task = datastore.browser.SearchDatastore_Task(dirfullpath, spec)
        vc.wait_for_tasks([task])      
        for element in task.info.result.file:
            found.append(DatastoreElementInfo(datastore, task.info.result.folderPath, element, dirpath))

    return found


def datastore_upload(vc: VcenterConnection, datastore: vim.Datastore|str, data, path):
    if isinstance(datastore, vim.Datastore):
        datastore_name = datastore.name
    elif vc.datacenter_name is None:
        datastore = vc.find_obj(datastore, vim.Datastore)
        datastore_name = datastore.name
    else:
        datastore_name = datastore

    path = path.lstrip("/")
    resource = "/folder/%s" % path
    url = f"https://{vc.host}/" + resource.lstrip("/")

    # Prepare URL parames
    url += f"?dsName={quote(datastore_name)}&dcPath={quote(vc.datacenter_name)}"

    # Prepare headers
    headers = {'Cookie': vc.cookie}
    if isinstance(data, io.BufferedReader):
        headers['Content-Type'] = 'application/octet-stream'

    # Prepare SSL context
    if vc.disable_ssl_verify:
        ssl_context = ssl.create_default_context() 
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
    else:
        ssl_context = None

    # Perform request
    req = Request(url, method='PUT', headers=headers, data=data)
    with urlopen(req, context=ssl_context) as f:
        pass
