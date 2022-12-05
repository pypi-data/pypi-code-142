from tracemalloc import start
from ticsummary_domain import dataTIC, databaseMYSQL, inputDataHandler
from ticsummary_domain.ui.mainWindow import MainWindow, ModeInterface as MWModeInterface
from ticsummary_domain.ui.connectionConfigurationDialog import ConnectionConfiguration
from ticsummary_domain.ui.openSqlDataDialog import OpenSQLData
from ticsummary_domain.ui.chooseRecordDialog import ChooseRecordDialog
from ticsummary_domain import databaseMYSQL
from ticsummary_domain.backWorking import factoryThreadByTask
from ticsummary_domain import modeShowData as modeSD
from ticsummary_domain import outputDataHandler

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QTimer
import numpy as np

class Model(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.__initView__()
        self.__initSignal__()
        self.__initThreadPool__()
        self.sqlParameters = None
        self.currentModeSD = modeSD.modeShowData.MANUALMODE
        self.profileXDescriptionDevice = dataTIC.DescriptionDevice("profileX",0,31)
        self.profileYDescriptionDevice = dataTIC.DescriptionDevice("profileY",32,63)
        self.additionalCounterCh1 = dataTIC.DescriptionDevice("Counter ch1", 64, 64)
        self.additionalCounterCh2 = dataTIC.DescriptionDevice("Counter ch2", 65, 65)
        self.additionalCounterCh3 = dataTIC.DescriptionDevice("Counter ch3", 66, 66)
        self.additionalCounterCh4 = dataTIC.DescriptionDevice("Counter ch4", 67, 67)
        self.additionalCounterCh5 = dataTIC.DescriptionDevice("Counter ch5", 68, 68)
        self.additionalCounterCh6 = dataTIC.DescriptionDevice("Counter ch6", 69, 69)
        self.additionalCounterCh7 = dataTIC.DescriptionDevice("Counter ch7", 70, 70)
        self.additionalCounterCh8 = dataTIC.DescriptionDevice("Counter ch8", 71, 71)


        self.currentManualIdData = 1
        self.currentManualSumIdData = 1
        self.currentManualSumCountData = 2
    def __initView__(self):
        self.mainWindow = MainWindow(version='1.2.16')
        self.mainWindow.show()
    def __initThreadPool__(self):
        self.threadPool = QtCore.QThreadPool.globalInstance()
        self.threadPool.setMaxThreadCount(60)
        
    def __initSignal__(self):
        self.mainWindow.comboBoxType.currentIndexChanged.connect(self.__typeChanged)
        self.mainWindow.actionConnectionSqlDatabase.triggered.connect(self.openConnectionConfiguration)
        self.mainWindow.actionFrom_sql_database.triggered.connect(self.startOpenSQLData)
        self.mainWindow.pushButtonChooseRecord.clicked.connect(self.openChooseRecordDialog)
        self.mainWindow.sigIterationValueId.connect(self.iterationData)
        self.mainWindow.sigSetIdCountRecord.connect(self.setIdCountRecord)
        #self.mainWindow.sigSetNewCountSum.connect(self.setNewCountSum)
        self.mainWindow.actionExportDataToCsv.triggered.connect(self.exportData)
        #self.mainWindow.connectSignalIterationValueId(self.iterationData)
        #self.mainWindow.ui.comboBoxListData.currentTextChanged.connect(self.loadDataByIdAndPlot)
    
    def __del__(self):
        if hasattr(self, "connector"):
            self.connector.close()

    def __startCheckNewCountInDB__(self):
        self.checkCountTimer = QTimer()
        self.checkCountTimer.timeout.connect(lambda:self.__checkCountDB__())
        self.checkCountTimer.start(5000)
    def __stopCheckNewCountInDB__(self):
        self.checkCountTimer.stop()
    def __checkCountDB__(self):
        self.updateSizeDB()
        self.checkBorderIdValue()
    
    def openConnectionConfiguration(self):
        connectionConfigurationDialog = ConnectionConfiguration(parent=self.mainWindow, parameters=self.sqlParameters)
        connectionConfigurationDialog.setModal(True)
        connectionConfigurationDialog.exec()
        if connectionConfigurationDialog.result() == QtWidgets.QDialog.DialogCode.Accepted:
            #self.mainWindow.setInfinityProgress(True)
            self.sqlParameters = connectionConfigurationDialog.getNewParameters()
            self.connector = databaseMYSQL.openConnection(self.sqlParameters)
            self.updateSizeDB(databaseMYSQL.getCountRecords(self.sqlParameters.table, self.connector))
            self.currentModeSD.uninit(self)
            self.currentModeSD = modeSD.modeShowData.MANUALMODE
            self.mainWindow.setMode(self.currentModeSD.modeInterface)
            self.currentModeSD.init(self)

    def __loadNewConnection__(self,sqlParameters):
        self.listData = databaseMYSQL.getListId(self.sqlParameters)

    def loadDataByIdAndPlot(self,id:str, connector=None):
        i = 0
        if connector == None:
            self.controllerBWTask = factoryThreadByTask(self.__loadDataById__,self.__plotData__,id=int(id),connector=self.connector)
        else:
            self.controllerBWTask = factoryThreadByTask(self.__loadDataById__,self.__plotData__,id=int(id),connector=connector)
        self.controllerBWTask.start()

    def __plotData__(self,loadedData):
        self.profileX1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.profileXDescriptionDevice.channelFrom, self.profileXDescriptionDevice.channelTo)
        self.profileY1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.profileYDescriptionDevice.channelFrom, self.profileYDescriptionDevice.channelTo)
        self.profileX2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.profileXDescriptionDevice.channelFrom, self.profileXDescriptionDevice.channelTo)
        self.profileY2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.profileYDescriptionDevice.channelFrom, self.profileYDescriptionDevice.channelTo)

        self.additionalCounterCh1B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh1.channelFrom, self.additionalCounterCh1.channelTo)
        self.additionalCounterCh2B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh2.channelFrom, self.additionalCounterCh2.channelTo)
        self.additionalCounterCh3B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh3.channelFrom, self.additionalCounterCh3.channelTo)
        self.additionalCounterCh4B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh4.channelFrom, self.additionalCounterCh4.channelTo)
        self.additionalCounterCh5B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh5.channelFrom, self.additionalCounterCh5.channelTo)
        self.additionalCounterCh6B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh6.channelFrom, self.additionalCounterCh6.channelTo)
        self.additionalCounterCh7B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh7.channelFrom, self.additionalCounterCh7.channelTo)
        self.additionalCounterCh8B1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.additionalCounterCh8.channelFrom, self.additionalCounterCh8.channelTo)

        self.additionalCounterCh1B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh1.channelFrom, self.additionalCounterCh1.channelTo)
        self.additionalCounterCh2B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh2.channelFrom, self.additionalCounterCh2.channelTo)
        self.additionalCounterCh3B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh3.channelFrom, self.additionalCounterCh3.channelTo)
        self.additionalCounterCh4B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh4.channelFrom, self.additionalCounterCh4.channelTo)
        self.additionalCounterCh5B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh5.channelFrom, self.additionalCounterCh5.channelTo)
        self.additionalCounterCh6B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh6.channelFrom, self.additionalCounterCh6.channelTo)
        self.additionalCounterCh7B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh7.channelFrom, self.additionalCounterCh7.channelTo)
        self.additionalCounterCh8B2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.additionalCounterCh8.channelFrom, self.additionalCounterCh8.channelTo)

        self.scaleChannelToMM = 2
        self.mainWindow.setData(
            self.profileX1Data,
            float(loadedData.timeSliceB1/(10**6)),
            0,
            self.profileY1Data,
            float(loadedData.timeSliceB1/(10**6)),
            0,
            self.profileX2Data,
            float(loadedData.timeSliceB2/(10**6)),
            0,
            self.profileY2Data,
            float(loadedData.timeSliceB2/(10**6)),
            0,
            (
                self.additionalCounterCh1B1Data,
                self.additionalCounterCh2B1Data,
                self.additionalCounterCh3B1Data,
                self.additionalCounterCh4B1Data,
                self.additionalCounterCh5B1Data,
                self.additionalCounterCh6B1Data,
                self.additionalCounterCh7B1Data,
                self.additionalCounterCh8B1Data,),
            (
                self.additionalCounterCh1B2Data,
                self.additionalCounterCh2B2Data,
                self.additionalCounterCh3B2Data,
                self.additionalCounterCh4B2Data,
                self.additionalCounterCh5B2Data,
                self.additionalCounterCh6B2Data,
                self.additionalCounterCh7B2Data,
                self.additionalCounterCh8B2Data,),
            self.scaleChannelToMM)
        self.descriptionLoadedData = loadedData.description
        self.mainWindow.setDataInfo(loadedData.description)
        self.checkBorderIdValue()
        if self.mainWindow.isBusy:
            self.mainWindow.setBusyMode(False)
        self.mainWindow.enableControlDataMode()
        #self.mainWindow.loadPrevModeInterface()
        #self.mainWindow.flagControlKeysOff = False

    def iterationData(self,it):
        self.currentModeSD.iterationId(self,it)

    def setIdCountRecord(self,id,count):
        if count != -1:
            self.currentManualSumCountData = count
            self.currentModeSD.setId(self,id)
        else:
            self.currentModeSD.setId(self,id)

    def updateSizeDB(self,value=None):
        if (value==None):
            value = databaseMYSQL.getCountRecordsByParameters(self.sqlParameters)
        self.countRecordsInDB = value
        self.mainWindow.setRangeId(0, self.countRecordsInDB)

    def __typeChanged(self,id):
        self.currentModeSD.uninit(self)
        if id == 0:
            self.currentModeSD = modeSD.modeShowData.MANUALMODE
        if id == 1:
            self.currentModeSD = modeSD.modeShowData.ONLINE
        if id == 2:
            self.currentModeSD = modeSD.modeShowData.MANUALSUMMODE
        self.currentModeSD.init(self)
        self.mainWindow.setMode(self.currentModeSD.modeInterface)

    def checkBorderIdValue(self):
        if self.currentModeSD == modeSD.modeShowData.MANUALMODE:
            self.mainWindow.setButtonPrevEnabled(not self.currentManualIdData == 1)
            self.mainWindow.prevEnabled = not self.currentManualIdData == 1
            self.mainWindow.setButtonNextEnabled(not self.currentManualIdData == self.countRecordsInDB)
            self.mainWindow.nextEnabled = not self.currentManualIdData == self.countRecordsInDB
        elif self.currentModeSD == modeSD.modeShowData.MANUALSUMMODE:
            self.mainWindow.setButtonPrevEnabled(not self.currentManualSumIdData - self.currentManualSumCountData < 1)
            self.mainWindow.prevEnabled = not self.currentManualSumIdData - self.currentManualSumCountData < 1
            self.mainWindow.setButtonNextEnabled(not self.currentManualSumIdData + self.currentManualSumCountData > self.countRecordsInDB)
            self.mainWindow.nextEnabled = not self.currentManualSumIdData + self.currentManualSumCountData > self.countRecordsInDB

    def openChooseRecordDialog(self):
        chooseRecordDialog = ChooseRecordDialog(self.mainWindow,self)
        chooseRecordDialog.setIdRecordSignal.connect(self.setIdCountRecord)
        chooseRecordDialog.show()

    def startOpenSQLData(self):
        self.mainWindow.setInfinityProgress()
        self.handlerTaskOpenData = runTask(self.taskOpenData,self.endOpenSqlData)
        
    def taskOpenData(self):
        self.openSQLData = OpenSQLData(self.sqlParameters, lambda result: self.setNewListData(result))
        
    def endOpenSqlData(self):
        self.mainWindow.unsetInfinityProgress()
        self.openSQLData.show()

    def setNewConnectionParameters(self, parameters):
        self.sqlParameters = parameters
        
    def setNewListData(self, list):
        self.listData = list

    def exportData(self):
        outputDataHandler.saveDataToCSV(self.mainWindow, [['X Buffer 1',self.profileX1Data ],['Y Buffer 1',self.profileY1Data ],['X Buffer 2',self.profileX2Data ],['Y Buffer 2',self.profileY2Data ]], f'{self.descriptionLoadedData} Scale_Channel_MM={self.scaleChannelToMM}')