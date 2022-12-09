from __future__ import annotations

import typing as t

import numpy as np
import pandas as pd
import pyqtgraph as pg
from _warnings import warn
from pyqtgraph import QtCore, QtGui, QtWidgets
from pyqtgraph.graphicsItems.LegendItem import ItemSample
from pyqtgraph.graphicsItems.ScatterPlotItem import drawSymbol
from pyqtgraph.graphicsItems.ViewBox.ViewBoxMenu import ViewBoxMenu

from qtextras import fns
from qtextras._funcparse import bindInteractorOptions as bind
from qtextras.misc import CompositionMixin
from qtextras.params import ParameterEditor, RunOptions
from qtextras.typeoverloads import FilePath
from qtextras.widgets.easywidget import EasyWidget


class ImageViewer(CompositionMixin, pg.PlotWidget):
    sigMouseMoved = QtCore.Signal(object)  # ndarray(int, int) xy pos rel. to image

    def __init__(self, imageSource: np.ndarray = None, **kwargs):
        super().__init__(**kwargs)
        self.pxColorLbl, self.mouseCoordsLbl = None, None
        """
        Set these to QLabels to have up-to-date information about the image coordinates
        under the mouse
        """
        self.toolsEditor = ParameterEditor(name="Region Tools")
        vb = self.getViewBox()
        self.menu: QtWidgets.QMenu = vb.menu
        self.oldVbMenu: ViewBoxMenu = vb.menu
        # Disable default menus
        self.plotItem.ctrlMenu = None
        self.sceneObj.contextMenu = None

        self.setAspectLocked(True)
        vb.invertY()

        # -----
        # IMAGE
        # -----
        self.imageItem = self.exposes(pg.ImageItem())
        self.imageItem.setZValue(-100)
        self.addItem(self.imageItem)
        if imageSource is not None:
            self.setImage(imageSource)

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent):
        super().mouseMoveEvent(ev)
        pos = ev.position() if hasattr(ev, "position") else ev.localPos()
        relpos = self.imageItem.mapFromScene(pos)
        xyCoord = np.array([relpos.x(), relpos.y()], dtype=int)
        if (
            self.imageItem.image is None
            or np.any(xyCoord < 0)
            or np.any(xyCoord > np.array(self.imageItem.image.shape[:2][::-1]) - 1)
        ):
            return
        imgValue = self.imageItem.image[xyCoord[1], xyCoord[0], ...]
        self.updateCursorInfo(xyCoord, imgValue)
        self.sigMouseMoved.emit(xyCoord)

    def updateCursorInfo(self, xyPos: np.ndarray, pxValue: np.ndarray):
        if pxValue is None:
            return
        if self.mouseCoordsLbl is not None:
            self.mouseCoordsLbl.setText(f"Mouse (x,y): {xyPos[0]}, {xyPos[1]}")

        if self.pxColorLbl is None:
            return
        self.pxColorLbl.setText(f"Pixel Color: {pxValue}")
        if self.imageItem.qimage is None:
            return
        imColor = self.imageItem.qimage.pixelColor(*xyPos)
        grayClr = QtGui.qGray(imColor.rgb())
        fontColor = "black" if grayClr > 127 else "white"
        self.pxColorLbl.setStyleSheet(f"background:{imColor.name()}; color:{fontColor}")

    def setImage(
        self, imageSource: t.Union[FilePath, np.ndarray] = None, stripAlpha=False
    ):
        """
        Allows the user to change the main image either from a filepath or array data.
        Files can be any format accepted by QImage -> pg.imageToArray Optionally strips
        the alpha channel from the image, if it exists (i.e. if its shape is MxNx4)
        """
        if isinstance(imageSource, FilePath.__args__):
            # TODO: Handle alpha channel images. For now, discard that data
            qtImg = QtGui.QImage(str(imageSource))
            nchans = qtImg.bitPlaneCount() // 8
            imageSource = pg.imageToArray(qtImg, transpose=False)

            if nchans >= 3:
                chanOrder = [2, 1, 0]
                # Alpha is always added by imageToArray, so chop it off if necessary
                if nchans == 4:
                    chanOrder.append(3)
                imageSource = imageSource[..., chanOrder]
                # imageToArray creates bgr array, turn this into rgb. Also,
                # some algorithms perform better with contiguous arrays, so make sure
                # potential views after this operation remain contiguous Finally,
                # force a copy to avoid crashing after qtImg (which owns the array) is
                # garbage collected
            imageSource = imageSource.copy(order="C")
        if imageSource is None:
            self.imageItem.clear()
        else:
            if stripAlpha and imageSource.ndim > 2:
                imageSource = imageSource[:, :, :3]
            self.imageItem.setImage(imageSource)

    def widgetContainer(self, asMainWin=True, showTools=True, **kwargs):
        """
        Though this is a PlotWidget class, it has a lot of widget children (toolsEditor
        group, buttons) that are not visible when spawning the widget. This is a
        convenience method that creates a new, outer widget from all the graphical
        elements of an EditableImage.

        Parameters
        ----------
        asMainWin
            Whether to return a QMainWindow or QWidget
        showTools
            If `showMainWin` is True, this determines whether to show the tools editor
            with the window
        **kwargs
            Passed to either EasyWidget.buildMainWin or EasyWidget.BuildWidget,
            depending on the value of `asMainWin`
        """
        if asMainWin:
            wid = EasyWidget.buildMainWindow(self._widgetContainerChildren(), **kwargs)
            self.mouseCoordsLbl = QtWidgets.QLabel()
            self.pxColorLbl = QtWidgets.QLabel()
            wid.statusBar().addWidget(self.mouseCoordsLbl)
            wid.statusBar().addWidget(self.pxColorLbl)
            dock = QtWidgets.QDockWidget("Tools", wid)
            dock.setWidget(self.toolsEditor)
            wid.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            if showTools:
                self.toolsEditor.show()
        else:
            wid = EasyWidget.buildWidget(self._widgetContainerChildren(), **kwargs)
        return wid

    def showAndExec(self):
        win = self.widgetContainer(True)
        QtCore.QTimer.singleShot(0, win.showMaximized)
        QtCore.QCoreApplication.instance().exec_()

    def _widgetContainerChildren(self):
        """
        Returns the children that should be added to the container when
        widgetContainer() is called
        """
        return [self]


class CompositorItemSample(ItemSample):
    def paint(self, p: QtGui.QPainter, *args):
        opts = self.item.opts

        if opts.get("antialias"):
            p.setRenderHint(p.Antialiasing)
        symbol = opts.get("symbol", None)
        p.translate(0, 14)
        drawSymbol(
            p, symbol, opts["size"], pg.mkPen(opts["pen"]), pg.mkBrush(opts["brush"])
        )


class CompositorLegend(pg.LegendItem):
    def paint(self, p: QtGui.QPainter, *args):
        br = self.boundingRect()
        p.setPen(self.opts["pen"])
        p.setBrush(self.opts["brush"])
        p.drawRoundedRect(br, 5, 5)


class MaskCompositor(ImageViewer):
    _cachedCmapLimits = None

    def __init__(self, img: np.ndarray = None):
        super().__init__()
        # -----
        # Create properties
        # -----
        self.masksParameter = fns.getParameterChild(
            self.toolsEditor.rootParameter, "Overlays"
        )
        if self._cachedCmapLimits is None:
            # Set at class level to cache for new instances too
            type(self)._cachedCmapLimits = fns.listAllPgColormaps()

        self.legend = CompositorLegend(
            offset=(5, 5), horSpacing=5, brush="#ccce", pen="k"
        )
        self.recordDf = pd.DataFrame(
            columns=["name", "item", "opacity", "isMask"]
        ).set_index("name")
        # Initialized in clearOverlays and updateLabelMap. Given here to avoid
        # intellisense warnings
        self.inUseLabelValues = (
            self.scatterSer
        ) = self.backgroundValues = self.labelToNameMapping = None
        self.updateLabelMap()
        self.legendFontArgs = {"size": "11pt", "color": "k", "bold": True}
        self.curZ = 2

        # -----
        # Configure relationships
        # -----
        self.legend.setParentItem(self.plotItem)
        self.viewbox: pg.ViewBox = self.getViewBox()

        self.allVisible = True
        # for ax in 'left', 'bottom', 'right', 'top':
        #   self.mainImage.plotItem.hideAxis(ax)
        # self.mainImage.setContentsMargins(0, 0, 0, 0)

        def newFmt(name):
            if name.startswith("set"):
                name = name.replace("set", "")
            name = fns.pascalCaseToTitle(name)
            return name

        with fns.nameFormatter.set(newFmt):
            self.propertiesProc = self.toolsEditor.registerFunction(
                self.setOverlayProperties,
                runOptions=RunOptions.ON_CHANGED,
                colormap=dict(limits=self._cachedCmapLimits),
                fullLabelMapColors=dict(ignore=True),
            )
            self.toolsEditor.registerFunction(self.save)
            self.toolsEditor.registerFunction(
                lambda: self.imageItem.setVisible(not self.imageItem.isVisible()),
                name="Toggle Image Visible",
            )
            self.toolsEditor.registerFunction(
                lambda: self.legend.setVisible(not self.legend.isVisible()),
                name="Toggle Legend Visible",
            )
            self.toolsEditor.registerFunction(
                self.toggleAllVisible, parent=("Overlays",)
            )
        if img is not None:
            self.setImage(img)
        self.clearOverlays()

    @staticmethod
    def _createLabelToNameMapping(data=None):
        """
        Helper method to ensure proper dtypes when making a legend series. Helps avoid
        pitfalls with empty data, etc.
        """
        if data is None:
            data = []
        ser = pd.Series(data, dtype=str)
        ser.index = ser.index.astype("int64", copy=False)
        return ser

    def _addItemCtrls(self, record: pd.Series):
        item = record["item"]

        def maskOpts(_, visible=True):
            item.setVisible(visible)

        newParam = fns.getParameterChild(
            self.masksParameter,
            childOpts={"name": record.name, "type": "bool", "value": True},
        )
        newParam.sigValueChanged.connect(maskOpts)

    def setBaseImage(self, baseImg: np.ndarray, clearOverlays=True):
        # self.winSz = baseImg.shape[:2][::-1]
        # self.viewbox.setRange(
        #   xRange=[0, imageItem.shape[1]], yRange=[0, imageItem.shape[0]], padding=0
        # )
        self.setImage(baseImg)
        # self.refreshWinContents()
        if clearOverlays:
            self.clearOverlays()

    def setImage(self, *args, **kwargs):
        super().setImage(*args, **kwargs)
        self._updateLegendPos()

    def _addRecord(self, rec: pd.Series, update=True):
        self.recordDf.loc[rec.name] = rec
        self.curZ += 1

        self._addItemCtrls(rec)

        if update:
            self._updateGraphics()

    def addImageItem(self, item: pg.ImageItem, **kwargs):
        kwargs.setdefault("opacity", -1)
        name = self._getUniqueName(kwargs.pop("name", None))
        update = kwargs.pop("update", True)
        kwargs.setdefault("isMask", False)
        newRecord = dict(item=item, **kwargs)
        item.setZValue(self.curZ + 1)
        self.viewbox.addItem(item)

        rec = pd.Series(newRecord, name=name)
        self._addRecord(rec, update)

    def _getUniqueName(self, baseName: str = None):
        if baseName is None:
            baseName = "[No Name]"
        ii = 2
        name = baseName
        while name in self.recordDf.index:
            name = f"{baseName} {ii}"
            ii += 1
        return name

    def addLabelMask(
        self,
        labelMask: np.ndarray,
        name=None,
        clearOverlays=False,
        fullLabelMapInLegend=False,
        **overlayKwargs,
    ):
        """
        Splits a label mask into its constituent labels and adds a mask for each unique
        label.

        Parameters
        ----------
        labelMask
            Grayscale label mask of integers
        name
            Name to identify this mask in the property editor
        clearOverlays
            If *True*, `clearOverlays` will be called before adding this item. This
            is useful if only one mask is viewed at a time
        fullLabelMapInLegend
            See ``updateLegendEntries`` -- this parameter is passed during legend
            creation
        **overlayKwargs
            Keyword arguments passed to setOverlayProperties
        """
        if clearOverlays and len(self.recordDf):
            # Reuse item if possible
            item = self._reuseLastOverlay(labelMask, name)
        else:
            item = None
        maskValues = np.unique(labelMask.ravel())
        # Booleans don't mix well with int series indexing/logic
        # Floats are completely wonky
        if np.issubdtype(maskValues.dtype, np.bool_):
            maskValues = maskValues.astype("uint8")
        elif not np.issubdtype(maskValues.dtype, np.integer):
            raise ValueError(
                f"Overlays can only be created using integer dtypes. Encountered"
                f" `{maskValues.dtype}`"
            )

        self.inUseLabelValues = np.union1d(self.inUseLabelValues, maskValues)
        self.updateLegendEntries(useFullLabelMap=fullLabelMapInLegend)
        if item is None:
            self.addImageItem(
                pg.ImageItem(labelMask),
                name=name,
                isMask=True,
                opacity=-1,
                update=False,
            )
        self.propertiesProc(**overlayKwargs)

    def _reuseLastOverlay(self, newImageData=None, newName=None, isMask=True):
        """
        When a set of images must be overlaid separately, it is more efficient to reuse
        an image item compared to constantly adding and removing them from a scene.
        Assumes at least one record is already present in ``self.recordDf``
        """
        self.clearOverlays(self.recordDf.index[:-1])
        # Use two steps to update name so conflicts are avoided
        self.recordDf.index = [None]
        self.recordDf.index = [self._getUniqueName(newName)]
        rec = self.recordDf.iloc[-1]
        rec["isMask"] = isMask
        item = rec["item"]
        item.setImage(newImageData)
        return item

    def setLegendFontStyle(self, startItemIdx=0, **lblTxtArgs):
        for item in self.legend.items[startItemIdx:]:
            for single_item in item:
                if isinstance(single_item, pg.LabelItem):
                    single_item.setText(single_item.text, **lblTxtArgs)

    def updateLegendEntries(self, useFullLabelMap=False, updateOverlays=False):
        """
        Parameters
        ----------
        useFullLabelMap
            If *True*, guarantees that every entry in the label->name mapping will be
            present in the legend.
        updateOverlays
            If *True*, the image overlay properties will be refereshed
        """
        if useFullLabelMap:
            labels = np.union1d(self.inUseLabelValues, self.labelToNameMapping.index)
        else:
            labels = self.inUseLabelValues
        labels = np.setdiff1d(labels, self.backgroundValues)
        names = self.labelToNameMapping.reindex(labels)
        needsEntry = names.isna()
        names[needsEntry] = names.index[needsEntry].map(str)
        self.legend.clear()
        self.scatterSer = pd.Series(
            [None] * len(names), index=names.index, dtype=object
        )
        # Make sure alpha is not carried over
        for value, name in names.items():
            scat = pg.ScatterPlotItem(symbol="s", width=5)
            self.legend.addItem(CompositorItemSample(scat), name=name)
            self.scatterSer.at[value] = scat
        if updateOverlays:
            self.propertiesProc()

    def updateLabelMap(
        self,
        labelMap: dict | pd.Series = None,
        backgroundValues=0,
        updateOverlays=False,
    ):
        """
        Parameters
        ----------
        labelMap
            Series or dict-like with integer key and string value. Gives a legend name
            to each label in the image. Unspecified labels will be named by their
            numeric value, e.g. 34 will be '34'. Note that this will update the global
            legend, meaning if {10 -> 'test'} is a legend entry, it will overwrite the
            old legend value for 10.
        backgroundValues
            Represents label mask values that should be transparent in the overlay
        updateOverlays
            If *True*, overlay graphics will be refreshed to reflect these updates. Keep
            *False* if several updates will happen in sequence.
        """
        if labelMap is None:
            labelMap = {}
        if np.isscalar(backgroundValues):
            backgroundValues = [backgroundValues]
        self.backgroundValues = np.array(backgroundValues)
        self.labelToNameMapping = self._createLabelToNameMapping(labelMap)
        if updateOverlays:
            self._updateGraphics()

    @bind(opacity=dict(limits=[0, 1], step=0.1), colormap=dict(type="popuplineeditor"))
    def setOverlayProperties(
        self, colormap="magma", opacity=0.6, fullLabelMapColors=False
    ):
        """
        Sets overlay properties

        Parameters
        ----------
        colormap
            Colormap to use for the overlay. Should be a string that names a pyqtgraph
            colormap
        opacity
            Opacity of the overlay, from 0 (transparent) to 1 (opaque)
        fullLabelMapColors
            If *True*, enough colors will be generated for all labels in
            ``self.labelToNameMapping``. If *False*, only enough colors will be
            generated for the labels in the added masks.
        """
        maskIdxs = self.recordDf["isMask"].to_numpy(bool)
        cmap = fns.getAnyPgColormap(colormap)
        labelValues = self.scatterSer.index.values
        if fullLabelMapColors:
            labelValues = np.union1d(labelValues, self.labelToNameMapping.index.values)
        if not len(labelValues):
            pass  # return
        if cmap is None:
            raise ValueError(f"Invalid colormap: {colormap}")
        colors = cmap.getLookupTable(nPts=len(labelValues), alpha=True)
        colors[:, -1] = opacity * 255
        # If a labelmap has entries, try to scale the colormap to contain all
        # possibilities
        numEntries = (
            max(
                np.max(labelValues, initial=-1),
                np.max(self.labelToNameMapping.index.values, initial=-1),
            )
            + 1
        )
        lut = np.zeros((numEntries, 4), dtype="uint8")
        lut[labelValues] = colors
        bgValsInLut = self.backgroundValues[self.backgroundValues < len(lut)]
        lut[bgValsInLut] = 0
        for idx, scat in self.scatterSer.items():
            # Make sure alpha is not carried over
            color = lut[idx, :-1]
            brush, pen = pg.mkBrush(color), pg.mkPen(color)
            scat.setData(symbol="s", brush=brush, pen=pen, width=5)
        for _, maskRec in self.recordDf[maskIdxs].iterrows():
            itemOpacity = maskRec["opacity"]
            if itemOpacity < 0:
                itemOpacity = opacity
            maskRec["item"].setOpts(
                lut=lut, opacity=itemOpacity, levels=[0, numEntries - 1]
            )
        # Handle non-mask items who still want controlled opacity
        for _, rec in self.recordDf[
            (~maskIdxs) & self.recordDf["opacity"] < 0
        ].iterrows():
            rec["item"].setOpts(opacity=opacity)
        self.setLegendFontStyle(**self.legendFontArgs)
        self.legend.update()

        # Handle all non-mask items now
        for name, remainingRec in self.recordDf[~maskIdxs].iterrows():
            curOpacity = remainingRec["opacity"]
            if curOpacity < 0:
                curOpacity = opacity
            remainingRec["item"].setOpacity(curOpacity)

    def _updateLegendPos(self):
        imPos = self.imageItem.mapToScene(self.imageItem.pos())
        self.legend.autoAnchor(imPos)

    def _updateGraphics(self):
        self.propertiesProc()

    def clearOverlays(self, clearIdxs=None):
        """
        Clears image item overlays by index. If No index is specified, all overlays are
        removed

        Parameters
        ----------
        clearIdxs
            Indexes of overlays to remove
        """
        if clearIdxs is None:
            clearIdxs = self.recordDf.index
        for imgItem in self.recordDf.loc[clearIdxs, "item"]:
            self.viewbox.removeItem(imgItem)
        keepIdxs = np.setdiff1d(self.recordDf.index, clearIdxs)
        self.recordDf: pd.DataFrame = self.recordDf.loc[keepIdxs].copy()
        self.inUseLabelValues = np.array([], "int64")
        self.updateLegendEntries()
        overlayParam = self.toolsEditor.rootParameter.child("Overlays")

        for idx in clearIdxs:
            overlayParam.child(idx).remove()

    def toggleAllVisible(self):
        for param in self.masksParameter:
            if param.type() == "bool":
                param.setValue(not self.allVisible)
        self.allVisible = not self.allVisible

    @bind(saveFile=dict(type="file", fileMode="AnyFile", acceptMode="AcceptSave"))
    def save(
        self,
        saveFile: FilePath = "",
        cropToViewbox=False,
        toClipboard=False,
        floatLegend=False,
    ):
        """
        Parameters
        ----------
        saveFile
            Save destination. If blank, no file is created.
        toClipboard
            Whether to copy to clipboard
        cropToViewbox
            Whether to only save the visible portion of the image
        floatLegend
            Whether to ancor the legend in the top-left corner (if *False*) or put it
            exactly where it is positioned currently (if *True*). In the latter case, it
            may not appear if out of view and `cropToViewbox` is *True*.
        """
        if self.imageItem.isVisible():
            saveImg = self.imageItem.getPixmap()
        else:
            saveImg = QtGui.QPixmap(*self.imageItem.image.shape[:2][::-1])
        painter = QtGui.QPainter(saveImg)

        visibleMasks = [
            p.name() for p in fns.flattenedParameters(self.masksParameter) if p.value()
        ]
        for name, item in self.recordDf["item"].items():
            if name in visibleMasks:
                painter.setOpacity(item.opacity())
                item.paint(painter)
        painter.setOpacity(1.0)

        if cropToViewbox:
            maxBnd = np.array(self.image.shape[:2][::-1]).reshape(-1, 1) - 1
            vRange = np.array(self.viewbox.viewRange()).astype(int)
            vRange = np.clip(vRange, 0, maxBnd)
            # Convert range to topleft->bottomright
            pts = QtCore.QPoint(*vRange[:, 0]), QtCore.QPoint(*vRange[:, 1])
            # Qt doesn't do so well overwriting the original reference
            origRef = saveImg
            saveImg = origRef.copy(QtCore.QRect(*pts))
            painter.end()
            painter = QtGui.QPainter(saveImg)
        if self.legend.isVisible():
            # Wait to paint legend until here in case cropping is active
            self._paintLegend(painter, floatLegend)

        if toClipboard:
            QtWidgets.QApplication.clipboard().setImage(saveImg.toImage())

        saveFile = str(saveFile)
        if saveFile and not saveImg.save(str(saveFile)):
            warn("Image compositor save failed", UserWarning)
        return saveImg

    def _paintLegend(self, painter: QtGui.QPainter, floatLegend=False):
        oldPos = self.legend.pos()
        try:
            exportScene = pg.GraphicsScene(parent=None)
            oldScale = max(
                np.clip(0.5 / np.array(self.imageItem.pixelSize()), 1, np.inf)
            )
            exportScene.addItem(self.legend)
            self.legend.setScale(oldScale)
            # Legend does not scale itself, handle this
            painter.save()
            if floatLegend:
                viewPos = self.viewbox.viewRect()
                viewX = max(viewPos.x(), 0)
                viewY = max(viewPos.y(), 0)
                imPos = self.legend.mapRectToItem(self.imageItem, self.legend.rect())
                painter.translate(int(imPos.x() - viewX), int(imPos.y() - viewY))
            exportScene.render(painter)
            self.legend.setScale(1 / oldScale)
            painter.restore()
        finally:
            self.legend.setParentItem(self.plotItem)
            self.legend.autoAnchor(oldPos, relative=False)

    def __getstate__(self):
        ret = dict(
            image=self.imageItem.image,
            legendVisible=self.legend.isVisible(),
        )
        if len(self.recordDf):
            ret["recordDf"] = self.recordDf

    def __setstate__(self, state):
        self.__init__(state["image"])
        self.legend.setVisible(state["legendVisible"])
        if "recordDf" in state:
            for _, rec in state["recordDf"].items():
                self._addRecord(rec, False)
            self._updateGraphics()
