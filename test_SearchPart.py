# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:04:48 2019

@author: stefflc
"""


import unittest #Standard library
'''https://docs.python.org/3/library/unittest.html'''


from MSACES_SearchPart import VueSearchPart
from MSACES_NewPart import VueEditPartFilled

'''http://johnnado.com/pyqt-qtest-example/'''
from PyQt5.QtWidgets import QApplication #Not QtGui
# from PyQt5.QtTest import QTest
# from PyQt5.QtCore import Qt
import sys
import traceback

'''
https://www.youtube.com/watch?v=6tNS--WetLI
Corey Schafer web series
'''

app = QApplication(sys.argv) #This will make UI try to appear and fail don't use.


sys.excepthook = traceback.print_exception
    #     # app.exec_()



class TestSearchPart_VueSearchPart(unittest.TestCase):

    #Class methods happen once per class
    #I.E. they happen at the very beginning and end
    #Not before/after each test, but once per TestNewPart
    # @classmethod
    # def setUpClass(cls):
    #     print("set up class test_SearchPart")

    # @classmethod
    # def tearDownClass(cls):
    #     print("tear down class test_SearchPart")




    #Runs before EACH test
    def setUp(self):
        # print("setup")
        parent = None
        # description = "unitTestPart"
        # revision = "A"
        # mfgspec = "NC"
        # estby = "P.S."
        # date = "09/30/2019"
        # mat = "A286"
        # headop = "HOTHEAD"
        # diam = 0.5
        # shank = 1.5
        # note ="A note"
        # ops = ['101','103']
        # print("typeops2: ", type(ops))
        # isNut = False
        # isStud = False
        # self.form = VueNewPart(None)

        self.form = VueSearchPart(parent)





    # #Runs after EACH test
    # def tearDown(self):
    #     print("teardown")

    '''Not sure of a good way to test the function setSearchPartNumberComplter '''
    # def test_setSearchPartNumberCompleter(self):
    #     print("no good way to test this?")

    '''Run a manual test instead of actually deleting?'''
    '''Or create a temporary database to use?'''
    ''' or connect to the existing database - add part - delete that part '''
    # def test_DeletePart(self):
    #     print("Let's not test this")
    #     ###Create part
    #     ### delete part
    #     ### re-query
    #     ### make sure it's deleted

    def test_translateNut(self):
        nut = 1

        self.form.translateNut(nut)

        self.assertTrue(self.form.isNut)
        # self.assertFalse(self.isStud)
    def test_translateStud(self):
        stud = 1

        self.form.translateStud(stud)

        self.assertTrue(self.form.isStud)
        # self.assertFalse(self.isStud)

    def test_PBGoToEditPart(self):

        self.form.LE_SearchPartNumber.setText("BACB30PN10-17")
        #desc 12PT,FB,7185/8-18
        #rev AP
        #mfgspec BP
        #mat 600
        #diam 0.635
        #shank 2.0325
        #hothead #0
        #pw 0.326
        #slug 3.429
        #1.397
        #P.S #0
        #note **PASSIVATE**
        #estimate date 10/04/2019
        self.form.PBGoToEditPart()
        partnumber = self.form.LE_SearchPartNumber.text()

        parent = None
        Description = "12PT,FB,7185/8-18"
        Revision = "AP"
        MfgSpec = "BP"
        EstBy = 0 #index
        Date = "09/17/2019"
        Mat = '600'
        HeadOp = 0 #index
        Diameter = "0.635"
        Shank = "2.0325"
        Note = "**PASSIVATE**"
        Ops = ['117','103','121','133','104','311','162','111','115','189','188','325','129','130','560','283','284','470']
        isNoBid = 0
        NoBidNote = None
        self.isNut = 0
        self.isStud = 0


        self.assertEqual("BACB30PN10-17", partnumber)
        vue = VueEditPartFilled(parent,partnumber, Description,Revision,MfgSpec,EstBy,Date,Mat,HeadOp,Diameter,Shank,Note,Ops,self.isNut,self.isStud, isNoBid, NoBidNote)

        self.assertEqual(partnumber, vue.partnumber)
        self.assertEqual(Description, vue.description)
        # print("vue.description: ", vue.description)
        self.assertEqual(Revision, vue.revision)
        self.assertEqual(MfgSpec, vue.mfgspec)
        self.assertEqual(EstBy, vue.estby)
        self.assertEqual(Date, vue.date)
        self.assertEqual(Mat, vue.mat)
        self.assertEqual(HeadOp, vue.headop)
        self.assertEqual(Diameter, vue.diam)
        self.assertEqual(Shank, vue.shank)
        self.assertEqual(Note, vue.note)
        self.assertEqual(Ops, vue.ops)
        self.assertEqual(self.isNut, vue.isNut)
        self.assertEqual(self.isStud, vue.isStud)


        self.assertEqual(vue.partnumber, vue.LE_PartNumber.text())
        self.assertEqual(vue.description, vue.LE_Description.text())
        self.assertEqual(vue.revision, vue.LE_Revision.text())
        # print("vue")
        self.assertEqual(vue.mfgspec, vue.LE_MfgSpec.text())
        # print("vue.estby: ", vue.estby)
        self.assertEqual(vue.estby, vue.CB_EstBy.currentIndex())
        self.assertEqual(vue.mat, vue.LE_Mat.text())
        self.assertEqual(vue.headop, vue.CB_HeadOp.currentIndex())
        self.assertEqual(vue.diam, vue.LE_Diam.text())
        self.assertEqual(vue.shank, vue.LE_Shank.text())
        # self.assertEqual(vue.note, vue.LE_Note.text())
        self.assertEqual(vue.note, vue.LE_Note.toPlainText()) #Specific property for QTextEdit instead of QLineEdit

        self.assertEqual("1", vue.LE_NumeroOp.text())

    def test_PBGoToEditPart_nobidpart(self):

        self.form.LE_SearchPartNumber.setText("51U688 ($$$$) (NO BID)")
        #desc 12PT,FB,7185/8-18
        #rev AP
        #mfgspec BP
        #mat 600
        #diam 0.635
        #shank 2.0325
        #hothead #0
        #pw 0.326
        #slug 3.429
        #1.397
        #P.S #0
        #note **PASSIVATE**
        #estimate date 10/04/2019
        self.form.PBGoToEditPart()
        partnumber = self.form.LE_SearchPartNumber.text()

        parent = None
        Description = "SLAB/HD,CLEVIS,MP159,1-12"
        Revision = "C"
        MfgSpec = "BPAS7475"
        EstBy = 0 #index
        Date = "01/22/2020"
        Mat = '986'
        HeadOp = 0 #index
        Diameter = "1.39"
        Shank = "4.103"
        Note = "** NO BID, CAN'T ACHIEVE ELEVATED TENSILE REQUIREMENT** "
        #make sure to include Op1 from database which is (# of operations + 100). I.E. 39 operations is 139.'''
        Ops = ['139','299', '299', '299', '299', '299', '299', '299', '299', '299', '103','120','121','133','402','402','649','647','534','162','263','1017','931','415','269','630','143','143','613','220','646','166','366','972','215','491','734','401','401','401']
        isNoBid = 1
        NoBidNote = "** NO BID, CAN'T ACHIEVE ELEVATED TENSILE REQUIREMENT** "
        self.isNut = 0
        self.isStud = 0


        self.assertEqual("51U688 ($$$$) (NO BID)", partnumber)
        vue = VueEditPartFilled(parent,partnumber, Description,Revision,MfgSpec,EstBy,Date,Mat,HeadOp,Diameter,Shank,Note,Ops,self.isNut,self.isStud, isNoBid, NoBidNote)

        self.assertEqual(partnumber, vue.partnumber)
        self.assertEqual(Description, vue.description)
        # print("vue.description: ", vue.description)
        self.assertEqual(Revision, vue.revision)
        self.assertEqual(MfgSpec, vue.mfgspec)
        self.assertEqual(EstBy, vue.estby)
        self.assertEqual(Date, vue.date)
        self.assertEqual(Mat, vue.mat)
        self.assertEqual(HeadOp, vue.headop)
        self.assertEqual(Diameter, vue.diam)
        self.assertEqual(Shank, vue.shank)
        self.assertEqual(Note, vue.note)
        self.assertEqual(Ops, vue.ops)
        self.assertEqual(self.isNut, vue.isNut)
        self.assertEqual(self.isStud, vue.isStud)


        self.assertEqual(vue.partnumber, vue.LE_PartNumber.text())
        self.assertEqual(vue.description, vue.LE_Description.text())
        self.assertEqual(vue.revision, vue.LE_Revision.text())
        # print("vue")
        self.assertEqual(vue.mfgspec, vue.LE_MfgSpec.text())
        # print("vue.estby: ", vue.estby)
        self.assertEqual(vue.estby, vue.CB_EstBy.currentIndex())
        self.assertEqual(vue.mat, vue.LE_Mat.text())
        self.assertEqual(vue.headop, vue.CB_HeadOp.currentIndex())
        self.assertEqual(vue.diam, vue.LE_Diam.text())
        self.assertEqual(vue.shank, vue.LE_Shank.text())
        # self.assertEqual(vue.note, vue.LE_Note.text())
        self.assertEqual(vue.note, vue.LE_Note.toPlainText()) #Specific property for QTextEdit instead of QLineEdit

        self.assertEqual("1", vue.LE_NumeroOp.text())

        self.assertEqual(vue.NoBidNote, vue.txtNoBid.toPlainText())







'''
This will make python test_NewPart_UI.py work
instead of python -m unittest test_NewPart_UI.py
'''
if __name__ == '__main__':
    unittest.main()