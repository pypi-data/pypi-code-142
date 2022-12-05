import pyqtgraph as pg
from pyqtgraph.dockarea import DockArea, Dock
from pyqtgraph.graphicsItems.GradientEditorItem import Gradients

from PyQt6 import QtWidgets,QtGui
import numpy as np

from ticsummary_domain.ui.settingsColorBarDialog import SettingsColorBarDialog

class CounterDock(Dock):

    def __init__(self,keyEventHandler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyEventHandler = keyEventHandler
        self.stateHidden = False
        self.__initGraph__()
    def keyPressEvent(self,event):
        self.keyEventHandler(event)
    def updateStyle(self):
        Dock.updateStyle(self)
        self.setOrientation("horizontal")
    def __initGraph__(self):
        labelAxisStyle = {'color': '#FFF', 'font-size': '8pt'}
        titlePlotStyle = {'color': '#FFF', 'font-size': '14pt'}
        font=QtGui.QFont()
        font.setPixelSize(10)


        self.lineCounterPlot = pg.plot()
        self.lineCounterPlot.addLegend(offset=(30,30))
        self.lineCounterPlot.getAxis("bottom").setTickFont(font)
        self.lineCounterPlot.getAxis("left").setTickFont(font)
        self.addWidget(self.lineCounterPlot)
        self.lineCounterPlot.setTitle("Counter", **titlePlotStyle)
        self.lineCounterPlot.setLabel('left', "count", units="qty", **labelAxisStyle)
        self.lineCounterPlot.setLabel('bottom', "time", units="sec", **labelAxisStyle)

        self.counterCh1PlotDataItem = self.lineCounterPlot.plot(pen=(0,0,255),name="counterCh1")
        self.counterCh2PlotDataItem = self.lineCounterPlot.plot(pen=(0,255,255),name="counterCh2")
        self.counterCh3PlotDataItem = self.lineCounterPlot.plot(pen=(0,255,0),name="counterCh3")
        self.counterCh4PlotDataItem = self.lineCounterPlot.plot(pen=(255,255,0),name="counterCh4")
        self.counterCh5PlotDataItem = self.lineCounterPlot.plot(pen=(255,0,0),name="counterCh5")
        self.counterCh6PlotDataItem = self.lineCounterPlot.plot(pen=(128,0,128),name="counterCh6")
        self.counterCh7PlotDataItem = self.lineCounterPlot.plot(pen=(0,128,128),name="counterCh7")
        self.counterCh8PlotDataItem = self.lineCounterPlot.plot(pen=(128,128,0),name="counterCh8")

        self.plotDataItemList = list()

        self.plotDataItemList.append(self.counterCh1PlotDataItem)
        self.plotDataItemList.append(self.counterCh2PlotDataItem)
        self.plotDataItemList.append(self.counterCh3PlotDataItem)
        self.plotDataItemList.append(self.counterCh4PlotDataItem)
        self.plotDataItemList.append(self.counterCh5PlotDataItem)
        self.plotDataItemList.append(self.counterCh6PlotDataItem)
        self.plotDataItemList.append(self.counterCh7PlotDataItem)
        self.plotDataItemList.append(self.counterCh8PlotDataItem)
    
    def setData(self,x,dataList):
        for i in range(len(dataList)):
            self.plotDataItemList[i].setData(x,dataList[i])

    def clearData(self):
        for item in self.plotDataItemList:
            item.clear()
        self.lineCounterPlot.replot()
    def mhide(self):
        self.stateHidden = True
        Dock.hide(self)
    def mshow(self):
        self.stateHidden = False
        Dock.show(self)
    def hide(self):
        if self.stateHidden:
            Dock.hide(self)
    def show(self):
        if not self.stateHidden:
            Dock.show(self)