# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSACES_ViewPart_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
from math import pi
from MSACES import *

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

class Ui_NewPart(object):
    def setupUi(self, NewPart):
        NewPart.setObjectName("NewPart")
        NewPart.resize(962, 597)
        NewPart.setMinimumSize(QtCore.QSize(962, 597))
        NewPart.setMaximumSize(QtCore.QSize(962, 597))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        NewPart.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("msaero.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewPart.setWindowIcon(icon)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(NewPart)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(NewPart)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(936, 571))
        self.tabWidget.setMaximumSize(QtCore.QSize(936, 571))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 911, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(793, 360))
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
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.LE_PartNumber = QtWidgets.QLineEdit(self.groupBox)
        self.LE_PartNumber.setGeometry(QtCore.QRect(170, 60, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_PartNumber.setFont(font)
        self.LE_PartNumber.setObjectName("LE_PartNumber")
        self.LE_Description = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Description.setGeometry(QtCore.QRect(170, 100, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Description.setFont(font)
        self.LE_Description.setObjectName("LE_Description")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(620, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(610, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.LE_Revision = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Revision.setGeometry(QtCore.QRect(730, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Revision.setFont(font)
        self.LE_Revision.setObjectName("LE_Revision")
        self.LE_MfgSpec = QtWidgets.QLineEdit(self.groupBox)
        self.LE_MfgSpec.setGeometry(QtCore.QRect(730, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_MfgSpec.setFont(font)
        self.LE_MfgSpec.setObjectName("LE_MfgSpec")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(610, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.LE_Mat = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Mat.setGeometry(QtCore.QRect(150, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Mat.setFont(font)
        self.LE_Mat.setObjectName("LE_Mat")
        self.LE_Diam = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Diam.setGeometry(QtCore.QRect(150, 250, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Diam.setFont(font)
        self.LE_Diam.setObjectName("LE_Diam")
        self.CB_HeadOp = QtWidgets.QComboBox(self.groupBox)
        self.CB_HeadOp.setGeometry(QtCore.QRect(730, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CB_HeadOp.setFont(font)
        self.CB_HeadOp.setObjectName("CB_HeadOp")
        self.CB_HeadOp.addItem("")
        self.CB_HeadOp.addItem("")
        self.CB_HeadOp.addItem("")
        self.CB_HeadOp.addItem("")
        self.CB_HeadOp.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(570, 260, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.LE_Shank = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Shank.setGeometry(QtCore.QRect(730, 260, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Shank.setFont(font)
        self.LE_Shank.setObjectName("LE_Shank")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(70, 430, 68, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(600, 420, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(560, 460, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.LE_EstDate = QtWidgets.QLineEdit(self.groupBox)
        self.LE_EstDate.setGeometry(QtCore.QRect(740, 464, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_EstDate.setFont(font)
        self.LE_EstDate.setText("")
        self.LE_EstDate.setObjectName("LE_EstDate")
        self.CB_EstBy = QtWidgets.QComboBox(self.groupBox)
        self.CB_EstBy.setGeometry(QtCore.QRect(740, 420, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CB_EstBy.setFont(font)
        self.CB_EstBy.setObjectName("CB_EstBy")
        self.CB_EstBy.addItem("")
        self.CB_EstBy.addItem("")
        self.CB_EstBy.addItem("")
        self.LE_Note = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Note.setGeometry(QtCore.QRect(150, 430, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Note.setFont(font)
        self.LE_Note.setText("")
        self.LE_Note.setObjectName("LE_Note")
        self.LE_DescMat = QtWidgets.QLineEdit(self.groupBox)
        self.LE_DescMat.setGeometry(QtCore.QRect(280, 210, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_DescMat.setFont(font)
        self.LE_DescMat.setObjectName("LE_DescMat")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(150, 190, 51, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(280, 190, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.LE_Diam_2 = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Diam_2.setGeometry(QtCore.QRect(150, 310, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Diam_2.setFont(font)
        self.LE_Diam_2.setObjectName("LE_Diam_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(40, 360, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.LE_Diam_3 = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Diam_3.setGeometry(QtCore.QRect(150, 360, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Diam_3.setFont(font)
        self.LE_Diam_3.setObjectName("LE_Diam_3")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(590, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.LE_Diam_4 = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Diam_4.setGeometry(QtCore.QRect(730, 310, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Diam_4.setFont(font)
        self.LE_Diam_4.setObjectName("LE_Diam_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 911, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
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
        self.groupBox_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.TableOp = QtWidgets.QTableWidget(self.groupBox_2)
        self.TableOp.setGeometry(QtCore.QRect(10, 30, 891, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableOp.sizePolicy().hasHeightForWidth())
        self.TableOp.setSizePolicy(sizePolicy)
        self.TableOp.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TableOp.setObjectName("TableOp")
        self.TableOp.setColumnCount(4)
        self.TableOp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableOp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOp.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOp.setHorizontalHeaderItem(3, item)
        self.TableOp.horizontalHeader().setCascadingSectionResizes(False)
        self.TableOp.horizontalHeader().setDefaultSectionSize(200)
        self.TableOp.horizontalHeader().setSortIndicatorShown(False)
        self.TableOp.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_8.addWidget(self.tabWidget)

        ##https://stackoverflow.com/questions/22187207/pyqt-dialogs-minimize-window-button-is-missing-in-osx
        ##Minimize and maximize buttons -> WindowMinMaxButtonsHint
        NewPart.setWindowFlags(NewPart.windowFlags() |
        QtCore.Qt.WindowMinMaxButtonsHint  |
        QtCore.Qt.WindowSystemMenuHint)



        self.retranslateUi(NewPart)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NewPart)

    def retranslateUi(self, NewPart):
        _translate = QtCore.QCoreApplication.translate
        NewPart.setWindowTitle(_translate("NewPart", "Part Management"))
        self.groupBox.setTitle(_translate("NewPart", "Part Information :"))
        self.label.setText(_translate("NewPart", "Part Number :"))
        self.label_2.setText(_translate("NewPart", "Description :"))
        self.label_3.setText(_translate("NewPart", "Revision :"))
        self.label_4.setText(_translate("NewPart", "Mfg Spec :"))
        self.label_5.setText(_translate("NewPart", "Material :"))
        self.label_6.setText(_translate("NewPart", "Head Op :"))
        self.label_7.setText(_translate("NewPart", "Diameter :"))
        self.CB_HeadOp.setItemText(0, _translate("NewPart", "HotHead"))
        self.CB_HeadOp.setItemText(1, _translate("NewPart", "ColdHead"))
        self.CB_HeadOp.setItemText(2, _translate("NewPart", "ColdHeadUpset"))
        self.CB_HeadOp.setItemText(3, _translate("NewPart", "HotHeadUpset"))
        self.CB_HeadOp.setItemText(4, _translate("NewPart", "MachinePart"))
        self.label_10.setText(_translate("NewPart", "Shank Lenght :"))
        self.label_11.setText(_translate("NewPart", "Notes : "))
        self.label_12.setText(_translate("NewPart", "Estimator :"))
        self.label_13.setText(_translate("NewPart", "Estimate date : "))
        self.CB_EstBy.setItemText(0, _translate("NewPart", "P.S"))
        self.CB_EstBy.setItemText(1, _translate("NewPart", "J.T"))
        self.CB_EstBy.setItemText(2, _translate("NewPart", "J.C"))
        self.label_17.setText(_translate("NewPart", "Code :"))
        self.label_18.setText(_translate("NewPart", "Designation :"))
        self.label_8.setText(_translate("NewPart", "Part Weight :"))
        self.label_9.setText(_translate("NewPart", "Head Vol :"))
        self.label_19.setText(_translate("NewPart", "Slug Length :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("NewPart", "Part Information"))
        self.groupBox_2.setTitle(_translate("NewPart", "Operation"))
        item = self.TableOp.horizontalHeaderItem(0)
        item.setText(_translate("NewPart", "Code"))
        item = self.TableOp.horizontalHeaderItem(1)
        item.setText(_translate("NewPart", "Operation"))
        item = self.TableOp.horizontalHeaderItem(2)
        item.setText(_translate("NewPart", "Setup"))
        item = self.TableOp.horizontalHeaderItem(3)
        item.setText(_translate("NewPart", "Cost"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("NewPart", "Operation"))



#==============================================================================

#conn = sqlite3.connect("db_Synoptic")
#cur = conn.cursor()    

conn = CES.connectSQLite()        
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


# Classe permettant l'affichage de la fenetre remplie 
            
class VueNewPartFilled(QtWidgets.QDialog,Ui_NewPart):
    def __init__(self, parent,partnumber,description,revision,mfgspec,estby,date,mat,headop,diam,shank,note,ops):
        super(VueNewPartFilled, self).__init__(parent)
        self.setupUi(self)

        self.nbligne = 0
        
        self.LE_PartNumber.setText(partnumber)
        self.LE_Description.setText(description)
        self.LE_Revision.setText(revision)
        self.LE_MfgSpec.setText(mfgspec)
        self.CB_EstBy.setCurrentIndex(estby)
        self.LE_Mat.setText(mat)
        self.CB_HeadOp.setCurrentIndex(headop)
        self.LE_Diam.setText(diam)
        self.LE_Shank.setText(shank)
        self.LE_EstDate.setText(date)
        self.LE_Note.setText(note)
        
        cur.execute("SELECT Groupe, Name, Type FROM Mat WHERE Number = ?",(mat,))
        Groupe = cur.fetchone() 
        group = str(Groupe[0])
        desc = str(Groupe[1])
        mattype = str(Groupe[2])
        
        d = float(diam)
        s = float(shank)
        hdv = round(d * 2.2,3)
        HDV = str(hdv)
        slug = round(hdv + s ,3)
        SLUG = str(slug)
        
        if mattype == "Steel" or mattype == "NiBase" :
                    
            PW = (pi*((d*d)/4)*slug)*0.3
                            
        elif mattype == "Titan" :
                
            PW = (pi*((d*d)/4)*slug)*0.17
            
        elif mattype == "Alum" :
            
            PW = (pi*((d*d)/4)*slug)*0.2
            
        PW = round(PW,3)
        PW = str(PW)
        
        
        
        self.LE_DescMat.setText(desc)
        self.LE_Diam_2.setText(PW)
        self.LE_Diam_3.setText(HDV)
        self.LE_Diam_4.setText(SLUG)
        
        Diam =  float(diam)
        
        setupcost,cost = trouvercout(group,Diam)
        
        i = 0
        while i <= len(ops)-1:
            
            if ops[i] == '0' or ops[i] == ''  or ops[i] == None : 
                break
            
            p = int(i)
            self.TableOp.insertRow(p)
            
            a2 = str(ops[i])        
            a2 = QtWidgets.QTableWidgetItem(a2)
            self.TableOp.setItem(i,0,a2)
        
            pnum = str(ops[i])   
            
            cur.execute("SELECT Name FROM Op WHERE Number = ?",(pnum,))
            Name = cur.fetchone()    
            
            a3 = str(Name[0])
            a3 = QtWidgets.QTableWidgetItem(a3)
            self.TableOp.setItem(i,1,a3)
            
            cur.execute("SELECT %s,%s FROM Op WHERE Number = ?" %(setupcost,cost),(pnum,))
            Cout = cur.fetchone()
            
            a4 = str(Cout[0])
            a4 = QtWidgets.QTableWidgetItem(a4)
            self.TableOp.setItem(i,2,a4)
            a5 = str(Cout[1])
            a5 = QtWidgets.QTableWidgetItem(a5)
            self.TableOp.setItem(i,3,a5)
            

            i = i+1