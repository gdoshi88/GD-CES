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
    #     # app.exec_()



class TestQuote_VueQuote(unittest.TestCase):

    #Runs before EACH test
    def setUp(self):
        parent = None
        self.form = VueQuote(parent)
        # self.form.show()


    '''This will generate a quote by entering part number and price break(s)
    '''

    #Use this to test a quote and to test PBQuote##
    def test_Quoting(self):
        text1 = QLineEdit(str("BACB30PN10-17"))
        a2 = QtWidgets.QTableWidgetItem(str(1500))
        # a3 = QtWidgets.QTableWidgetItem(str(3000))


        #row, line, item
        self.form.TableQuote.setCellWidget(0, 0, text1)
        self.form.TableQuote.setItem(0, 1, a2)
        # self.form.TableQuote.setItem(0, 2, a3)

        self.form.PBQuote()

        self.assertEqual(0.745, self.form.SETUP)
        self.assertEqual(1500, self.form.qty)
        self.assertEqual(17, self.form.synopticNumOps)
        self.assertEqual(152, self.form.scrap)
        self.assertEqual("NiBase", self.form.mattype)
        self.assertEqual(0.635, self.form.diam)
        self.assertEqual(19, self.form.matcost)
        self.assertEqual(3.429, self.form.SLUG)
        self.assertEqual("SUE", self.form.setupcost)
        self.assertEqual("DG6E", self.form.cost)
        self.assertEqual("E", self.form.matgroupe)
        self.assertEqual(19.0, self.form.matcost)
        self.assertFalse(self.form.isNut)
        self.assertFalse(self.form.isStud)
        self.assertEqual(2.0325, self.form.shank)
        self.assertEqual("BACB30PN10-17", self.form.partnumber)

    # def test_Quoting_Fail(self):
    #     text1 = QLineEdit(str("BACB30PN10-17"))
    #     a2 = QtWidgets.QTableWidgetItem("1,500")
    #     # a3 = QtWidgets.QTableWidgetItem(str(3000))


    #     #row, line, item
    #     self.form.TableQuote.setCellWidget(0, 0, text1)
    #     self.form.TableQuote.setItem(0, 1, a2)
    #     # self.form.TableQuote.setItem(0, 2, a3)

    #     self.form.PBQuote()

    #     self.assertEqual(0.745, self.form.SETUP)
    #     self.assertEqual(1500, self.form.qty)
    #     self.assertEqual(17, self.form.synopticNumOps)
    #     self.assertEqual(152, self.form.scrap)
    #     self.assertEqual("NiBase", self.form.mattype)
    #     self.assertEqual(0.635, self.form.diam)
    #     self.assertEqual(19, self.form.matcost)
    #     self.assertEqual(3.429, self.form.SLUG)
    #     self.assertEqual("SUE", self.form.setupcost)
    #     self.assertEqual("DG6E", self.form.cost)
    #     self.assertEqual("E", self.form.matgroupe)
    #     self.assertEqual(19.0, self.form.matcost)
    #     self.assertFalse(self.form.isNut)
    #     self.assertFalse(self.form.isStud)
    #     self.assertEqual(2.0325, self.form.shank)
    #     self.assertEqual("BACB30PN10-17", self.form.partnumber)


    def test_EraseForPaste(self):
        self.form.eraseForPaste()
        ###Assert that the 0,0 cell is blank I.E. has NO Completer / drop down helper box
        self.assertIsNone(self.form.TableQuote.cellWidget(0,0))

    def test_getCurrentCell(self):
        self.assertEqual(0, self.form.currentrow)
        self.assertEqual(0, self.form.currentcolumn)
        self.assertNotEqual(1, self.form.currentrow)




    def test_clipboardChanged(self):
        pass

    def test_PBClearContent(self):
        text1 = QLineEdit(str("BACB30PN10-17"))
        a2 = QtWidgets.QTableWidgetItem(str(1500))
        a3 = QtWidgets.QTableWidgetItem(str(3000))


        #row, line, item
        self.form.TableQuote.setCellWidget(0, 0, text1)
        self.form.TableQuote.setItem(0, 1, a2)
        self.form.TableQuote.setItem(0, 2, a3)

        self.form.TableQuote.setCellWidget(1, 0, text1)
        self.form.TableQuote.setItem(1, 1, a2)
        self.form.TableQuote.setItem(1, 2, a3)

        self.form.PBClearContent()


        self.assertEqual(0, self.form.currentrow)
        self.assertEqual(0, self.form.currentcolumn)
        self.assertEqual(0, self.form.copy)
        self.assertIsInstance(self.form.TableQuote.cellWidget(0,0).completer(), QCompleter)

        self.assertIsNone(self.form.TableQuote.cellWidget(0,1) )
        self.assertIsNone(self.form.TableQuote.cellWidget(0,2) )
        self.assertIsNone(self.form.TableQuote.cellWidget(1,1) )
        self.assertIsNone(self.form.TableQuote.cellWidget(1,2) )

    def test_isPartNumberValid(self):
        self.form.partnumber = "BACB30PN10-17"
        self.form.isPartNumberValid()

        self.assertTrue(self.form.partNumberValid)

    def test_isPartNumberValidFail(self):
        self.form.partnumber = "xACB30PN10-17"
        self.form.isPartNumberValid()


        self.assertFalse(self.form.partNumberValid)





    def test_calculatePW(self):
        # slug, diam
        PW = calculatePW("Steel",4.272,1.26 )
        self.assertEqual(PW, 1.598)
        self.assertIsInstance(PW, float)

    def test_calculatePWFail(self):

        with self.assertRaises(NameError):
            PW = calculatePW("Steeel",4.272,1.26 )


        with self.assertRaises(UnboundLocalError):
            self.assertIsNone(PW)



    def test_setCompleters(self):
        # print()
        bill =self.form.TableQuote.cellWidget(0,0)
        # print(bill.completer())
        # self.assertEqual(type(bill), QCompleter)
        self.assertIsInstance(bill.completer(), QCompleter)

    def test_calculateScrap10(self):
        self.form.matcost = 10
        self.form.qty = 1500
        self.form.calculateScrap()
        self.assertEqual(152,self.form.scrap)

        self.form.matcost = 10
        self.form.qty = 3000
        self.form.calculateScrap()
        self.assertEqual(245,self.form.scrap)

        self.form.matcost = 10
        self.form.qty = 5000
        self.form.calculateScrap()
        self.assertEqual(369,self.form.scrap)
            ####
        self.form.matcost = 19
        self.form.qty = 1500
        self.form.calculateScrap()
        self.assertEqual(152,self.form.scrap)

        self.form.matcost = 19
        self.form.qty = 3000
        self.form.calculateScrap()
        self.assertEqual(245,self.form.scrap)

        self.form.matcost = 19
        self.form.qty = 5000
        self.form.calculateScrap()
        self.assertEqual(369,self.form.scrap)
        ####
        self.form.matcost = -19
        self.form.qty = 5000
        with self.assertRaises(ValueError):
            self.form.calculateScrap()
        ####
        self.form.matcost = 19
        self.form.qty = -5000
        with self.assertRaises(ValueError):
            self.form.calculateScrap()

    def test_calculateScrap50(self):
        self.form.matcost = 50
        self.form.qty = 1500
        self.form.calculateScrap()
        self.assertEqual(135,self.form.scrap)

        self.form.matcost = 50
        self.form.qty = 3000
        self.form.calculateScrap()
        self.assertEqual(228,self.form.scrap)

        self.form.matcost = 50
        self.form.qty = 5000
        self.form.calculateScrap()
        self.assertEqual(352,self.form.scrap)
            ####

        self.form.matcost = -50
        self.form.qty = 5000
        with self.assertRaises(ValueError):
            self.form.calculateScrap()
        ####
        self.form.matcost = 50
        self.form.qty = -5000
        with self.assertRaises(ValueError):
            self.form.calculateScrap()

    def test_calculateHeadVol(self):
        self.form.isNut = False
        self.form.isStud = False


        self.form.diam = 1.26
        self.form.calculateHeadVol()
        self.assertEqual(2.772, self.form.HDVOL)
        self.form.HDVOL is None


        self.form.isNut = True
        self.form.calculateHeadVol()
        self.assertEqual(2.520, self.form.HDVOL)
        self.form.HDVOL is None

        self.form.partnumber = "JSFB11-14-31 ($$$)"
        self.form.isStud = True
        #logic error - still a nut when changed to a stud
        with self.assertRaises(ValueError):
            self.form.calculateHeadVol()


        self.form.isNut = False
        self.form.calculateHeadVol()
        self.assertEqual(0.000, self.form.HDVOL)



    def test_calculateSlugLength(self):
        self.form.HDVOL = 2.772
        self.form.shank = 1.5

        self.form.calculateSlugLength()
        self.assertEqual(4.272, self.form.SLUG)


    def test_getNumberOps(self):
        self.form.partnumber = "BACB30PN10-17"
        conn =connectSQLite()
        cur = conn.cursor()

        self.form.getNumberOps(cur)
        closeSQLite(conn)
        self.assertEqual(17, self.form.synopticNumOps)

    def test_findPartInfo(self):
        self.form.partnumber = "BACB30PN10-17"
        conn =connectSQLite()
        cur = conn.cursor()

        self.form.findPartInfo(cur)
        closeSQLite(conn)

        self.assertEqual("P.S", self.form.estimator)
        self.assertEqual("AP", self.form.partRev)
        self.assertEqual("12PT,FB,7185/8-18", self.form.partDesc)
        self.assertEqual("BP", self.form.partMfgSpec)
        self.assertEqual("**PASSIVATE**", self.form.partNote)
        self.assertEqual(600, self.form.partMaterial)
        self.assertEqual("09/17/2019", self.form.creationDate)

    def test_findMaterialInfo(self):
        # self.form.partnumber = "BACB30PN10-17"
        self.form.partMaterial = "600"
        conn =connectSQLite()
        cur = conn.cursor()

        self.form.findMaterialInfo(cur)
        closeSQLite(conn)

        self.assertEqual("INCO718--AMS5662/C50TF13", self.form.matnamespec)

    def test_findEstimator(self):
        self.form.estimator = "PS !*XX"
        self.form.findEstimator()
        self.assertEqual("PS", self.form.estimator)

        self.form.estimator = "****FOR INFO ONLY***"
        self.form.findEstimator()
        self.assertEqual("****FOR INFO ONLY***", self.form.estimator)

        self.form.estimator = "JIM H!*X"
        self.form.findEstimator()
        self.assertEqual("JIM", self.form.estimator)

        self.form.estimator = "JIM  L=G+1.3 82"
        self.form.findEstimator()
        self.assertEqual("JIM", self.form.estimator)

        self.form.estimator = "JOY 0"
        self.form.findEstimator()
        self.assertEqual("JOY", self.form.estimator)

        self.form.estimator = "JIM**$TOCK** !*XX"
        self.form.findEstimator()
        self.assertEqual("JIM", self.form.estimator)

        self.form.estimator = "JOY (PER JH/ RS)"
        self.form.findEstimator()
        self.assertEqual("JOY", self.form.estimator)

        self.form.estimator = "JIM*HIGH MAR GIN*!*XX"
        self.form.findEstimator()
        self.assertEqual("JIM", self.form.estimator)

        self.form.estimator = "JIM**MUST SE E NOTES*"
        self.form.findEstimator()
        self.assertEqual("JIM", self.form.estimator)

'''
This will make python test_NewPart_UI.py work
instead of python -m unittest test_NewPart_UI.py
'''
if __name__ == '__main__':
    unittest.main()

