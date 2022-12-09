from __future__ import annotations

import typing as t

from pyqtgraph import QtCore, QtWidgets
from pyqtgraph.parametertree import Parameter

from qtextras import fns

_layoutTypes = t.Union[t.Literal["H"], t.Literal["V"]]


class EasyWidget:
    def __init__(
        self,
        children: t.MutableSequence,
        layout: str = None,
        useSplitter=False,
        baseWidget: QtWidgets.QWidget = None,
    ):
        if baseWidget is None:
            baseWidget = QtWidgets.QWidget()
        self._built = False
        self.children_ = children
        self.useSplitter = None
        self.widget_ = baseWidget
        self.layout_ = None

        self._resetOpts(useSplitter, layout)

    def _resetOpts(self, useSplitter, layout):
        if layout == "V":
            orient = QtCore.Qt.Orientation.Vertical
            layout = QtWidgets.QVBoxLayout
        elif layout == "H":
            orient = QtCore.Qt.Orientation.Horizontal
            layout = QtWidgets.QHBoxLayout
        else:
            orient = layout = None
        self.orient_ = orient

        if useSplitter == self.useSplitter and self.layout_:
            return
        # Had children in existing widget which will be discarded when changing self
        # widget_ to splitter
        if self.widget_.children() and useSplitter:
            raise ValueError(
                "Cannot change splitter status to *True* when widget already has "
                "children"
            )
        self.useSplitter = useSplitter

        if useSplitter:
            self.layout_ = QtWidgets.QSplitter(orient)
            self.widget_ = self.layout_
        else:
            try:
                self.layout_ = layout()
                self.widget_.setLayout(self.layout_)
            except TypeError:
                # When layout is none
                self.layout_ = None

    def build(self):
        if self._built:
            return
        if self.layout_ is None:
            raise ValueError(
                'Top-level orientation must be set to "V" or "H" before adding children'
            )
        if self.orient_ == QtCore.Qt.Orientation.Horizontal:
            chSuggested = "V"
        elif self.orient_ == QtCore.Qt.Orientation.Vertical:
            chSuggested = "H"
        else:
            chSuggested = None

        for ii, child in enumerate(self.children_):
            morphChild = self.addChild(child, chSuggested)
            if morphChild is not child:
                self.children_[ii] = morphChild
        self._built = True

    def addChild(
        self,
        child: t.Union[QtWidgets.QWidget, t.Sequence, EasyWidget],
        suggestedLayout: str = None,
    ):
        if isinstance(child, QtWidgets.QWidget):
            self.layout_.addWidget(child)
        else:
            child = self.listChildrenWrapper(child, suggestedLayout)
            # At this point, child should be an EasyWidget
            child.build()
            self.layout_.addWidget(child.widget_)
        return child

    def insertChild(self, child: EasyWidget, index: int):
        child.build()
        return self.layout_.insertWidget(index, child.widget_)

    def hide(self):
        self.widget_.hide()

    def show(self):
        self.widget_.show()

    def removeInnerMargins(self):
        for ch in self.children_:
            if isinstance(ch, EasyWidget):
                ch.removeInnerMargins()
                lay = ch.widget_.layout()
                # layout_ != widget_.layout() for splitter
                if lay:
                    lay.setContentsMargins(0, 0, 0, 0)
                    lay.setSpacing(0)

    @classmethod
    def listChildrenWrapper(
        cls,
        children: t.Union[t.MutableSequence, EasyWidget],
        maybeNewLayout: str = None,
    ):
        if not isinstance(children, EasyWidget):
            children = cls(children)
        if children.layout_ is None and maybeNewLayout is not None:
            children._resetOpts(children.useSplitter, maybeNewLayout)
        return children

    @classmethod
    def buildMainWindow(
        cls,
        children: t.Union[t.MutableSequence, EasyWidget],
        window: QtWidgets.QMainWindow = None,
        layout="V",
        **kwargs,
    ) -> _HasEasyChild:
        if window is None:
            window = QtWidgets.QMainWindow()
        if isinstance(children, t.MutableSequence):
            children = cls(children, layout=layout, **kwargs)

        children.build()
        window.easyChild = children
        window.setCentralWidget(children.widget_)
        children.removeInnerMargins()
        # _HasEasyChild is mostly defined to allow editors to recognize the
        # custom attribute
        return window  # noqa

    @classmethod
    def buildWidget(
        cls, children: t.MutableSequence | EasyWidget, layout="V", **kwargs
    ):
        builder = cls(children, layout=layout, **kwargs)
        builder.build()
        # See noqa note on buildMainWindow
        retWidget: _HasEasyChild = builder.widget_  # noqa
        retWidget.easyChild = builder
        builder.removeInnerMargins()
        return retWidget

    @classmethod
    def fromPgParam(
        cls, param: Parameter = None, layout="H", **opts
    ) -> EasyWidget | tuple[EasyWidget, Parameter]:
        """
        Creates a form-style EasyWidget (name + edit widget) from pyqtgraph parameter
        options or a parameter directly.

        Parameters
        ----------
        param
            Parameter to use, if it already exists. Otherwise, one is created from
            `opts` and returned.
        layout
            EasyWidget layout
        opts
            If `parameter` is unspecified, a parameter is created from these opts instead
            and returned

        Returns
        -------
        Just the EasyWidget if ``parameter`` is provided, otherwise (EasyWidget, Parameter)
        tuple
        """
        returnParam = False
        if param is None:
            param = Parameter.create(**opts)
            returnParam = True
        try:
            item = param.itemClass(param, 0)
            editWidget = item.makeWidget()
            fns.hookupParamWidget(param, editWidget)
        except AttributeError as ex:
            raise ValueError(
                f"Can only create EasyWidgets from parameters that have an itemClass"
                f" and implement makeWidget(). Problem type: {opts['type']}\n"
                f"Exception: {ex}"
            )
        lbl = QtWidgets.QLabel(opts["name"])
        obj = cls([lbl, editWidget], layout)
        obj.build()
        if returnParam:
            return obj, param
        return obj


class _HasEasyChild(QtWidgets.QMainWindow):
    """
    Provided just for type checking purposes
    """

    easyChild: EasyWidget
