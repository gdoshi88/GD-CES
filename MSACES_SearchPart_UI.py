# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSACES_SearchPart.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

##09/19/19 - Added ability to delete part

##10/2/19 - Remove GoToPart, remove links to VueNewPartFilled and replace with VueEditPartFilled
##10/3/19 - Split up UI and controller functions of SearchPart into SearchPart.py
from PyQt5 import QtCore, QtGui, QtWidgets

# import MSACES ##This needs to be eliminated or circular referene will occur in MSACES_SearchPart.py


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

class Ui_SearchPartNumber(object):
    def setupUi(self, SearchPartNumber):
        SearchPartNumber.setObjectName("SearchPartNumber")
        SearchPartNumber.resize(778, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchPartNumber.sizePolicy().hasHeightForWidth())
        SearchPartNumber.setSizePolicy(sizePolicy)
        SearchPartNumber.setMinimumSize(QtCore.QSize(778, 118))
        SearchPartNumber.setMaximumSize(QtCore.QSize(778, 118))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchPartNumber.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SearchPartNumber)
        self.gridLayout.setObjectName("gridLayout")
        self.PB_GoToPart = QtWidgets.QPushButton(SearchPartNumber)
        self.PB_GoToPart.setMinimumSize(QtCore.QSize(202, 40))
        self.PB_GoToPart.setMaximumSize(QtCore.QSize(202, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PB_GoToPart.setFont(font)
        self.PB_GoToPart.setObjectName("PB_GoToPart")
        self.gridLayout.addWidget(self.PB_GoToPart, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(SearchPartNumber)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LE_SearchPartNumber = QtWidgets.QLineEdit(SearchPartNumber)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_SearchPartNumber.sizePolicy().hasHeightForWidth())
        self.LE_SearchPartNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LE_SearchPartNumber.setFont(font)
        self.LE_SearchPartNumber.setObjectName("LE_SearchPartNumber")
        self.gridLayout.addWidget(self.LE_SearchPartNumber, 0, 1, 1, 1)

        ##manually add
        # self.PB_GoToEditPart = QtWidgets.QPushButton(SearchPartNumber)
        # self.PB_GoToEditPart.setMinimumSize(QtCore.QSize(202, 40))
        # self.PB_GoToEditPart.setMaximumSize(QtCore.QSize(202, 40))
        # self.PB_GoToEditPart.setFont(font)
        # self.PB_GoToEditPart.setObjectName("PB_GoToEditPart")
        # self.gridLayout.addWidget(self.PB_GoToEditPart, 1, 2, 1, 1)

        self.PB_DeletePart = QtWidgets.QPushButton(SearchPartNumber)
        self.PB_DeletePart.setMinimumSize(QtCore.QSize(202, 40))
        self.PB_DeletePart.setMaximumSize(QtCore.QSize(202, 40))
        self.PB_DeletePart.setFont(font)
        self.PB_DeletePart.setObjectName("PB_DeletePart")
        self.gridLayout.addWidget(self.PB_DeletePart, 1, 3, 1, 1)





        self.retranslateUi(SearchPartNumber)
        QtCore.QMetaObject.connectSlotsByName(SearchPartNumber)
        
       
        
        
        
    def retranslateUi(self, SearchPartNumber):
        _translate = QtCore.QCoreApplication.translate
        SearchPartNumber.setWindowTitle(_translate("SearchPartNumber", "Search Part Number"))
        self.PB_GoToPart.setText(_translate("SearchPartNumber", "Edit or Copy Part"))
        self.label.setText(_translate("SearchPartNumber", "Enter the Part Number :"))
        # self.PB_GoToEditPart.setText(_translate("SearchPartNumber", "Edit Part"))
        self.PB_DeletePart.setText(_translate("SearchPartNumber", "Delete Part"))


