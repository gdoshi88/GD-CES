# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSACES_Quote_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication

from math import pi
import xlsxwriter
from datetime import datetime

import sqlite3  
import os
import traceback

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)





class Ui_Quote(object):
    def setupUi(self, Quote):
        Quote.setObjectName("Quote")
        Quote.resize(1041, 718)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Quote.sizePolicy().hasHeightForWidth())
        Quote.setSizePolicy(sizePolicy)
        Quote.setMinimumSize(QtCore.QSize(889, 515))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Script/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Quote.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(Quote)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Quote)
        self.groupBox.setMinimumSize(QtCore.QSize(861, 441))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.TableQuote = QtWidgets.QTableWidget(self.groupBox)
        self.TableQuote.setAlternatingRowColors(True)
        self.TableQuote.setObjectName("TableQuote")
        self.TableQuote.setColumnCount(12)
        self.TableQuote.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(41, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(42, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(43, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(44, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(45, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(46, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(47, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(48, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(49, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(50, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(51, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(52, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(53, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(54, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(55, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(56, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(57, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(58, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(59, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(60, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(61, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(62, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(63, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(64, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(65, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(66, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(67, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(68, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(69, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(70, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(71, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(72, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(73, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(74, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(75, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(76, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(77, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(78, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(79, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(80, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(81, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(82, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(83, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(84, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(85, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(86, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(87, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(88, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(89, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(90, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(91, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(92, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(93, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(94, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(95, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(96, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(97, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(98, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setVerticalHeaderItem(99, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableQuote.setHorizontalHeaderItem(11, item)
        self.TableQuote.horizontalHeader().setDefaultSectionSize(170)
        self.gridLayout.addWidget(self.TableQuote, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.Action = QtWidgets.QGroupBox(Quote)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Action.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Action.setFont(font)
        self.Action.setAutoFillBackground(True)
        self.Action.setObjectName("Action")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Action)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PB_Quote = QtWidgets.QPushButton(self.Action)
        self.PB_Quote.setMinimumSize(QtCore.QSize(181, 41))
        self.PB_Quote.setMaximumSize(QtCore.QSize(181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_Quote.setFont(font)
        self.PB_Quote.setObjectName("PB_Quote")
        self.gridLayout_2.addWidget(self.PB_Quote, 1, 0, 1, 1)
        self.PB_ClearContent = QtWidgets.QPushButton(self.Action)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_ClearContent.sizePolicy().hasHeightForWidth())
        self.PB_ClearContent.setSizePolicy(sizePolicy)
        self.PB_ClearContent.setMinimumSize(QtCore.QSize(181, 41))
        self.PB_ClearContent.setMaximumSize(QtCore.QSize(181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_ClearContent.setFont(font)
        self.PB_ClearContent.setObjectName("PB_ClearContent")
        self.gridLayout_2.addWidget(self.PB_ClearContent, 1, 2, 1, 1)
        self.PB_CopyPaste = QtWidgets.QPushButton(self.Action)
        self.PB_CopyPaste.setMinimumSize(QtCore.QSize(181, 41))
        self.PB_CopyPaste.setMaximumSize(QtCore.QSize(181, 41))
        self.PB_CopyPaste.setObjectName("PB_CopyPaste")
        self.gridLayout_2.addWidget(self.PB_CopyPaste, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.Action, 1, 0, 1, 1)

        self.retranslateUi(Quote)
        QtCore.QMetaObject.connectSlotsByName(Quote)

    def retranslateUi(self, Quote):
        _translate = QtCore.QCoreApplication.translate
        Quote.setWindowTitle(_translate("Quote", "Quote"))
        self.groupBox.setTitle(_translate("Quote", "Quotation Info :"))
        item = self.TableQuote.verticalHeaderItem(0)
        item.setText(_translate("Quote", "1"))
        item = self.TableQuote.verticalHeaderItem(1)
        item.setText(_translate("Quote", "2"))
        item = self.TableQuote.verticalHeaderItem(2)
        item.setText(_translate("Quote", "3"))
        item = self.TableQuote.verticalHeaderItem(3)
        item.setText(_translate("Quote", "4"))
        item = self.TableQuote.verticalHeaderItem(4)
        item.setText(_translate("Quote", "5"))
        item = self.TableQuote.verticalHeaderItem(5)
        item.setText(_translate("Quote", "6"))
        item = self.TableQuote.verticalHeaderItem(6)
        item.setText(_translate("Quote", "7"))
        item = self.TableQuote.verticalHeaderItem(7)
        item.setText(_translate("Quote", "8"))
        item = self.TableQuote.verticalHeaderItem(8)
        item.setText(_translate("Quote", "9"))
        item = self.TableQuote.verticalHeaderItem(9)
        item.setText(_translate("Quote", "10"))
        item = self.TableQuote.verticalHeaderItem(10)
        item.setText(_translate("Quote", "11"))
        item = self.TableQuote.verticalHeaderItem(11)
        item.setText(_translate("Quote", "12"))
        item = self.TableQuote.verticalHeaderItem(12)
        item.setText(_translate("Quote", "13"))
        item = self.TableQuote.verticalHeaderItem(13)
        item.setText(_translate("Quote", "14"))
        item = self.TableQuote.verticalHeaderItem(14)
        item.setText(_translate("Quote", "15"))
        item = self.TableQuote.verticalHeaderItem(15)
        item.setText(_translate("Quote", "16"))
        item = self.TableQuote.verticalHeaderItem(16)
        item.setText(_translate("Quote", "17"))
        item = self.TableQuote.verticalHeaderItem(17)
        item.setText(_translate("Quote", "18"))
        item = self.TableQuote.verticalHeaderItem(18)
        item.setText(_translate("Quote", "19"))
        item = self.TableQuote.verticalHeaderItem(19)
        item.setText(_translate("Quote", "20"))
        item = self.TableQuote.verticalHeaderItem(20)
        item.setText(_translate("Quote", "21"))
        item = self.TableQuote.verticalHeaderItem(21)
        item.setText(_translate("Quote", "22"))
        item = self.TableQuote.verticalHeaderItem(22)
        item.setText(_translate("Quote", "23"))
        item = self.TableQuote.verticalHeaderItem(23)
        item.setText(_translate("Quote", "24"))
        item = self.TableQuote.verticalHeaderItem(24)
        item.setText(_translate("Quote", "25"))
        item = self.TableQuote.verticalHeaderItem(25)
        item.setText(_translate("Quote", "26"))
        item = self.TableQuote.verticalHeaderItem(26)
        item.setText(_translate("Quote", "27"))
        item = self.TableQuote.verticalHeaderItem(27)
        item.setText(_translate("Quote", "28"))
        item = self.TableQuote.verticalHeaderItem(28)
        item.setText(_translate("Quote", "29"))
        item = self.TableQuote.verticalHeaderItem(29)
        item.setText(_translate("Quote", "30"))
        item = self.TableQuote.verticalHeaderItem(30)
        item.setText(_translate("Quote", "31"))
        item = self.TableQuote.verticalHeaderItem(31)
        item.setText(_translate("Quote", "32"))
        item = self.TableQuote.verticalHeaderItem(32)
        item.setText(_translate("Quote", "33"))
        item = self.TableQuote.verticalHeaderItem(33)
        item.setText(_translate("Quote", "34"))
        item = self.TableQuote.verticalHeaderItem(34)
        item.setText(_translate("Quote", "35"))
        item = self.TableQuote.verticalHeaderItem(35)
        item.setText(_translate("Quote", "36"))
        item = self.TableQuote.verticalHeaderItem(36)
        item.setText(_translate("Quote", "37"))
        item = self.TableQuote.verticalHeaderItem(37)
        item.setText(_translate("Quote", "38"))
        item = self.TableQuote.verticalHeaderItem(38)
        item.setText(_translate("Quote", "39"))
        item = self.TableQuote.verticalHeaderItem(39)
        item.setText(_translate("Quote", "40"))
        item = self.TableQuote.verticalHeaderItem(40)
        item.setText(_translate("Quote", "41"))
        item = self.TableQuote.verticalHeaderItem(41)
        item.setText(_translate("Quote", "42"))
        item = self.TableQuote.verticalHeaderItem(42)
        item.setText(_translate("Quote", "43"))
        item = self.TableQuote.verticalHeaderItem(43)
        item.setText(_translate("Quote", "44"))
        item = self.TableQuote.verticalHeaderItem(44)
        item.setText(_translate("Quote", "45"))
        item = self.TableQuote.verticalHeaderItem(45)
        item.setText(_translate("Quote", "46"))
        item = self.TableQuote.verticalHeaderItem(46)
        item.setText(_translate("Quote", "47"))
        item = self.TableQuote.verticalHeaderItem(47)
        item.setText(_translate("Quote", "48"))
        item = self.TableQuote.verticalHeaderItem(48)
        item.setText(_translate("Quote", "49"))
        item = self.TableQuote.verticalHeaderItem(49)
        item.setText(_translate("Quote", "50"))
        item = self.TableQuote.verticalHeaderItem(50)
        item.setText(_translate("Quote", "51"))
        item = self.TableQuote.verticalHeaderItem(51)
        item.setText(_translate("Quote", "52"))
        item = self.TableQuote.verticalHeaderItem(52)
        item.setText(_translate("Quote", "53"))
        item = self.TableQuote.verticalHeaderItem(53)
        item.setText(_translate("Quote", "54"))
        item = self.TableQuote.verticalHeaderItem(54)
        item.setText(_translate("Quote", "55"))
        item = self.TableQuote.verticalHeaderItem(55)
        item.setText(_translate("Quote", "56"))
        item = self.TableQuote.verticalHeaderItem(56)
        item.setText(_translate("Quote", "57"))
        item = self.TableQuote.verticalHeaderItem(57)
        item.setText(_translate("Quote", "58"))
        item = self.TableQuote.verticalHeaderItem(58)
        item.setText(_translate("Quote", "59"))
        item = self.TableQuote.verticalHeaderItem(59)
        item.setText(_translate("Quote", "60"))
        item = self.TableQuote.verticalHeaderItem(60)
        item.setText(_translate("Quote", "61"))
        item = self.TableQuote.verticalHeaderItem(61)
        item.setText(_translate("Quote", "62"))
        item = self.TableQuote.verticalHeaderItem(62)
        item.setText(_translate("Quote", "63"))
        item = self.TableQuote.verticalHeaderItem(63)
        item.setText(_translate("Quote", "64"))
        item = self.TableQuote.verticalHeaderItem(64)
        item.setText(_translate("Quote", "65"))
        item = self.TableQuote.verticalHeaderItem(65)
        item.setText(_translate("Quote", "66"))
        item = self.TableQuote.verticalHeaderItem(66)
        item.setText(_translate("Quote", "67"))
        item = self.TableQuote.verticalHeaderItem(67)
        item.setText(_translate("Quote", "68"))
        item = self.TableQuote.verticalHeaderItem(68)
        item.setText(_translate("Quote", "69"))
        item = self.TableQuote.verticalHeaderItem(69)
        item.setText(_translate("Quote", "70"))
        item = self.TableQuote.verticalHeaderItem(70)
        item.setText(_translate("Quote", "71"))
        item = self.TableQuote.verticalHeaderItem(71)
        item.setText(_translate("Quote", "72"))
        item = self.TableQuote.verticalHeaderItem(72)
        item.setText(_translate("Quote", "73"))
        item = self.TableQuote.verticalHeaderItem(73)
        item.setText(_translate("Quote", "74"))
        item = self.TableQuote.verticalHeaderItem(74)
        item.setText(_translate("Quote", "75"))
        item = self.TableQuote.verticalHeaderItem(75)
        item.setText(_translate("Quote", "76"))
        item = self.TableQuote.verticalHeaderItem(76)
        item.setText(_translate("Quote", "77"))
        item = self.TableQuote.verticalHeaderItem(77)
        item.setText(_translate("Quote", "78"))
        item = self.TableQuote.verticalHeaderItem(78)
        item.setText(_translate("Quote", "79"))
        item = self.TableQuote.verticalHeaderItem(79)
        item.setText(_translate("Quote", "80"))
        item = self.TableQuote.verticalHeaderItem(80)
        item.setText(_translate("Quote", "81"))
        item = self.TableQuote.verticalHeaderItem(81)
        item.setText(_translate("Quote", "82"))
        item = self.TableQuote.verticalHeaderItem(82)
        item.setText(_translate("Quote", "83"))
        item = self.TableQuote.verticalHeaderItem(83)
        item.setText(_translate("Quote", "84"))
        item = self.TableQuote.verticalHeaderItem(84)
        item.setText(_translate("Quote", "85"))
        item = self.TableQuote.verticalHeaderItem(85)
        item.setText(_translate("Quote", "86"))
        item = self.TableQuote.verticalHeaderItem(86)
        item.setText(_translate("Quote", "87"))
        item = self.TableQuote.verticalHeaderItem(87)
        item.setText(_translate("Quote", "88"))
        item = self.TableQuote.verticalHeaderItem(88)
        item.setText(_translate("Quote", "89"))
        item = self.TableQuote.verticalHeaderItem(89)
        item.setText(_translate("Quote", "90"))
        item = self.TableQuote.verticalHeaderItem(90)
        item.setText(_translate("Quote", "91"))
        item = self.TableQuote.verticalHeaderItem(91)
        item.setText(_translate("Quote", "92"))
        item = self.TableQuote.verticalHeaderItem(92)
        item.setText(_translate("Quote", "93"))
        item = self.TableQuote.verticalHeaderItem(93)
        item.setText(_translate("Quote", "94"))
        item = self.TableQuote.verticalHeaderItem(94)
        item.setText(_translate("Quote", "95"))
        item = self.TableQuote.verticalHeaderItem(95)
        item.setText(_translate("Quote", "96"))
        item = self.TableQuote.verticalHeaderItem(96)
        item.setText(_translate("Quote", "97"))
        item = self.TableQuote.verticalHeaderItem(97)
        item.setText(_translate("Quote", "98"))
        item = self.TableQuote.verticalHeaderItem(98)
        item.setText(_translate("Quote", "99"))
        item = self.TableQuote.verticalHeaderItem(99)
        item.setText(_translate("Quote", "100"))
        item = self.TableQuote.horizontalHeaderItem(0)
        item.setText(_translate("Quote", "Part Number"))
        item = self.TableQuote.horizontalHeaderItem(1)
        item.setText(_translate("Quote", "Price Break 1"))
        item = self.TableQuote.horizontalHeaderItem(2)
        item.setText(_translate("Quote", "Price Break 2"))
        item = self.TableQuote.horizontalHeaderItem(3)
        item.setText(_translate("Quote", "Price Break 3"))
        item = self.TableQuote.horizontalHeaderItem(4)
        item.setText(_translate("Quote", "Price Break 4"))
        item = self.TableQuote.horizontalHeaderItem(5)
        item.setText(_translate("Quote", "Price Break 5"))
        item = self.TableQuote.horizontalHeaderItem(6)
        item.setText(_translate("Quote", "Price Break 6"))
        item = self.TableQuote.horizontalHeaderItem(7)
        item.setText(_translate("Quote", "Price Break 7"))
        item = self.TableQuote.horizontalHeaderItem(8)
        item.setText(_translate("Quote", "Price Break 8"))
        item = self.TableQuote.horizontalHeaderItem(9)
        item.setText(_translate("Quote", "Price Break 9"))
        item = self.TableQuote.horizontalHeaderItem(10)
        item.setText(_translate("Quote", "Price Break 10"))
        item = self.TableQuote.horizontalHeaderItem(11)
        item.setText(_translate("Quote", "Mat Change"))
        self.Action.setTitle(_translate("Quote", "Action"))
        self.PB_Quote.setText(_translate("Quote", "Validate Quote"))
        self.PB_ClearContent.setText(_translate("Quote", "Clear Content"))
        self.PB_CopyPaste.setText(_translate("Quote", "Paste"))



#============================================================================  
def printError(ex):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    traceback.print_exc()        
        
conn = sqlite3.connect("db_Synoptic")
cur = conn.cursor()


def trouvercout(group,Diam):
    if group == "B":
        if Diam <= 0.188 :
            return "SUB","DG1B"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUB","DG2B"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUB","DG3B"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUB","DG4B"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUB","DG5B"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUB","DG6B"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUB","DG7B"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUB","DG8B"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUB","DG9B"
        elif Diam > 1.125:
            return "SUB","DG10B"
    elif group == "C":
        if Diam <= 0.188 :
            return "SUC","DG1C"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUC","DG2C"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUC","DG3C"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUC","DG4C"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUC","DG5C"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUC","DG6C"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUC","DG7C"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUC","DG8C"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUC","DG9C"
        elif Diam > 1.125:
            return "SUC","DG10C"
    elif group == "D":
        if Diam <= 0.188 :
            return "SUD","DG1D"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUD","DG2D"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUD","DG3D"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUD","DG4D"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUD","DG5D"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUD","DG6D"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUD","DG7D"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUD","DG8D"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUD","DG9D"
        elif Diam > 1.125:
            return "SUD","DG10D"
    elif group == "E":
        if Diam <= 0.188 :
            return "SUE","DG1E"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUE","DG2E"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUE","DG3E"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUE","DG4E"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUE","DG5E"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUE","DG6E"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUE","DG7E"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUE","DG8E"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUE","DG9E"
        elif Diam > 1.125:
            return "SUE","DG10E"
    elif group == "F":
        if Diam <= 0.188 :
            return "SUF","DG1F"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUF","DG2F"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUF","DG3F"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUF","DG4F"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUF","DG5F"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUF","DG6F"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUF","DG7F"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUF","DG8F"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUF","DG9F"
        elif Diam > 1.125:
            return "SUF","DG10F" 

# Classe permettant l'affichage de la fenetre

class VueQuote(QtWidgets.QDialog,Ui_Quote):

    def __init__(self, parent):
        super(VueQuote, self).__init__(parent)
        self.setupUi(self)  
        self.PB_ClearContent.clicked.connect(self.PBClearContent)
        self.PB_Quote.clicked.connect(self.PBQuote)
        
        self.copy = 0
        self.currentrow = 0
        self.currentcolumn = 0
        
        

# COMPLETERS        
        cur.execute("SELECT PartNumber FROM Part ORDER BY PartNumber ASC")
        part = cur.fetchall()
        
        listpart = []
        for prt in part:
            for p in prt:
                listpart.append(str(p))  
        cmpt = QCompleter(listpart) 
        cmpt.setCaseSensitivity(0)
        
        for index in range(100):
            new = QLineEdit()
            new.setCompleter(cmpt)
            self.TableQuote.setCellWidget(index,0, new)
 

        self.PB_CopyPaste.clicked.connect(self.clipboardChanged)
        self.TableQuote.cellClicked.connect(self.junkStuff)
        
    def junkStuff(self):
        bb = self.TableQuote.currentColumn()
        print("bb, current column: ", bb)
        self.currentcolumn = bb
        a = self.TableQuote.currentRow()
        a = int(a)
        print("a, current row: ", a)
        self.currentrow = a
        
        self.TableQuote.clearContents()
        self.TableQuote.setCurrentCell(a, bb)
        
                        
            
   # Get the system clipboard contents
    def clipboardChanged(self):
        
        self.copy = 1
        
        self.TableQuote.clearContents()

#        a = self.TableQuote.currentRow()
#        a = int(a)
#        print("a, current row: ", a)
        a = self.currentrow
        print("self.currentrow: ", a)
        b = self.currentcolumn
        print("self.currentcolumn: ", b)
        
        text = QApplication.clipboard().text()  
        textl = text.split('\n')
        print("text copied: ", text)
        n = 0 
        while n <= len(textl)-1:
            
            ##\t is a tab
            textc = textl[n].split('\t')
            print("textc split tab: ", textc)
                       
            i = 0 
            while i <=len(textc)-1:
                
                a1 = str(textc[i])
                a1 = QtWidgets.QTableWidgetItem(a1)
                ##setItem(int row, int column, item)
                self.TableQuote.setItem(n+a,i+b,a1)               
                i = i + 1            
            n = n + 1
    
    def PBClearContent(self):
        
        self.TableQuote.clearContents()
        
        self.copy = 0
        
        cur.execute("SELECT PartNumber FROM Part ORDER BY PartNumber ASC")
        part = cur.fetchall()
        
        listpart = []
        for prt in part:
            for p in prt:
                listpart.append(str(p))  
        cmpt = QCompleter(listpart) 
        cmpt.setCaseSensitivity(0)
        
        for index in range(100):
            new = QLineEdit()
            new.setCompleter(cmpt)
            self.TableQuote.setCellWidget(index,0, new)
        
    def PBQuote(self):
        
        try : 
            
            ligne = 0
            while ligne <= 99 :
                
                if self.copy == 0 : 
                    partnumber = self.TableQuote.cellWidget(ligne,0).text()
                    
                elif self.copy == 1 :
                    partnumber = self.TableQuote.item(ligne,0).text()
                
                if partnumber == "" or partnumber == None : 
                    break
                else :
                    cur.execute("SELECT Description FROM Part WHERE PartNumber = ?",(partnumber,))
                    desc = cur.fetchone()
                    
                    if desc == None:
                        QMessageBox.warning(self, "Warning", "Part Number : "+partnumber+" is unknown, please add this new part before quoting.")
                        return
                    
                    ligne = ligne + 1
        except : 
            QMessageBox.warning(self, "Warning", "Error during treatment of the part number entered.")
            return
        
        
        e = datetime.now()
        e = str(e.month)+"-"+str(e.day)+"-"+str(e.year)+"--"+str(e.hour)+"h-"+str(e.minute)+"m"
                
        titleexport = 'ExportQuote '+str(e)+'.xlsx'
        
        try : 
            desktoppath = os.path.join(os.path.expanduser("~"), "Desktop")
        except : 
            QMessageBox.warning(self, "Warning", "Could not find desktop path.")
            return    
        
        ##Define save path for .XLSX file name saved in titleexport variable
        try:
#            way = str(desktoppath)+"/Export-CES/"+str(titleexport)   ### Slashes are wrong way in previous version for filepath
            way = str(desktoppath)+"\\Export-CES\\"+str(titleexport)

            workbook = xlsxwriter.Workbook(way)
        except :
            print("desktoppatherror")
        
        
        ### Create desktop folder "Export-CES" if it does not exist
        try:
            folder = str(desktoppath)+"\\Export-CES"
            if not os.path.exists(folder):
                os.makedirs(folder)
        except:
            QMessageBox.warning(self, "Warning", "Could not create folder 'Export-CES' on Desktop.")

#        feuillebase = workbook.add_worksheet('Recap')
#        feuillebase.set_column('A:K', 20)
        
#        feuillebase.write(1,3,'Total Gross Income :')
        
#        feuillebase.write(4,0,'Part Number :')
   
        newrawmat = 0
        ligne = 0
        while ligne <= 99 :
            
            try :
                if self.copy == 0 : 
                    partnumber = self.TableQuote.cellWidget(ligne,0).text()
                    
                elif self.copy == 1 :
                    partnumber = self.TableQuote.item(ligne,0).text()
                
                if partnumber == "" or partnumber == None : 
                    break
            except :
                
                QMessageBox.warning(self, "Warning", "Error (2.2) while proccessing the Part number.")
                    

            #MAT CHANGE
            try :  
                newrawmat = self.TableQuote.item(ligne,11).text()
            except :
                newrawmat = 0
    
#            feuillebase.write(ligne+5,0,partnumber)
            
            try :
                feuille = workbook.add_worksheet(partnumber)               
            except : 
                feuille = workbook.add_worksheet("NV PN")
            
            
            feuille.set_column('A:K', 20)
        
            feuille.write(4,0,'Part Number :')
            feuille.write(5,0,'Revision :')
            feuille.write(6,0,'Description :')
            feuille.write(7,0,'Mfg. Spec. :')
            feuille.write(8,0,'Notes :')
            feuille.write(13,0,'Operations :')
            feuille.write(4,3,'Material :')
            feuille.write(5,3,'Matl Cost :')
            feuille.write(6,3,'Diameter :')
            feuille.write(7,3,'Part Weight :')
            feuille.write(9,3,'Req Qty :')
            feuille.write(10,3,'Scrap Qty :')
            feuille.write(11,3,'Total Qty :')
            feuille.write(4,6,'Slug Lenght :')
            feuille.write(5,6,'Hd. Vol Len :')
            feuille.write(6,6,'Shank Lenght :')
                
            feuille.write(0,0,'Export :')
                
            feuille.write(2,0,'Date of the Quote :' + e +".")
            
            try : #####################################################
                colonne = 1
                while colonne <= 10:

                    try :
                        qty = int(self.TableQuote.item(ligne,colonne).text())
                    except :
                        break
                    






                    cur.execute("SELECT Material, Diam, Shank, Op1, Op2, Op3, Op4, Op5, Op6, Op7, Op8, Op9, Op10, Op11, Op12, Op13, Op14, Op15, Op16, Op17, Op18, Op19, Op20, Op21, Op22, Op23, Op24, Op25, Op26, Op27, Op28, Op29, Op30, Op31, Op32, Op33, Op34,Op35, Op36, Op37, Op38, Op39, Op40 FROM Part WHERE PartNumber = ?", (partnumber,))
                    Part = cur.fetchone()
                    
                    mat = str(Part[0])
                    
                    diam = Part[1]
                    shank = Part[2]
            
                    op = list()        
                    n = 3 
                    while n <= 43:        
                        operation = Part[n]           
                        if operation == 0 or operation == "":
                            break
                        else:
                            op.append(operation)           
                        n = n+1
                        
                    cur.execute("SELECT Type,Groupe,Cost FROM Mat WHERE Number = ?",(mat,))
                    Mat = cur.fetchone()
                    
                    try:    
                        mattype = str(Mat[0])
                        matgroupe = str(Mat[1])
                        matcost = Mat[2]
                    except Exception as ex :
                        printError(ex)
                        message = "Material number: " + mat + " is missing."
                        QMessageBox.warning(self, "Warning", message)

                    #Equations per Jean-Paul Nicolle
                    # if cost > 100
                    if matcost >= 100:
                        scrap = int (25 + (qty + 25) * 0.062)
                    elif matcost >= 22:
                        # if cost > 22
                        scrap = int(40 + (qty + 40) * 0.062)
                    else:
                        #Original synoptic is 40, this is more conservative per JP
                        scrap = int(56 + ((qty + 56) * 0.062))
                    
                    if newrawmat != None and newrawmat != 0 :
                        matcost = int(newrawmat)
                    
                    setupcost,cost = trouvercout(matgroupe,diam)     
    
                    Opname = list()
                    Opmin = list()
                    Opunit = list()
                    Opsetup = list()
                    Opcost = list()
                      
                    n = 0
                    while n <= len(op)-1 :
                        
                        pn = str(op[n])
                        try : 
                            cur.execute("SELECT Name, Min, Unit,%s,%s FROM Op WHERE Number = ?" %(setupcost,cost),(pn,))
                            Op = cur.fetchone()
                            
                            Opname.append(Op[0])
                            if Op[1] == "":
                                Opmin.append(0)
                            else :
                                Opmin.append(Op[1])
                            Opunit.append(Op[2])
                            if Op[3] == "":
                                Opsetup.append(Op[3])
                            else :
                                Opsetup.append(Op[3])
                                
                            Opcost.append(Op[4])
                        except: 
                            n = n + 1
                        
                        n = n + 1

            #cout = cost

            # Calcul du cout de Set Up par piece
            # Calculating the cost of Set Up per piece
                    try:
                        SETUP = sum(Opsetup)/qty
                        
                        SETUP = round(SETUP,3)
                
                
                # Calcul du Head Vol
                        
                        HDVOL = diam * 2.2
                        
                        HDVOL = round(HDVOL,3)
                
                # Calcul du Slug Lenght 
                        
                        SLUG = HDVOL + shank
                        
                        SLUG = round(SLUG,3)
                        
                        
                # Calcul du Part Weight
                        
                        if mattype == "Steel" or mattype == "NiBase" :
                            
                            PW = (pi*((diam*diam)/4)*SLUG)*0.3
                                    
                        elif mattype == "Titan" :
                            
                            PW = (pi*((diam*diam)/4)*SLUG)*0.17
                            
                        elif mattype == "Alum" :
                            
                            PW = (pi*((diam*diam)/4)*SLUG)*0.2
                            
                        PW = round(PW,3)
                    except:
                        print("Error G")

            # creation de la liste de cout et calcul du subtotal
            
            ###
            #Scrap process cost is 0 if the cost/pc * qty is < minimum lot
            #the minimum lot already includes padding for scrap processing cost.
                    SCRAPPROCBOOL = False
                    try:
                        listprocess = list()
                        coutprocess = 0
    
                        n = 0 
                        while n <= len(op)-1 :
                        
                            setup = Opsetup[n]
                            setup = setup/qty
                            
                            unit = str(Opunit[n])
                            if unit == "pc" :
                                
                                cost = Opcost[n]
                                
                            elif unit == "lb":
                                print("PW: ", PW)
                                cost = Opcost[n]
                                cost = cost * PW
                                
                            minimumlot = Opmin[n]
                            minimumlot = minimumlot/qty
                            opmin = Opmin[n]
                            # print("setup: ", setup)
                            # print("cost : ", cost)  # THIS IS $COST / PART
                            # print("coutprocess: ", coutprocess)
                            # print("minimumlot: ", minimumlot)
                            # print(cost, "*", qty,"<",opmin, " = ",(cost * qty) <= opmin)
                            if ((cost * qty) <= opmin):
                                SCRAPPROCBOOL = True
                            else:
                                SCRAPPROCBOOL = False
                            
                            if setup > cost :
                                coutprocess = setup
                                # print("a setup: ", setup)
                            else : 
                                coutprocess = cost
                                # print("b cost: ", cost)
                            
                            if coutprocess > minimumlot:
                                # print("c coutprocess: ", coutprocess)
                                coutprocess = coutprocess 
                            else : 
                                coutprocess = minimumlot
                                # print("d minimum lot: ", minimumlot)
                            
                            if Opcost[n] == 0:
                                # print("e")
                                coutprocess = 0
                            
                            listprocess.append(coutprocess)
                            print("listprocess: ", listprocess)
                            print("SCRPPROCBOOL", SCRAPPROCBOOL)
                            n = n+1
                    except:
                        print("Error F")
                        
                    try: 
                        SUBTOTAL = sum(listprocess)
                        
                        SUBTOTAL = round(SUBTOTAL,3)
    
                # Calcul Raw mateiral cost per piece
    
                        RAWMATCOST = PW * matcost
    
                        RAWMATCOST = round(RAWMATCOST,3)
            
                # Calcul du scrap allowance material cost per piece
                        # PW = part weight
                        # scrap = scrap quantity
                        # matcost = $dollars / pound
                        # qty = quantity ordered/ desired
                        SCRAPMATCOST = (((PW * scrap)*matcost)/qty)
                        print("Scrapmatcost: ", SCRAPMATCOST)
                        SCRAPMATCOST = round(SCRAPMATCOST,3)
    
                # Calcul du scrap allowance processus cost per piece   
                        #
                        #SCRAPPROCCOST = 0 IF QTY * COST/PC < MIN LOT COST ######################
                        SCRAPPROCCOST = (((SUBTOTAL * 0.5)*scrap)/qty)
                        print("Scrap process cost: ", SCRAPPROCCOST)
                        print("SUBTOTAL: ", SUBTOTAL)
                        print("scrap: ", scrap)
                        print("qty: ", qty)
                        SCRAPPROCCOST = round(SCRAPPROCCOST,3)

                        #If for every part qty order * cost/piece (or cost / lb) is <= minimum lot cost then
                        #scrap process cost is $0 as it scrap prcoess allowance is already factored into minimum lot costs
                        if(SCRAPPROCBOOL):
                            SCRAPPROCCOST = 0
                            
                # calcul de la perte de matiere 
    
                        qtytotal = qty + scrap
                        
                        longueurtotal = (SLUG + 0.04) * qtytotal
                        
                        nbbar = longueurtotal / 144 
                        
                        nbbartotal = int(nbbar)+1
                        
                        nbbarperdu = nbbartotal - nbbar 
                        
                        longueurperdu = (nbbarperdu * 144) + ( scrap * 0.04 )
                        
                        if mattype == "Steel" or mattype == "NiBase" :
                            
                            lossw = (pi*((diam*diam)/4)*longueurperdu)*0.3
                                    
                        elif mattype == "Titan" :
                            
                            lossw = (pi*((diam*diam)/4)*longueurperdu)*0.17
                            
                        elif mattype == "Alum" :
                            
                            lossw = (pi*((diam*diam)/4)*longueurperdu)*0.2
                            
                        lossw = round(lossw,3)
                        
                        LOSS = (lossw * matcost) / qtytotal
                        
                        LOSS = round(LOSS,3)
                    except:
                        print("Error E")
            # Calcul du cout final 
                    try:
                        TOTAL = SUBTOTAL + SETUP + RAWMATCOST + SCRAPMATCOST + SCRAPPROCCOST + LOSS
                        
                        TOTAL= round(TOTAL,3)
                        
                        Miscellaneous = TOTAL * 0.10
                        
                        TOTALMFG = TOTAL + Miscellaneous

                        MINCOSTVALUE = 5000 #Per Mike Ross 1/11/2019
                        MARGE = 30
    
                        
                        PRX = TOTALMFG/((100-MARGE)/100)
                        Finalresult = PRX * qty
        
                        if Finalresult < MINCOSTVALUE :
        
                            while Finalresult <= MINCOSTVALUE :
                                
                                MARGE = MARGE + 1
                                PRX = TOTALMFG/((100-MARGE)/100)
                                Finalresult = PRX * qty
        
                        feuille.write(9,(3+colonne),qty)
                        feuille.write(10,(3+colonne),scrap)
                        feuille.write(11,(3+colonne),qtytotal)
                        
                        ii = 0
                        while ii <= len(listprocess)-1 :
                            
                            k = int(ii)
                            feuille.write((13+k),(3+colonne),listprocess[ii])
                            
                            ii = ii+1
                        
                        if colonne == 1 :
                            lettre = "E"
                        elif colonne == 2 :
                            lettre = "F"
                        elif colonne == 3 :
                            lettre = "G"
                        elif colonne == 4 :
                            lettre = "H"
                        elif colonne == 5 :
                            lettre = "I"
                        elif colonne == 6 :
                            lettre = "J"
                        elif colonne == 7 :
                            lettre = "K"
                        elif colonne == 8 :
                            lettre = "L"
                        elif colonne == 9 :
                            lettre = "M"
                        elif colonne == 10 :
                            lettre = "N"
                        elif colonne == 11 :
                            lettre = "O"
                    except:
                        print("error D")
                    try:
                        debut = str(lettre+'14')
                        long = str(14 + k)
                        fin = str(lettre+long)
                        dtot = str(14+k+2)
                        ftot = str(14+k+7)
                        debuttot = str(lettre+dtot)
                        fintot = str(lettre+ftot)
                        stot = str(14+k+8)
                        supertot = str(lettre+stot)
                        mfgtot = str(14+k+9)
                        mfgtotal = str(lettre+mfgtot)           
                        mrg = str(14+k+10)
                        mrgtot = str(lettre+mrg)
                        prx = str(14+k+11)
                        prxtot = str(lettre+prx)
                    except:
                        print("error C")
                    try:
                        feuille.write((13+k+2),(3+colonne),'=SUM(%s:%s)'%(debut,fin))
                        feuille.write((13+k+3),(3+colonne),SETUP)
                        feuille.write((13+k+4),(3+colonne),RAWMATCOST)
                        feuille.write((13+k+5),(3+colonne),SCRAPMATCOST)
                        feuille.write((13+k+6),(3+colonne),SCRAPPROCCOST)
                        feuille.write((13+k+7),(3+colonne),LOSS)
                        feuille.write((13+k+8),(3+colonne),'=SUM(%s:%s)'%(debuttot,fintot))
                        feuille.write((13+k+9),(3+colonne),'=%s*1.1'%(supertot))
                        feuille.write((13+k+10),(3+colonne),MARGE)
                        feuille.write((13+k+11),(3+colonne),'=%s/((100-%s)/100)'%(mfgtotal,mrgtot))
                        feuille.write((13+k+12),(3+colonne),'=(%s*%s)'%(prxtot,qty))
                    except:
                        print("error b")
                    
    #                aa = colonne
    #                bb = colonne+1
    #                cc = colonne+2
    #                dd = colonne+3
    #                feuillebase.write(4,(aa+(4*(colonne-1))),'Req Qty :')
    #                feuillebase.write(4,(bb+(4*(colonne-1))),'Cost :')
    #                feuillebase.write(4,(cc+(4*(colonne-1))),'Marge (%) :')
    #                feuillebase.write(4,(dd+(4*(colonne-1))),'Price :')
                    
    #                feuillebase.write(ligne+5,(aa+(4*(colonne-1))),qty)
     #               feuillebase.write(ligne+5,(bb+(4*(colonne-1))),TOTALMFG)
    #                feuillebase.write(ligne+5,(cc+(4*(colonne-1))),'30')
    #                feuillebase.write(ligne+5,(dd+(4*(colonne-1))),TOTALMFG*1.3)
    
                    colonne = colonne+1
            except TypeError as ex:
                printError(ex)
                QMessageBox.warning(self, "Warning", "Type Error (2.3) in the computation process.")                
                
                
            except Exception as ex :
                printError(ex)
                QMessageBox.warning(self, "Warning", "Error (2.3) in the computation process.")
                
                
            try:
                feuille.write((13+k+2),3,'Subtotal process :')  
                feuille.write((13+k+3),3,'Set up cost:') 
                feuille.write((13+k+4),3,'Raw Matl cost:') 
                feuille.write((13+k+5),3,'Scrap Matl cost :') 
                feuille.write((13+k+6),3,'Scrap Process cost :') 
                feuille.write((13+k+7),3,'Matl Loss cost :') 
                feuille.write((13+k+8),3,'Total:') 
                feuille.write((13+k+9),3,'Total Mfg:') 
                feuille.write((13+k+10),3,'Marge ( % ):') 
                feuille.write((13+k+11),3,'Price:') 
                feuille.write((13+k+12),3,'Total Value:') 
            except:
                print("exception a")
            
            ##Example SS5211-4H10 IS PART NUMBER
            ##PART[4] = 114 (MATERIAL)
            
            ##ON MAT TABLE THERE IS NO NUMBER 114
            
            cur.execute("SELECT Rev, Description, MfgSpec, Note, Material, Shank FROM Part WHERE PartNumber = ?",(partnumber,))
            part = cur.fetchone()
            
            cur.execute("SELECT Name, Spec FROM Mat WHERE Number = ?",(part[4],))
            matdescription = cur.fetchone()
            
            
            try:
                print("matdescription: ", matdescription)
                print("matdescription[0]", matdescription[0])
                print("matdescription[1]", matdescription[1])
                
                matnamespec = str(matdescription[0])+"--"+str(matdescription[1])
            except TypeError as ex:
                printError(ex)
                
                message = "Error relates to: " + str(part[4]) + " part number: " + str(partnumber)
                QMessageBox.warning(self, "warning", message)
            
            except Exception as ex:
                printError(ex)
                QMessageBox.warning(self, "Warning", message)

            
            feuille.write(4,1,partnumber)
            feuille.write(5,1,part[0])
            feuille.write(6,1,part[1])
            feuille.write(7,1,part[2])
            feuille.write(8,1,part[3])
            feuille.write(4,4,matnamespec)
            feuille.write(5,4,matcost)
            feuille.write(6,4,diam)
            feuille.write(7,4,PW)
            feuille.write(4,7,SLUG)
            feuille.write(5,7,HDVOL)
            feuille.write(6,7,part[5])
            
            i = 0
            while i <= len(Opname)-1 :
                
                k = int(i)
                feuille.write((13+k),1,Opname[i])

                i = i+1

            ligne = ligne+1         
        
        try :
            workbook.close()
            ##This line will not trigger if above line is not executed successfully
            QMessageBox.about(self, "Confimation", "Your quote has been saved.")
        except IOError as e:
            QMessageBox.warning(self, "Warning", "I/O error({0}): {1}".format(e.errno, e.strerror) )
            print("I/O error({0}): {1}".format(e.errno, e.strerror) )
        except : 
            QMessageBox.warning(self, "Warning", "Cannot save Excel quote.")
            return

        
        
        
        
        #file = r"\\fpserver\Departments\Software\MSACostEstimatingSystem\MSACES-beta\ExportQuote.xlsx"
        file = way
        os.startfile(file)
        
        return
        
