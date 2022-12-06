# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numeric_online.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_NumericDisplay(object):
    def setupUi(self, NumericDisplay):
        if not NumericDisplay.objectName():
            NumericDisplay.setObjectName(u"NumericDisplay")
        NumericDisplay.resize(566, 851)
        self.verticalLayout = QVBoxLayout(NumericDisplay)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.float_precision = QComboBox(NumericDisplay)
        self.float_precision.setObjectName(u"float_precision")

        self.gridLayout.addWidget(self.float_precision, 0, 1, 1, 1)

        self.label_5 = QLabel(NumericDisplay)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(NumericDisplay)

        QMetaObject.connectSlotsByName(NumericDisplay)
    # setupUi

    def retranslateUi(self, NumericDisplay):
        NumericDisplay.setWindowTitle(QCoreApplication.translate("NumericDisplay", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("NumericDisplay", u"Float precision", None))
    # retranslateUi

