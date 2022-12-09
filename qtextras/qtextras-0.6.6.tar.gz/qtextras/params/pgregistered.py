from __future__ import annotations

import typing as t

from pkg_resources import parse_version
from pyqtgraph.parametertree import (
    InteractiveFunction,
    Interactor,
    Parameter,
    interact,
    parameterTypes as ptypes,
)
from pyqtgraph.parametertree.Parameter import PARAM_TYPES
from pyqtgraph.parametertree.parameterTypes import ActionGroupParameterItem
from pyqtgraph.Qt import QtCore, QtGui, QtVersion, QtWidgets

from qtextras import fns
from qtextras.shims import ActionGroupParameter
from qtextras.widgets.lineeditor import PopupLineEditor

__all__ = [
    "KeySequenceParameterItem",
    "ParameterDialog",
    "PgParameterDelegate",
    "PgPopupDelegate",
    "PopupLineEditorParameterItem",
    "PopupLineEditorParameter",
    "ChainedActionGroupParameterItem",
    "ChainedActionGroupParameter",
]


class MonkeyPatchedTextParameterItem(ptypes.TextParameterItem):
    def makeWidget(self):
        textBox: QtWidgets.QTextEdit = super().makeWidget()
        textBox.setTabChangesFocus(True)
        return textBox


# Monkey patch pyqtgraph text box to allow tab changing focus
ptypes.TextParameter.itemClass = MonkeyPatchedTextParameterItem


class ParameterDialog(QtWidgets.QDialog):
    def __init__(self, param: Parameter, parent=None):
        super().__init__(parent)
        self.setModal(True)
        self.param = param
        self.tree = fns.flexibleParameterTree(param)
        self.saveChanges = False

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.tree)

        okBtn = QtWidgets.QPushButton("Ok")
        cancelBtn = QtWidgets.QPushButton("Cancel")
        btnLay = QtWidgets.QHBoxLayout()
        btnLay.addWidget(okBtn)
        btnLay.addWidget(cancelBtn)
        layout.addLayout(btnLay)

        def okClicked():
            self.saveChanges = True
            self.accept()

        def cancelClicked():
            self.saveChanges = False
            self.reject()

        okBtn.clicked.connect(okClicked)
        cancelBtn.clicked.connect(cancelClicked)


class PgPopupDelegate(QtWidgets.QStyledItemDelegate):
    """
    For pyqtgraph-registered parameter types that don't define an itemClass with
    `makeWidget`, this popup delegate can be used instead which creates a popout
    parameter tree.
    """

    def __init__(self, paramDict: dict, parent=None):
        super().__init__(parent)
        paramDict.setdefault("name", paramDict["type"])
        self.param = Parameter.create(**paramDict)

    def createEditor(self, parent, option, index: QtCore.QModelIndex):
        self.param.setValue(index.data(QtCore.Qt.ItemDataRole.EditRole))
        editor = ParameterDialog(self.param)
        editor.show()
        editor.resize(editor.width() + 50, editor.height() + 30)

        return editor

    def setModelData(
        self,
        editor: QtWidgets.QWidget,
        model: QtCore.QAbstractTableModel,
        index: QtCore.QModelIndex,
    ):
        if editor.saveChanges:
            model.setData(index, editor.param.value())

    def setEditorData(self, editor: QtWidgets.QWidget, index):
        value = index.data(QtCore.Qt.ItemDataRole.EditRole)
        self.param.setValue(value)

    def updateEditorGeometry(
        self,
        editor: QtWidgets.QWidget,
        option: QtWidgets.QStyleOptionViewItem,
        index: QtCore.QModelIndex,
    ):
        return


class PgParameterDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parameterDict: dict, parent=None):
        super().__init__(parent)
        errMsg = (
            f"`{self.__class__}` can only create parameter editors from registered"
            f" pyqtgraph widgets whose items subclass `WidgetParameterItem` and are in"
            f" pyqtgraph's `PARAM_TYPES`.\n"
            f"These requirements are not met for type `{parameterDict['type']}`"
        )

        if parameterDict["type"] not in PARAM_TYPES:
            raise TypeError(errMsg)
        parameterDict.update(name="dummy")
        self.param = param = Parameter.create(**parameterDict)
        item = param.makeTreeItem(0)
        if isinstance(item, ptypes.WidgetParameterItem):
            self.item = item
        else:
            raise TypeError(errMsg)

    def createEditor(self, parent, option, index: QtCore.QModelIndex):
        # TODO: Deal with params that go out of scope before yielding a value
        editor = self.item.makeWidget()
        editor.setParent(parent)
        editor.setMaximumSize(option.rect.width(), option.rect.height())
        return editor

    def setModelData(
        self,
        editor: QtWidgets.QWidget,
        model: QtCore.QAbstractTableModel,
        index: QtCore.QModelIndex,
    ):
        model.setData(index, editor.value())

    def setEditorData(self, editor: QtWidgets.QWidget, index):
        value = index.data(QtCore.Qt.ItemDataRole.EditRole)
        editor.setValue(value)

    def updateEditorGeometry(
        self,
        editor: QtWidgets.QWidget,
        option: QtWidgets.QStyleOptionViewItem,
        index: QtCore.QModelIndex,
    ):
        editor.setGeometry(option.rect)


class KeySequenceParameterItem(ptypes.WidgetParameterItem):
    """
    Class for creating custom shortcuts. Must be made here since pyqtgraph doesn't
    provide an implementation.
    """

    def makeWidget(self):
        item = QtWidgets.QKeySequenceEdit()

        item.sigChanged = item.editingFinished
        item.value = lambda: item.keySequence().toString()

        def setter(val: QtGui.QKeySequence):
            if val is None or len(val) == 0:
                item.clear()
            else:
                item.setKeySequence(val)

        item.setValue = setter
        self.param.seqEdit = item

        return item

    def updateDisplayLabel(self, value=None):
        # Make sure the key sequence is human-readable
        self.displayLabel.setText(self.widget.keySequence().toString())


class PopupLineEditorParameterItem(ptypes.WidgetParameterItem):
    def __init__(self, param, depth):
        strings = param.opts.get("limits", [])
        self.model = QtCore.QStringListModel(strings)
        param.sigLimitsChanged.connect(
            lambda _param, limits: self.model.setStringList(limits)
        )
        super().__init__(param, depth)

    def makeWidget(self):
        opts = self.param.opts
        editor = PopupLineEditor(
            model=self.model,
            clearOnComplete=False,
            forceMatch=opts.get("forceMatch", True),
            validateCase=opts.get("validateCase", False),
        )
        editor.setValue = editor.setText
        editor.value = editor.text
        editor.sigChanged = editor.editingFinished
        return editor

    def widgetEventFilter(self, obj, ev):
        # Prevent tab from leaving widget
        return False


class PopupLineEditorParameter(Parameter):
    itemClass = PopupLineEditorParameterItem

    def __init__(self, **opts):
        if "value" in opts:
            limits = opts.get("limits", [])
            if opts["value"] not in limits:
                limits.insert(0, opts["value"])
            opts["limits"] = limits
        super().__init__(**opts)


class DisplayValueParameterItem(ptypes.StrParameterItem):
    def makeWidget(self):
        widget = super().makeWidget()
        widget.setValue = lambda val: widget.setText(str(val))
        widget.value = self.param.value
        return widget

    def __init__(self, param, depth):
        super().__init__(param, depth)
        self.widget.setReadOnly(True)
        if param.value() is None:
            # Force set initial value if "None" otherwise it won't get set
            # Because pg.eq() will say value never needed to be initially set
            self.widget.setText("None")
            self.updateDisplayLabel()


class DisplayValueParameter(ptypes.SimpleParameter):
    itemClass = DisplayValueParameterItem

    def __init__(self, **opts):
        opts.update(enabled=False)
        super().__init__(**opts)

    def _interpretValue(self, v):
        return v


class ChainedActionGroupParameterItem(ActionGroupParameterItem):
    def __init__(self, param, depth):
        self.enabledFontMap = None
        super().__init__(param, depth)
        if param.opts["enabled"]:
            # Starts out unchecked, adjust at the start
            self.setCheckState(0, QtCore.Qt.CheckState.Checked)

    def _mkFontMap(self):
        if self.enabledFontMap:
            return
        enabledFont = self.font(0)
        disableFont = QtGui.QFont()
        disableFont.setStrikeOut(True)
        self.enabledFontMap = {True: enabledFont, False: disableFont}

    def optsChanged(self, param, opts):
        super().optsChanged(param, opts)
        if "enabled" in opts:
            enabled = opts["enabled"]
            cs = QtCore.Qt.CheckState
            role = cs.Checked if enabled else cs.Unchecked
            # Bypass subclass to prevent early short-circuit
            self.setCheckState(0, role)
            # This gets called before constructor can finish, so add enabled font map here
            self._mkFontMap()
            self.setFont(0, self.enabledFontMap[enabled])

    def updateFlags(self):
        # It's a shame super() doesn't return flags...
        super().updateFlags()
        flags = self.flags()
        flags |= QtCore.Qt.ItemFlag.ItemIsUserCheckable & (
            ~QtCore.Qt.ItemFlag.ItemIsAutoTristate
        )
        self.setFlags(flags)

    def setData(self, column, role, value):
        castedRole = QtCore.Qt.ItemDataRole(role)
        if parse_version(QtVersion) >= parse_version("6.0"):
            # 'int' no longer implicitly cast. However, casting role on earlier
            # versions results in an error.
            role = castedRole
        if castedRole != QtCore.Qt.ItemDataRole.CheckStateRole:
            return super().setData(column, role, value)
        cs = QtCore.Qt.CheckState
        newEnabled = cs(value) == cs.Checked
        if newEnabled == self.param.opts["enabled"]:
            # Ensure no mismatch between param enabled and item checkstate
            super().setData(column, role, value)
        else:
            # `optsChanged` above will handle check state
            self.param.setOpts(enabled=newEnabled)


class ChainedActionGroupParameter(ActionGroupParameter):
    itemClass = ChainedActionGroupParameterItem

    def __init__(self, **opts):
        opts.setdefault("type", "chainedactiongroup")
        super().__init__(**opts)
        self.sigOptionsChanged.connect(self.optsChanged)

    def addStage(
        self,
        stage: InteractiveFunction | t.Callable,
        *,
        interactor: Interactor = None,
        stageInputOptions: dict = None,
        **metaOptions,
    ):
        if isinstance(stage, ChainedActionGroupParameter):
            # Child pipelines should only be activatable by the parents
            stage.setButtonOpts(visible=False)
            return self.addChild(stage)
        elif callable(stage) and not isinstance(stage, InteractiveFunction):
            stage = InteractiveFunction(stage)
        elif not isinstance(stage, InteractiveFunction):
            raise TypeError("Stage must be callable")

        stage: InteractiveFunction
        if interactor is None:
            interactor = interact

        # The new item class should be a ChainedActionGroupParameterItem to allow checkable
        # stages. Normally, this can be set after registering, but if the parent
        # parameter is already part of a ParameterTree, an item will immediately
        # be created. So, we need to dynamically adjust the itemClass during
        # registration, then set it after to also impact delayed child creation.
        with fns.overrideAttr(
            ActionGroupParameter, "itemClass", ChainedActionGroupParameterItem
        ):
            # Treat stage input options that collide with already-registered parameters
            # as value options
            registered = fns.interactAndHandleExistingParameters(  # noqa
                interactor,
                stage,
                allowSetValue=True,
                parent=self,
                runOptions=[],
                **(stageInputOptions or {}),
            )
        # As described above, also change `itemClass` here
        registered.itemClass = ChainedActionGroupParameterItem
        registered.setOpts(function=stage, **metaOptions)
        return registered

    def activate(self, **kwargs):
        if not self.opts["enabled"]:
            return kwargs
        super().activate()
        for child in self.children():  # type: ActionGroupParameter
            if isinstance(child, ChainedActionGroupParameter):
                kwargs.update(child.activate(**kwargs))
            if not child.opts["enabled"] or not (
                function := child.opts.get("function")
            ):
                continue
            useKwargs = {
                k: v
                for k, v in kwargs.items()
                if k in set(function.parameters).union(function.extra)
            }
            output = function(**useKwargs)
            if isinstance(output, dict):
                kwargs.update(output)
        return kwargs

    def optsChanged(self, _param, opts):
        if "enabled" not in opts:
            return
        enabled = opts["enabled"]
        for child in self:
            if isinstance(child, ChainedActionGroupParameter) or child.opts.get(
                "function"
            ):
                child.setOpts(enabled=enabled)

    def showButton(self, **buttonOpts):
        buttonOpts["visible"] = True
        self.setButtonOpts(**buttonOpts)


ptypes.registerParameterType("display", DisplayValueParameter, override=True)
ptypes.registerParameterItemType("keysequence", KeySequenceParameterItem, override=True)
ptypes.registerParameterType("popuplineeditor", PopupLineEditorParameter, override=True)
ptypes.registerParameterType(
    "chainedactiongroup", ChainedActionGroupParameter, override=True
)
