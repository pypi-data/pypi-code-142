from __future__ import annotations

import typing as t

import numpy as np
import pandas as pd
from pyqtgraph import QtCore

from qtextras.constants import PrjEnums


class PandasTableModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    sigDataChanged = QtCore.Signal(object)
    defaultEmitDict = {
        "deleted": np.array([]),
        "changed": np.array([]),
        "added": np.array([]),
    }

    # Will be set in 'changeDefaultRows'
    dataframe: pd.DataFrame
    _defaultSeries: pd.Series

    def __init__(self, defaultSer: pd.Series, parent=None):
        super().__init__(parent)
        self.dataframe = pd.DataFrame()
        self.changeDefaultRows(defaultSer)
        self._nextRowId = 0

    def rowCount(self, parent=None):
        return self.dataframe.shape[0]

    def columnCount(self, parent=None):
        return self.dataframe.shape[1]

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            value = self.dataframe.iloc[index.row(), index.column()]
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return str(value)
            elif role == QtCore.Qt.ItemDataRole.EditRole:
                return value
        return None

    def setData(
        self,
        index: QtCore.QModelIndex,
        value: t.Any,
        role: int = QtCore.Qt.ItemDataRole,
    ) -> bool:
        super().setData(index, role)
        row = index.row()
        col = index.column()
        oldVal = self.dataframe.iat[row, col]
        # Try-catch for case of numpy arrays
        noChange = oldVal == value
        try:
            if noChange:
                return True
        except ValueError:
            # Happens with array comparison
            pass
        self.dataframe.iat[row, col] = value
        self.sigDataChanged.emit()
        return True

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if (
            orientation == QtCore.Qt.Orientation.Horizontal
            and role == QtCore.Qt.ItemDataRole.DisplayRole
        ):
            return self.dataframe.columns[section]

    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        return QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable

    def addDfRows(
        self, rowData: pd.DataFrame, addType=PrjEnums.ADD_TYPE_NEW, emitChange=True
    ):
        toEmit = self.defaultEmitDict.copy()
        if addType == PrjEnums.ADD_TYPE_NEW:
            # Treat all components as new -> set their IDs to guaranteed new values
            newIds = np.arange(
                self._nextRowId, self._nextRowId + len(rowData), dtype=int
            )
            rowData.set_index(newIds, inplace=True, verify_integrity=False)
            # For new data without all columns, add missing values to ensure they're
            # correctly filled
            if np.setdiff1d(rowData.columns, self.dataframe.columns).size > 0:
                rowData = self.makeDefaultDfRows(len(rowData), rowData)
        else:
            # Merge may have been performed with new components (id -1) mixed in
            needsUpdatedId = rowData.index == -1
            newIds = np.arange(
                self._nextRowId, self._nextRowId + np.sum(needsUpdatedId), dtype=int
            )
            rowData.index[needsUpdatedId] = newIds

        # Merge existing IDs and add new ones
        changedIdxs = np.isin(rowData.index, self.dataframe.index, assume_unique=True)
        changedIds = rowData.index[changedIdxs]
        addedIds = rowData.index[~changedIdxs]

        # Signal to table that rows should change
        self.layoutAboutToBeChanged.emit()
        # Ensure indices overlap with the components these are replacing
        self.dataframe.update(rowData)
        toEmit["changed"] = changedIds

        # Finally, add new components
        compsToAdd = rowData.loc[addedIds]
        self.dataframe = pd.concat((self.dataframe, compsToAdd), sort=False)
        toEmit["added"] = addedIds

        # Retain type information
        self._coerceDfTypes()

        self.layoutChanged.emit()

        self._nextRowId = np.max(self.dataframe.index.to_numpy(), initial=-1) + 1

        if emitChange:
            self.sigDataChanged.emit(toEmit)
        return toEmit

    def removeDfRows(self, idsToRemove: t.Sequence[int] = None, emitChange=True):
        if idsToRemove is None:
            idsToRemove = self.dataframe.index
        toEmit = self.defaultEmitDict.copy()
        # Generate ID list
        existingCompIds = self.dataframe.index
        idsToRemove = np.asarray(idsToRemove)

        # Do nothing for IDs not actually in the existing list
        idsActuallyRemoved = np.isin(idsToRemove, existingCompIds, assume_unique=True)
        if len(idsActuallyRemoved) == 0:
            return toEmit
        idsToRemove = idsToRemove[idsActuallyRemoved]

        tfKeepIdx = np.isin(
            existingCompIds, idsToRemove, assume_unique=True, invert=True
        )

        # Reset manager's component list
        self.layoutAboutToBeChanged.emit()
        self.dataframe = self.dataframe.iloc[tfKeepIdx, :]
        self.layoutChanged.emit()

        # Preserve type information after change
        self._coerceDfTypes()

        # Determine next ID for new components
        self._nextRowId = 0
        if np.any(tfKeepIdx):
            self._nextRowId = np.max(existingCompIds[tfKeepIdx].to_numpy()) + 1

        # Reflect these changes to the component list
        toEmit["deleted"] = idsToRemove
        if emitChange:
            self.sigDataChanged.emit(toEmit)

    def makeDefaultDfRows(self, numRows=1, initData: pd.DataFrame = None):
        """
        Create a dummy table populated with default values from the class default
        pd.Series. If `initData` is provided, it must have rows entries and
        correspond to columns from the default series. these columns will be overridden
        by the init data.
        """
        if numRows == 0:
            return pd.DataFrame(columns=self._defaultSeries.index)
        outDf = pd.DataFrame([self._defaultSeries] * numRows)
        if initData is not None:
            outDf.update(initData.set_index(outDf.index))
        return outDf

    def changeDefaultRows(self, defaultSer: pd.Series):
        self.beginResetModel()
        self._defaultSeries = defaultSer
        self.removeDfRows(self.dataframe.index)
        self.dataframe = self.makeDefaultDfRows(0)
        self.endResetModel()

    def _coerceDfTypes(self):
        """
        Pandas currently has a bug where datatypes are not preserved after update
        operations. Current workaround is to coerce all types to their original values
        after each operation
        """
        for ii, col in enumerate(self.dataframe.columns):
            idealType = type(self._defaultSeries[col])
            if not np.issubdtype(self.dataframe.dtypes[ii], idealType):
                try:
                    self.dataframe[col] = self.dataframe[col].astype(idealType)
                except (TypeError, ValueError):
                    continue
