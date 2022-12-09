from __future__ import annotations

import inspect
import typing as t

from pyqtgraph import QtGui, QtWidgets
from pyqtgraph.parametertree import Parameter

from qtextras.fns import flattenedParameters, forceRichText
from qtextras.params import OptionsDict

ButtonCallable = t.Union[t.Callable[[OptionsDict], t.Any], t.Callable[[], t.Any]]


class ButtonCollection(QtWidgets.QGroupBox):
    def __init__(
        self,
        parent=None,
        title: str = None,
        buttonParameters: t.Collection[OptionsDict] = (),
        triggerFunctions: t.Union[ButtonCallable, t.Collection[ButtonCallable]] = (),
        exclusive=True,
        asToolButton=True,
        **createOpts,
    ):
        super().__init__(parent)
        self.lastTriggered: t.Optional[OptionsDict] = None
        self.uiLayout = QtWidgets.QHBoxLayout(self)
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.optionsFunctionMap: t.Dict[OptionsDict, ButtonCallable] = dict()
        self.optionsButtonMap: t.Dict[OptionsDict, QtWidgets.QPushButton] = dict()
        self.asToolButton = asToolButton
        if title is not None:
            self.setTitle(title)
        self.buttonGroup.setExclusive(exclusive)

        if not isinstance(triggerFunctions, t.Iterable):
            triggerFunctions = [triggerFunctions] * len(buttonParameters)
        for param, fn in zip(buttonParameters, triggerFunctions):
            self.createAndAddButton(param, fn, **createOpts)

    def createAndAddButton(
        self,
        buttonOptions: OptionsDict,
        triggerFunction: ButtonCallable,
        checkable=False,
        **createOpts,
    ) -> QtWidgets.QAbstractButton | None:
        if buttonOptions in self.optionsButtonMap:
            # Either already exists or wasn't designed to be a button
            return None

        if self.asToolButton:
            createOpts.setdefault("buttonType", QtWidgets.QToolButton)
        newBtn = self.createButton(buttonOptions, **createOpts)
        if checkable:
            newBtn.setCheckable(True)
            oldTriggerFn = triggerFunction
            numArgs = self._getTriggerArgumentCount(triggerFunction)

            def newTriggerFn(param: OptionsDict):
                """
                If the button is checkable, only call this function when the button
                is checked
                """
                if newBtn.isChecked():
                    return oldTriggerFn(param) if numArgs else oldTriggerFn()

            triggerFunction = newTriggerFn
        newBtn.clicked.connect(lambda: self.callAssociatedFunction(buttonOptions))

        self.addButton(buttonOptions, newBtn, triggerFunction)
        return newBtn

    def clear(self):
        for button in self.optionsButtonMap.values():
            self.buttonGroup.removeButton(button)
            self.uiLayout.removeWidget(button)
            button.deleteLater()

        self.optionsButtonMap.clear()
        self.optionsFunctionMap.clear()

    def addFromExisting(
        self, other: ButtonCollection, which: t.Collection[OptionsDict] = None
    ):
        for (param, btn), func in zip(
            other.optionsButtonMap.items(), other.optionsFunctionMap.values()
        ):
            if which is None or param in which:
                self.addButton(param, btn, func)

    def addButton(
        self,
        option: OptionsDict,
        button: QtWidgets.QPushButton,
        function: ButtonCallable,
    ):
        self.buttonGroup.addButton(button)
        self.uiLayout.addWidget(button)
        self.optionsFunctionMap[option] = function
        self.optionsButtonMap[option] = button

    @classmethod
    def createButton(
        cls,
        buttonOptions: OptionsDict,
        baseButton: QtWidgets.QAbstractButton = None,
        buttonType=QtWidgets.QPushButton,
        parent=None,
    ):
        tooltipText = buttonOptions.tip
        title = buttonOptions.get("title", buttonOptions.name)
        if baseButton is not None:
            newBtn = baseButton
        else:
            newBtn = buttonType(parent)
            newBtn.setText(title)
        icon = (
            buttonOptions.opts["button"].get("icon")
            if "group" in buttonOptions.type
            else buttonOptions.get("icon")
        )
        if icon:
            newBtn.setText("")
            newBtn.setIcon(QtGui.QIcon(str(icon)))
            tooltipText = buttonOptions.addHelpText(title)
        if tooltipText:
            tooltipText = forceRichText(tooltipText)
            newBtn.setToolTip(tooltipText)
        return newBtn

    def callAssociatedFunction(self, options: OptionsDict):
        if options is None:
            return
        # Ensure function is called in the event it requires a button to be checked
        btn = self.optionsButtonMap[options]
        if btn.isCheckable():
            btn.setChecked(True)
        function = self.optionsFunctionMap[options]
        argCount = self._getTriggerArgumentCount(function)
        ret = function(options) if argCount else function()
        self.lastTriggered = options
        return ret

    def addByParameter(self, parameter: Parameter, **registerOpts):
        """
        Adds a button to a group based on the parameter. Also works for group params
        that have an action nested.
        """
        for parameter in filter(
            lambda p: "action" in p.type(), flattenedParameters(parameter)
        ):
            self.createAndAddButton(
                OptionsDict(**parameter.opts), parameter.activate, **registerOpts
            )

    @classmethod
    def fromToolsEditors(
        cls,
        editors: t.Sequence[t.Any],
        title="Tools",
        ownerCollection: ButtonCollection = None,
        **registerOpts,
    ):
        if ownerCollection is None:
            ownerCollection = cls(title=title, exclusive=True)

        for editor in editors:
            ownerCollection.addByParameter(editor.rootParameter, **registerOpts)

        return ownerCollection

    def toolbarFormat(self):
        """
        Returns a list of buttons + title in a format that's easier to add to a
        toolbar, e.g. doesn't require as much horizontal space
        """
        title = self.title()
        out: t.List[QtWidgets.QWidget] = (
            [] if title is None else [QtWidgets.QLabel(self.title())]
        )
        for btn in self.optionsButtonMap.values():
            out.append(btn)
        return out

    def _getTriggerArgumentCount(self, triggerFunction: t.Callable):
        signature = inspect.signature(triggerFunction)
        numArgs = None
        for bindAttempt in [], [OptionsDict("dummy")]:
            try:
                signature.bind(*bindAttempt)
                numArgs = len(bindAttempt)
            except TypeError:
                pass
        if numArgs is None:
            raise ValueError(
                f"`{triggerFunction}` must accept either 0 or 1 positional arguments"
            )

        return numArgs
