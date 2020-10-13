# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:38:37 2017

@author: tastetf


10/08/19 - Various updates to users, code, etc.
Update use of AUTH_LIST, separate code into better functions

"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import getpass
# import sqlite3  #New 3/1


import MSACES_UI
# import MSACES_NewPart_UI
import MSACES_NewPart
# import MSACES_SearchPart_UI
import MSACES_SearchPart
# import MSACES_Quote_UI
import MSACES_Quote
# import MSACES_MM_UI
import MSACES_MM

# import MSACES_OpManagement_UI
import MSACES_OpManagement


from MSACES_genericFunctions import printError

# import os
import traceback


class CES(QtWidgets.QMainWindow, MSACES_UI.Ui_MainWindow):

    

    
    def __init__(self, parent=None): 
        super(CES, self).__init__(parent)
        self.setupUi(self)

        self.AUTH_USER_LIST = ['stellap', 'stefflc', 'doshig']
        self.user = getpass.getuser()
        self.setupButtons()

        
    def PBNewPart(self):
        try:
            vue = MSACES_NewPart.VueNewPart(self)
            self.checkAuth(vue)

        except Exception as ex:
            printError(ex)
            
    def PBCreateFrom(self):
        try:
            vue = MSACES_SearchPart.VueSearchPart(self)
            self.checkAuth(vue)
        except Exception as ex:
            printError(ex)        
        
    def PBStartQuote(self):
        try:
            vue = MSACES_Quote.VueQuote(self)
            vue.show()
        except Exception as ex:
            printError(ex)
    
    def PBRawMat(self):
        try:
            vue = MSACES_MM.VueMaterialManagement(self)
            self.checkAuth(vue)
        except Exception as ex:
            printError(ex)
    
    def PBOpManagement(self):
        try:
            vue = MSACES_OpManagement.VueOpManagement(self)
            self.checkAuth(vue)
        except Exception as ex:
            printError(ex)

    def setupButtons(self):
        self.PB_NewPart.clicked.connect(self.PBNewPart)
        self.PB_CreateFrom.clicked.connect(self.PBCreateFrom)
        self.PB_StartQuote.clicked.connect(self.PBStartQuote)
        self.PB_RawMat.clicked.connect(self.PBRawMat)
        self.PB_Op.clicked.connect(self.PBOpManagement)


    '''Display warning message if user is not authorized'''
    def notAuth(self):
        QMessageBox.about(self, "Warning", "Denied. User is not allowed to access this function.")
        return
    '''Check authorization. If authorize show the view/vue '''
    def checkAuth(self, vue):
        if self.user not in self.AUTH_USER_LIST:
            self.notAuth()
            return
        else:
            vue.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    form = CES()
    form.show()
    ###This will grab ALL exceptions even outside of a try/except look and print to the stack trace####
    ###https://coldfix.eu/2016/11/08/pyqt-boilerplate/###
    sys.excepthook = traceback.print_exception
    app.exec_()

if __name__ == "__main__":
    main()