# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:26:46 2019

@author: stefflc


UnitTest for MSACES_Quote
"""



import unittest #Standard library
'''https://docs.python.org/3/library/unittest.html'''





from MSACES_Quote import VueQuote
from MSACES_genericFunctions import calculatePW

'''http://johnnado.com/pyqt-qtest-example/'''
from PyQt5.QtWidgets import QApplication #Not QtGui
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QCompleter

from MSACES_genericFunctions import closeSQLite
from MSACES_genericFunctions import connectSQLite
from PyQt5 import QtWidgets

import sys
import traceback

'''
https://www.youtube.com/watch?v=6tNS--WetLI
Corey Schafer web series
'''

app = QApplication(sys.argv) #This will make UI try to appear and fail don't use.


sys.excepthook = traceback.print_exception



class TestQuote_VueQuote(unittest.TestCase):

    #Runs before EACH test
    def setUp(self):
        parent = None
        self.form = VueQuote(parent)


    '''This will generate a quote by entering part number and price break(s)
    '''

    #Use this to test a quote and to test PBQuote##
    def test_Quoting(self):
        # text1 = QLineEdit(str("JSFB11-14-31 ($$$)"))
        text1 = QLineEdit(str("S700T1715-NO BID"))
        a2 = QtWidgets.QTableWidgetItem(str(1500))
        # a3 = QtWidgets.QTableWidgetItem(str(3000))


        #row, line, item
        self.form.TableQuote.setCellWidget(0, 0, text1)
        self.form.TableQuote.setItem(0, 1, a2)
        # self.form.TableQuote.setItem(0, 2, a3)

        self.form.PBQuote()





'''
This will make python test_NewPart_UI.py work
instead of python -m unittest test_NewPart_UI.py
'''
if __name__ == '__main__':
    unittest.main()

