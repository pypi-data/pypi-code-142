from __future__ import annotations

import copy
import functools
import typing as t
from collections.abc import MutableMapping
from contextlib import ExitStack
from pathlib import Path

from pyqtgraph.parametertree import InteractiveFunction, Parameter
from pyqtgraph.parametertree.interactive import Interactor
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

from qtextras import VALUE_GROUP_TYPES, fns
from qtextras._funcparse import DocstringInteractor, RunOptions
from qtextras.params.optionsdict import OptionsDict
from qtextras.typeoverloads import FilePath
from qtextras.widgets.easywidget import EasyWidget

__all__ = [
    "RunOptions",
    "ParameterEditor",
    "ParameterContainer",
]

Signal = QtCore.Signal
_ParentType = t.Union[str, t.Sequence[str], Parameter, None]


class ParameterContainer(MutableMapping):
    """
    Utility for exposing dict-like behavior to the user for inserting and querying
    parameter objects. Behaves amost like a pyqtgraph parameter, with the exception
    that new parameter "children" can be added through the dict interface
    """

    def __init__(self, parameters: dict = None, extra: dict = None, **kwargs):
        if parameters is None:
            parameters = {}
        if extra is None:
            extra = {}
        self.parameters = parameters
        self.extra = extra
        for name, value in kwargs.items():
            self[name] = value

    def __delitem__(self, key):
        if key in self.extra and key in self.parameters:
            raise KeyError(
                f"Key `{key}` is ambiguous, exists in both `extras` and `parameters`"
            )
        try:
            self.extra.__delitem__(key)
        except KeyError:
            # KeyError on non-existence will be raised in the except block
            self.parameters.__delitem__(key)

    def __iter__(self):
        for d in self.extra, self.parameters:
            yield from d

    def __len__(self):
        return self.parameters.__len__() + self.extra.__len__()

    def __setitem__(self, key, value):
        if isinstance(value, Parameter):
            self.parameters[key] = value
            self.extra.pop(key, None)
        elif key in self.parameters:
            self.parameters[key].setValue(value)
            # Assume that if the key is already in parameters, it's not in extras
            # self.extra.pop(key, None)
        else:
            self.extra[key] = value
            self.parameters.pop(key, None)

    def __getitem__(self, item):
        try:
            return self.extra[item]
        except KeyError:
            return self.parameters[item].value()

    def copy(self, deepCopyParams=True, deepCopyExtras=False, deepCopyAttrs=False):
        ret = type(self)()
        ret.__dict__.update(self.__dict__)
        # Will be filled in later
        ret.extra = {}
        ret.parameters = {}
        if deepCopyAttrs:
            ret.__dict__ = copy.deepcopy(ret.__dict__)

        if deepCopyExtras:
            ret.extra = copy.deepcopy(self.extra)
        else:
            ret.extra = self.extra.copy()
        # As of now, ret.copy()['param'] = value will still modify ret['param'] if
        # `deepCopyParams` is false. Sometimes this may be desired, but doesn't follow
        # the interface of dict.copy()['key'] = value preventing modification of the
        # original dict's key
        if deepCopyParams:
            for param, val in self.parameters.items():
                ret.parameters[param] = Parameter.create(**val.saveState())
        else:
            ret.parameters = self.parameters.copy()
        return ret

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict):
        return self.copy(deepCopyExtras=True, deepCopyAttrs=True)

    def __str__(self):
        pieces = []
        for subdict, title in zip([self.extra, self.parameters], ["Extra", "Params"]):
            if len(subdict):
                pieces.append(f"{title}: {subdict}")
            else:
                pieces.append(f"{title}: <No keys>")
        return "\n".join(pieces)

    def __repr__(self):
        return str(self)


class ParameterStateSignals(QtCore.QObject):
    # List of string names of new or removed states
    created = Signal(list)
    deleted = Signal(list)
    loadRequested = Signal(str)


class FileStateManager:
    DEFAULT_STATE_NAME = "Default"

    def __init__(
        self,
        directory: FilePath | None = None,
        suffix: str = ".param",
    ):
        self.signals = ParameterStateSignals()
        self.directory: Path | None = None
        self.suffix = suffix

        self.savedStates: list[str] = []
        """Records which states are available since the last change"""

        self.watcher = QtCore.QFileSystemWatcher()
        # False positive type hint issues, return values are allowed
        self.watcher.directoryChanged.connect(self.updateSavedStates)  # noqa
        self.watcher.fileChanged.connect(self._onWatcherFileChanged)
        self.moveDirectory(directory)

    def moveDirectory(self, newDirectory: FilePath = None):
        if newDirectory is not None:
            newDirectory = Path(newDirectory)
        self.directory = newDirectory
        if toRemove := self.watcher.directories():
            self.watcher.removePaths(toRemove)
        if newDirectory is None:
            return
        self.watcher.addPath(str(self.directory.resolve()))
        self.updateSavedStates()

    def updateSavedStates(self):
        """
        Evaluates this directory's saved states and exposes them to the application
        via signals indicating new and deleted files
        """
        dirStates = sorted(f.stem for f in self.directory.glob(f"*{self.suffix}"))

        curStatesSet = set(dirStates)
        savedStatesSet = set(self.savedStates)

        newStates = sorted(curStatesSet - savedStatesSet)
        delStates = sorted(savedStatesSet - curStatesSet)

        self.savedStates = dirStates

        # Only emit if there are states in each category
        newStates and self.signals.created.emit(newStates)
        delStates and self.signals.deleted.emit(delStates)
        return dict(created=newStates, deleted=delStates)

    def _onWatcherFileChanged(self, file: str):
        """
        Called when a watched state file is changed.
        """
        if self.formatFileName(file).exists():
            self.signals.loadRequested.emit(self.formatFileName(file).stem)

    def getDefaultStateName(self, returnStateDict=False) -> Path | tuple[Path, dict]:
        name = self.formatFileName(self.DEFAULT_STATE_NAME)
        if returnStateDict:
            return name, fns.attemptFileLoad(name, missingOk=True)
        return name

    def formatFileName(self, stateName: str | Path = None) -> Path | None:
        if stateName is None:
            return None
        stateName = (self.directory or Path()).joinpath(stateName).resolve()
        if not stateName.suffix:
            stateName = stateName.with_suffix(self.suffix)

        return stateName

    def delete(self, stateName: str):
        filename = self.formatFileName(stateName)
        if not filename.exists():
            return
        filename.unlink()
        # File watcher will take care of emitting deleted signal

    def saveState(self, stateName: str, stateDict: dict):
        if self.directory is None:
            return
        stateName = self.formatFileName(stateName)
        if not self.directory.exists() and stateName.parent == self.directory:
            raise ValueError(
                f"Attempting to save `{stateName}` when `self.directory` does not exist"
            )
        fns.saveToFile(stateDict, stateName)

    def loadState(
        self,
        stateName: str = None,
        stateDict: dict = None,
        addDefaults=False,
        watch=False,
    ):
        filename = self.formatFileName(stateName)
        if stateDict is None:
            if filename is None:
                raise ValueError("Must provide either a filename or a state dict")
            stateDict = fns.attemptFileLoad(filename)
        else:
            # If loading from a dict, we don't need to watch the file
            watch = False
        if addDefaults:
            stateDict = self.maybePopulateDefaults(stateDict)
        if watch:
            if files := self.watcher.files():
                self.watcher.removePaths(files)
            self.watcher.addPath(str(self.directory))
            self.watcher.addPath(str(filename))
        return stateDict

    def maybePopulateDefaults(self, stateDict: dict):
        """
        Add default parameters to the state dict via hierarchical updates. This
        is only performed if there is a default state ("DEFAULT_STATE_NAME" in
        ``self.directory``) that can be loaded
        """
        name, defaultState = self.getDefaultStateName(returnStateDict=True)
        if defaultState:
            stateDict = fns.hierarchicalUpdate(defaultState, stateDict)
        return stateDict

    def addSavedStatesToMenu(
        self, parentMenu: QtWidgets.QMenu, removeExistingChildren=True, keepUpdated=True
    ):
        """
        Helper function for populating menu from directory contents
        """
        # We don't want all menu children to be removed, since this would also remove
        # the 'edit' and separator options. So, do this step manually. Remove all
        # actions after the separator
        if self.directory is None:
            return
        dirGlob = fns.naturalSorted(
            f.stem for f in self.directory.glob(f"*{self.suffix}")
        )

        if removeExistingChildren:
            parentMenu.clear()

        # TODO: At the moment parameter files that start with '.' aren't getting included
        #  in the glob

        def loaderFunc(stateName):
            self.signals.loadRequested.emit(stateName)

        def populateFunc():
            self.addSavedStatesToMenu(parentMenu)

        for name in dirGlob:
            # glob returns entire filepath, so keep only filename as layout name
            curAction = parentMenu.addAction(name)
            curAction.triggered.connect(functools.partial(loaderFunc, name))

        if keepUpdated:
            self.signals.created.connect(populateFunc)
            self.signals.deleted.connect(populateFunc)


class ParameterEditor(QtWidgets.QWidget):
    sigStateCreated = Signal(str)
    sigStateChanged = Signal(object)
    # Dict of changes, or *None*
    sigStateDeleted = Signal(str)

    sigFunctionRegistered = Signal(object)

    name: str = None
    """Human readable name (i.e., used when inserting into a menu)"""

    defaultInteractor = DocstringInteractor()
    defaultParent: _ParentType = None

    def __init__(
        self, *, name: str = None, directory: FilePath = None, suffix=".param"
    ):
        """
        GUI controls for user-interactive parameters within a QtWidget (usually main
        window). Each window consists of a parameter tree and basic saving capabilities.

        Parameters
        ----------
        name
            User-readable name of the parameter editor. If *None*, :attr:`name`
            is used
        directory
            Directory to save parameter files to. If *None*, no saving is performed
        suffix
            The suffix of the saved settings. E.g. if a settings configuration is saved
            with the name "test", it will result in a file "test[suffix]"
        """
        super().__init__()
        self.stateManager = mgr = FileStateManager(directory, suffix)

        self.stateName = self.getDefaultStateName().stem

        self.name = name

        self.nameFunctionMap: dict[str, InteractiveFunction] = {}
        """Record of registered functions / processes, {function.__name__: function}"""
        self.nameParameterMap: dict[str, Parameter] = {}
        """Record of registered parameters, {parameter.name(): parameter}"""
        self.nameShortcutMap: dict[str, QtGui.QShortcut | t.Any] = {}
        """Record of InteractiveFunction shortcuts, {function.__name__: shortcut}"""

        # -----------
        # Construct parameter tree
        # -----------
        self.rootParameter = Parameter.create(name="Parameters", type="group")
        self.tree = fns.flexibleParameterTree(self.rootParameter, showTop=False)

        self._buildGui()

        # Connect last on the off chance that files are being manipulated during
        # the construction of the GUI
        mgr.signals.loadRequested.connect(self.onLoadRequested)

    @property
    def directory(self):
        return self.stateManager.directory

    @property
    def suffix(self):
        return self.stateManager.suffix

    def getDefaultStateName(self, returnStateDict=False):
        return self.stateManager.getDefaultStateName(returnStateDict)

    def formatFileName(self, stateName: str):
        return self.stateManager.formatFileName(stateName)

    def saveParameterValues(
        self,
        stateName: str = None,
        stateDict: dict = None,
        *,
        addDefaults=False,
        blockWrite=False,
        requestLoad: bool | None = None,
    ) -> t.Dict[str, t.Any]:
        """
        Saves the current parameter values to a file.

        Parameters
        ----------
        stateName
            Name of the state to save. If *None*, the current state name is used.
        stateDict
            Dictionary of parameter values to save. If *None*, the current parameter
            values are used.
        addDefaults
            If *True*, include default values in the saved state. These can either
            be the default values of parameters in the tree, or the default state
            if one exists in the directory.
        blockWrite
            If *True*, don't actually write the file. This is useful for capturing
            the saved state of a parameter editor without writing to disk.
        requestLoad
            If *True*, emit the :attr:`stateManager.signals.loadRequested` signal. If
            *None*, this is determined by whether the state name has changed. Useful
            for making sure that the state name and values are in sync when i.e. the
            user has created a new state.
        """
        if stateName is None:
            stateName = self.stateName
        if stateName is None:
            raise ValueError(
                "No state name given and no default state name set; cannot save"
            )
        if stateDict is None:
            stateDict = self.getParameterValues()
        if addDefaults:
            _, defaults = self.stateManager.getDefaultStateName(returnStateDict=True)
            if defaults is None:
                defaults = self.getParameterDefaults()
            stateDict = fns.hierarchicalUpdate(defaults, stateDict)
        if not blockWrite:
            # Don't trigger infinite "load" loops through file watcher signal
            # if saving self's current state
            self._saveAndMaybeBlockUpdate(stateName, stateDict)
        if requestLoad is None:
            fmt = self.formatFileName
            requestLoad = fmt(stateName) != fmt(self.stateName)
        if requestLoad and not blockWrite:
            self.stateManager.signals.loadRequested.emit(stateName)
        return stateDict

    def getParameterDefaults(self):
        return fns.parameterValues(self.rootParameter, value="default")

    def getParameterValues(self):
        return fns.parameterValues(
            self.rootParameter, valueFilter=fns.valueIsNotDefault
        )

    def _saveAndMaybeBlockUpdate(self, stateName: str, stateDict: dict):
        """
        Save state and block updates to prevent infinite loop when saving self's
        current state
        """
        mgr = self.stateManager
        fmt = mgr.formatFileName
        with ExitStack() as stack:
            if fmt(stateName) == fmt(self.stateName):
                stack.enter_context(fns.makeDummySignal(mgr.signals, "loadRequested"))
            mgr.saveState(stateName, stateDict)

    def saveParameterValuesGui(self):
        saveName = fns.dialogGetSaveFileName(self, "Save As", self.stateName)
        if saveName == (default := self.getDefaultStateName().stem):
            QtWidgets.QMessageBox.information(
                self,
                "Save As",
                f"`{default}` is automatically generated and will overwrite changes "
                f"on next startup. Please choose a different name.",
            )
            return self.saveParameterValuesGui()
        if saveName:
            return self.saveParameterValues(saveName)

    def _parseAndUpdateCandidateParameters(
        self, loadDict: dict, candidateParameters: t.Sequence[Parameter] = None
    ):
        if candidateParameters is None:
            candidateParameters = fns.flattenedParameters(
                self.rootParameter, groupTypes=VALUE_GROUP_TYPES
            )
        if not candidateParameters:
            return

        def validName(param, name):
            return name in (param.opts["title"], param.name())

        def checkParentChain(param, name):
            if not param:
                return False
            return validName(param, name) or checkParentChain(param.parent(), name)

        unhandled = {}
        # Copy for mutable object
        for kk, vv in loadDict.items():
            if isinstance(vv, dict):
                # Successively traverse down child tree
                curCandidates = [
                    p for p in candidateParameters if checkParentChain(p, kk)
                ]
                # By this point defaults are already populated so no need to reset them
                # otherwise infinite recursion will occur
                self._parseAndUpdateCandidateParameters(
                    vv, candidateParameters=curCandidates
                )
            else:
                unhandled[kk] = vv
        with self.rootParameter.treeChangeBlocker():
            for kk, vv in unhandled.items():
                matches = [p for p in candidateParameters if validName(p, kk)]
                if len(matches) == 1:
                    matches[0].setValue(vv)
                # elif len(matches) == 0:
                #   warnings.warn(
                #       f'No matching parameters for key {kk}. Ignoring.', UserWarning
                #   )
                elif len(matches) > 0:
                    raise ValueError(
                        f"Multiple matching parameters for key {kk}:\n" f"{matches}"
                    )

    def loadParameterValues(
        self,
        stateName: str | Path = None,
        stateDict: dict = None,
        addDefaults=False,
        candidateParameters: t.List[Parameter] = None,
    ) -> dict[str, t.Any]:
        """
        Can restore a state created by ``fns.parameterValues``

        Parameters
        ----------
        stateName
            Name of the state to load
        stateDict
            If given, this dictionary will be used instead of loading from the state
            manager
        addDefaults
            If *True*, the default values of the parameters will be used if the
            parameter is not found in the state dictionary. If a state with name
            ``self.DEFAULT_STATE_NAME`` is present in ``self.directory``, this will
            be used as the default state. Otherwise, the default values of the
            parameters will be used.
        candidateParameters
            If given, only these parameters will be considered for loading. This is
            useful if you want to load a subset of parameters from a state.

        Returns
        -------
        Loaded state dictionary. If ``stateDict`` was given, this will be the same
        object unless ``addDefaults`` is *True*.
        """
        if candidateParameters is not None and not len(candidateParameters):
            # Nothing to update, no reason to load state dict
            self.stateName = self.stateManager.formatFileName(stateName).stem
            return self.getParameterValues()

        stateDict = self.stateManager.loadState(
            stateName, stateDict, addDefaults, watch=True
        )
        if addDefaults and not self.stateManager.getDefaultStateName().exists():
            # Defaults need to be added
            stateDict = fns.hierarchicalUpdate(self.getParameterDefaults(), stateDict)

        self._parseAndUpdateCandidateParameters(stateDict, candidateParameters)
        self.stateName = self.stateManager.formatFileName(stateName).stem

        return self.getParameterValues()

    def onLoadRequested(self, stateName):
        # First check for extra keys, will be the case if 'children' is one of the
        # keys. Can't do value-loading in that case, must do state-loading instead
        stateDict = self.stateManager.loadState(stateName)
        if not stateDict:
            # File didn't exist or there was a problem during loading
            return
        if "children" in stateDict:
            # Bug in pyqtgraph restore state doesn't play nice when parameters have
            # connected functions outside the parameter item, so re-implement without
            # inserting or removing children
            with self.rootParameter.treeChangeBlocker():
                fns.applyParameterOpts(self.rootParameter, stateDict)
        else:
            self.loadParameterValues(stateName, stateDict)

    def _resolveParameterParent(self, parent: _ParentType = None) -> Parameter:
        parent = parent or self.defaultParent
        if parent is None:
            parent = self.rootParameter
        if isinstance(parent, Parameter):
            return parent
        if isinstance(parent, str):
            parent = [parent]
        return fns.getParameterChild(self.rootParameter, *parent)

    def registerParameterList(
        self, parameters: t.Sequence[OptionsDict | Parameter], *args, **kwargs
    ) -> list[Parameter]:
        """
        Registers a list of properties and returns an array of each. For parameter
        descriptions, see :meth:`regiseterParameter`.
        """
        outProps = []
        with self.rootParameter.treeChangeBlocker():
            for param in parameters:
                outProps.append(self.registerParameter(param, *args, **kwargs))
        return outProps

    def registerParameter(
        self,
        parameter: OptionsDict | Parameter,
        *,
        parent: _ParentType = None,
        container: ParameterContainer = None,
        **extraOpts,
    ) -> Parameter:
        """
        Registers a property defined by ``constParam`` that will appear in the
        respective parameter editor.

        Parameters
        ----------
        parameter
            The parameter to register. Can either be an instantiated Parmeter
            or ``OptionsDict`` specification.
        parent
            See ``parent`` documentation in :meth:`ParameterEditor.registerFunction`
        container
            Optional container in which to insert this parameter
        **extraOpts
            Extra options passed directly to the created Parameter

        Returns
        -------
        Property bound to this value in the parameter editor
        """
        if isinstance(parameter, Parameter):
            paramOpts = parameter.opts
        else:
            paramOpts = dict(parameter)
        paramOpts.update(extraOpts)

        parent = self._resolveParameterParent(parent)
        paramForEditor = fns.getParameterChild(parent, childOpts=paramOpts)

        if container is not None:
            container[parameter] = paramForEditor
        return paramForEditor

    def registerFunction(
        self,
        function: t.Callable,
        *,
        name: str = None,
        interactor: Interactor = None,
        parent: _ParentType = None,
        runActionTemplate: dict = None,
        parametersNeedRunKwargs: bool | None = True,
        container: ParameterContainer = None,
        **kwargs,
    ) -> InteractiveFunction:
        """
        Like :meth:`registerParameter` but for functions instead along with interactive
        parameters for each argument. A button is added for the user to force run this
        function as well. In the case of a function with no parameters, the button will
        be named the same as the function itself for simplicity.

        Parameters
        ----------
        function
            Function to make interactive
        name:
            Name of the function. If None, defaults to the ``function.__name__``
        interactor
            The interactor to use for creating Parameters out of each argument. If None,
            defaults to :attr:`self.defaultInteractor`.
        parent
            Top :class:`Parameter` for registration. If a string or tuple is provided,
            it will be converted to a Parameter using ``fns.getParameterChild`` and
            inserted as a descendant of :attr:`self.rootParameter`. If None, defaults
            to :attr:`self.rootParameter`.
        runActionTemplate
            Template for the run action. See ``Interactor.runActionTemplate`` for
            more details.
        parametersNeedRunKwargs
            Passed to ``InteractiveFunction.parametersNeedRunKwargs``. If ``None``,
            the function's original attribute value is unchanged.
        container
            The container in which to put child parameters from the registered function.
            This has a similar effect to calling `registerProps` on each of the
            function arguments with this container. *Note*: while the former will
            register props according to the `parameter` OptionsDict, this will register
            to the container using the raw parameter name. A KeyError is raised when
            a new parameter name clashes with something already in the container.
        **kwargs
            All additional kwargs are passed to InteractiveFunction when wrapping the
            function. If an InteractiveFunction is passed in, ``kwargs`` are passed to
            the interactor.
        """
        if interactor is None:
            interactor = self.defaultInteractor
        rawFuncGiven = not isinstance(function, InteractiveFunction)
        if rawFuncGiven:
            function = InteractiveFunction(function)
        runActionTemplate = dict(runActionTemplate) if runActionTemplate else {}

        if rawFuncGiven and name is None and "name" in runActionTemplate:
            name = runActionTemplate.get("name")
            defaultName = self.defaultInteractor.runActionTemplate["defaultName"]
            runActionTemplate["name"] = defaultName
        elif not rawFuncGiven is not None and rawFuncGiven:
            raise ValueError(
                "Cannot specify `name` override when passing an already-interactive "
                "function"
            )

        parent = self._resolveParameterParent(parent)

        if name is not None:
            function.__name__ = name
        if parametersNeedRunKwargs is not None:
            function.parametersNeedRunKwargs = parametersNeedRunKwargs
        if runActionTemplate.get("shortcut"):
            self.registerFunctionShortcut(function, **runActionTemplate)
            del runActionTemplate["shortcut"]
        self.nameFunctionMap[function.__name__] = function
        if runActionTemplate:
            kwargs["runActionTemplate"] = runActionTemplate

        fns.interactAndHandleExistingParameters(
            interactor, function, parent=parent, **kwargs
        )

        if container is None:
            self.sigFunctionRegistered.emit(function)
            return function

        funcKwargs = {**function.extra, **function.parameters}
        if alreadyExists := set(container) & set(funcKwargs):
            raise KeyError(f"{alreadyExists} already exist in {container}")

        for name, value in funcKwargs.items():
            container[name] = value
        self.sigFunctionRegistered.emit(function)
        return function

    def registerFunctionShortcut(
        self,
        function: t.Callable,
        shortcut: str,
        ownerWidget: QtWidgets.QWidget = None,
        force=False,
        **opts,
    ):
        name = function.__name__
        if name in self.nameShortcutMap and not force:
            raise KeyError(
                f"{name} already present in shortcut map: {self.nameShortcutMap[name]=}"
            )
        if ownerWidget is None:
            defaultContext = QtCore.Qt.ShortcutContext.ApplicationShortcut
            ownerWidget = self
        else:
            defaultContext = QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut
        context = opts.get("context", defaultContext)
        qShortcut = QtGui.QShortcut(shortcut, ownerWidget, context=context)
        qShortcut.activated.connect(function)
        self.nameShortcutMap[name] = qShortcut
        return qShortcut

    def registerObjectShortcut(
        self, shortcuttable: t.Any, shortcut: str, name: str, force=False, **opts
    ):
        """
        Objects like ``QAction`` and ``QPushButton`` can be given shortcuts, but don't
        give access to a ``QShortcut`` that is directly manipulatable. Instead,
        their shortcut is given and accessed via its key sequence. Play nicely with
        these objects, but otherwise behave similarly to
        :meth:`ParameterEditor.registerFunctionShortcut`
        """
        if name in self.nameShortcutMap and not force:
            raise KeyError(
                f"{name} already present in shortcut map: {self.nameShortcutMap[name]=}"
            )
        if not hasattr(shortcuttable, "setShortcut"):
            raise ValueError(f"{shortcuttable} must have `setShortcut()` method")
        shortcuttable.setShortcut(shortcut)
        self.nameShortcutMap[name] = shortcuttable

    def createWindowDock(
        self,
        window: QtWidgets.QMainWindow,
        title: str = None,
        dockArea=QtCore.Qt.DockWidgetArea.RightDockWidgetArea,
        createProcessMenu=True,
        addShowAction=True,
        menu: QtWidgets.QMenu = None,
    ) -> tuple[QtWidgets.QDockWidget, QtWidgets.QMenu | None]:
        """
        Creates a dock widget for this parameter editor and adds it to the given
        window. If no window is provided, a new one is created

        Parameters
        ----------
        window
            Window to add the dock to
        title
            Title for the dock widget and created menu
        dockArea
            Area of the window to dock to
        createProcessMenu
            Whether to create a menu for running registered editor functions.
            If ``True``, a menu is created with the name ``title`` and added
            to the window's menu bar.
            .. note::
                This will change the return value to a tuple of the dock and the menu.
        addShowAction
            Whether to add an action to the created process menu which
            toggles display of the dock widget. Note that if ``createProcessesMenu``
            is ``False``, this is ignored

        Returns
        -------
        dock or tuple of (dock, menu)
            Either the dock widget or both the dock and created menu, the latter when
            ``createProcessesMenu`` is ``True``
        """
        title = title or self.name.title()
        dock = QtWidgets.QDockWidget(title)
        dock.setObjectName(title)
        dock.setWidget(self)
        dock.hide()

        curAreaWidgets = [
            d
            for d in window.findChildren(QtWidgets.QDockWidget)
            if window.dockWidgetArea(d) == dockArea
        ]
        window.addDockWidget(dockArea, dock)
        if len(curAreaWidgets):
            window.tabifyDockWidget(curAreaWidgets[-1], dock)
            window.setTabPosition(dockArea, QtWidgets.QTabWidget.TabPosition.North)

        if not createProcessMenu and not addShowAction:
            return dock, None

        def onShow():
            dock.show()
            dock.raise_()

        if menu is None:
            menu = QtWidgets.QMenu(title)

        if addShowAction:
            menu.addAction(f"{self.name}...", onShow)
        if createProcessMenu:
            self.createActionsFromFunctions(menu)
        return dock, menu

    def createActionsFromFunctions(
        self,
        menu: QtWidgets.QMenu = None,
        stealShortcuts=True,
        keepUpdated=True,
    ) -> QtWidgets.QMenu:
        if menu is None:
            menu = QtWidgets.QMenu(fns.nameFormatter(self.name))

        def addProcess(process):
            name = process.__name__
            if name not in self.rootParameter.names:
                raise ValueError(
                    "Creating a process menu from children outside `self.rootParameter` "
                    "is currently not supported."
                )
            parameter = self.rootParameter.child(name)
            # Don't interact with functions unless they specify RunOptions.ON_ACTION
            if not parameter.opts.get("button", {}).get("visible", True):
                return
            actTitle = self.defaultInteractor.titleFormat(process.__name__)
            act = menu.addAction(actTitle, process.__call__)
            if stealShortcuts and (
                shortcut := self.nameShortcutMap.get(process.__name__)
            ):
                self.registerObjectShortcut(
                    act, shortcut.key(), process.__name__, force=True
                )

        for proc in self.nameFunctionMap.values():
            addProcess(proc)
        if keepUpdated:
            self.sigFunctionRegistered.connect(addProcess)
        return menu

    # Allow customization through kwargs in subclasses
    # noinspection PyUnusedLocal
    def _buildGui(self, **kwargs):
        self.setWindowTitle(self.name)
        self.setObjectName(self.name)

        # -----------
        # Additional widget buttons
        # -----------
        self.expandAllButton = QtWidgets.QPushButton("Expand All")
        self.collapseAllButton = QtWidgets.QPushButton("Collapse All")
        self.saveAsButton = QtWidgets.QPushButton("Save As...")
        pol = QtWidgets.QSizePolicy.Policy
        self.saveAsButton.setSizePolicy(pol.MinimumExpanding, pol.Fixed)
        self._createLoadButton()

        # -----------
        # Widget layout
        # -----------
        # Optional buttons that can be specified in subclasses under `_guiChildren()`
        # if they should appear
        self.treeButtonsWidget = EasyWidget(
            [self.expandAllButton, self.collapseAllButton]
        )
        self.treeButtonsWidget.widget_.hide()
        children = self._guiChildren()

        EasyWidget.buildWidget(children, baseWidget=self)

        if self.stateManager.directory is None:
            self.saveAsButton.hide()
            self.loadButton.hide()

        self.tree.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        # -----------
        # UI Element Signals
        # -----------
        self.expandAllButton.clicked.connect(
            lambda: fns.setParametersExpanded(self.tree)
        )
        self.collapseAllButton.clicked.connect(
            lambda: fns.setParametersExpanded(self.tree, False)
        )
        self.saveAsButton.clicked.connect(self.saveParameterValuesGui)

    def _guiChildren(self) -> list:
        """
        Specifies which children should be added to this GUI. The return value
        is directly passed to :func:`EasyWidget.buildWidget`
        """
        return [
            self.treeButtonsWidget,
            self.tree,
            [self.saveAsButton, self.loadButton],
        ]

    def _createLoadButton(self):
        self.loadButton = QtWidgets.QToolButton()
        self.loadButton.setText("Load...")
        pol = QtWidgets.QSizePolicy.Policy
        self.loadButton.setSizePolicy(pol.MinimumExpanding, pol.Fixed)
        self.loadButton.setMenu(QtWidgets.QMenu(self.loadButton))
        self.loadButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.stateManager.addSavedStatesToMenu(self.loadButton.menu())
        return self.loadButton

    def __repr__(self):
        selfCls = type(self)
        oldName: str = super().__repr__()
        # Remove module name for brevity
        oldName = oldName.replace(
            f"{selfCls.__module__}.{selfCls.__name__}",
            f"{selfCls.__name__} '{self.name}'",
        )
        return oldName
