# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:04:48 2019

@author: stefflc
"""


import unittest #Standard library
'''https://docs.python.org/3/library/unittest.html'''

# import MSACES_NewPart_UI
from MSACES_NewPart_UI import VueNewPart, VueEditPartFilled
'''http://johnnado.com/pyqt-qtest-example/'''
from PyQt5.QtWidgets import QApplication #Not QtGui
# from PyQt5 import QtGui
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys

'''
https://www.youtube.com/watch?v=6tNS--WetLI
Corey Schafer web series
'''

app = QApplication(sys.argv)

class TestNewPart_VueNewPart(unittest.TestCase):

    #Class methods happen once per class
    #I.E. they happen at the very beginning and end
    #Not before/after each test, but once per TestNewPart
    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")




    #Runs before EACH test
    def setUp(self):
        parent = None
        description = "unitTestPart"
        revision = "A"
        mfgspec = "NC"
        estby = "P.S."
        date = "09/30/2019"
        mat = "A286"
        headop = "HOTHEAD"
        diam = 0.5
        shank = 1.5
        note ="A note"
        ops = ['101','103']
        print("typeops2: ", type(ops))
        isNut = False
        isStud = False
        self.form = VueNewPart(None)





    #Runs after EACH test
    def tearDown(self):
        print("teardown")


    # '''must start with test for unittest'''
    # '''python -m unittest test_NewPart_UI.py'''
    # def test_NewPart(self):
    #     print("hi")
    #     a = 1 + 1
    #     b = 2
    #     self.assertEqual(a, b)

    def test_filledpwBolt(self):
        self.form.LE_Mat.setText("517") #A286
        self.form.LE_Diam.setText("1.26")
        self.form.LE_Shank.setText("1.5")
        self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()

        # print(pw) #part weight
        # print(hdvol) #head vol
        # print(slugLength) #slug length
        # print(type(pw))
        # print(type(hdvol))
        # print(type(slugLength))
        # print(type("1.589"))



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "2.772")
        self.assertEqual(slugLength, "4.272")

        self.assertEqual(pw, '1.598')

        self.assertFalse(self.form.isStudBox.isChecked())
        self.assertFalse(self.form.isNutBox.isChecked())

    def test_filledpwBolt2(self):
        self.form.LE_Mat.setText("574") #A286 15/17
        self.form.LE_Diam.setText("0.51")
        self.form.LE_Shank.setText("2.908")
        self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "1.122")
        self.assertEqual(slugLength, "4.030")
        self.assertEqual(pw, '0.247')

        self.assertFalse(self.form.isStudBox.isChecked())
        self.assertFalse(self.form.isNutBox.isChecked())

    def test_filledpwNut(self):
        # self.form.nut == 1


        #hdvol = 2.52
        #shank length = 0
        #slug length = head volume


        self.form.LE_Mat.setText("517") #A286
        self.form.LE_Diam.setText("1.26")
        self.form.LE_Shank.setText("1.5") #simulate user input of 1.5, checking nut box will make this 0.000 actually
        self.form.isNutBox.setChecked(True)
        self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "2.520")
        self.assertEqual(slugLength, "2.520")

        self.assertEqual(pw, '0.943')
        self.assertFalse(self.form.isStudBox.isChecked())
        self.assertTrue(self.form.isNutBox.isChecked())

    def test_filledpwStud(self):
        # self.form.stud == 1

        #hdvol = 0
        #slug length = shank length

        self.form.LE_Mat.setText("517") #A286
        self.form.LE_Diam.setText("1.26")
        self.form.LE_Shank.setText("1.5")
        self.form.isStudBox.setChecked(True)
        self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "0.000")
        self.assertEqual(slugLength, "1.500")

        self.assertEqual(pw, '0.561')
        self.assertFalse(self.form.isNutBox.isChecked())
        self.assertTrue(self.form.isStudBox.isChecked())

    def test_remplirdescription(self):


        # 106 COLD HEAD - STANDARD
        # 118 POINT - HIGH VOLUME
        # 604 TAP THREADS
        # 150 CARBURIZE(9310) & H/T

        self.form.LE_CodeOp.setText("103")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "CUT-OFF SLUGS STD")

        self.form.LE_CodeOp.setText("106")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "COLD HEAD - STANDARD")

        self.form.LE_CodeOp.setText("118")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "POINT - HIGH VOLUME")

        self.form.LE_CodeOp.setText("604")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "TAP THREADS")

        self.form.LE_CodeOp.setText("150")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "CARBURIZE(9310) & H/T")


    def test_remplircode(self):
        self.form.LE_DescriptionOp.setText("CUT-OFF SLUGS STD")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "103")

        self.form.LE_DescriptionOp.setText("COLD HEAD - STANDARD")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "106")

        self.form.LE_DescriptionOp.setText("POINT - HIGH VOLUME")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "118")

        self.form.LE_DescriptionOp.setText("TAP THREADS")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "604")

        self.form.LE_DescriptionOp.setText("CARBURIZE(9310) & H/T")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "150")

    ''' I don't know if this is actually used??'''
    # def test_populerdescdiam(self):
    #     self.form.LE_Mat.setText("517") #A286
    #     # self.form.LE_Diam.setText("1.26")

    def test_remplircodemat(self):
        self.form.LE_DescMat.setText("A286")
        self.form.LE_Diam.setText("1.26")
        self.form.remplircodemat()

        self.assertEqual(self.form.LE_Mat.text(), "517")

    def test_remplircodematError(self):
        ##Make sure this fails###
        # self.assertRaises(TypeError) #catches NoneType / blanks
        with self.assertRaises(TypeError):

            self.form.LE_DescMat.setText("a286")
            self.form.LE_Diam.setText("1.26")
            self.form.remplircodemat()

# class TestNewPart_VueNewPartFilled(unittest.TestCase):

#     #Class methods happen once per class
#     #I.E. they happen at the very beginning and end
#     #Not before/after each test, but once per TestNewPart
#     @classmethod
#     def setUpClass(cls):
#         print("set up class")

#     @classmethod
#     def tearDownClass(cls):
#         print("tear down class")




#     #Runs before EACH test
#     def setUp(self):
#         parent = None
#         description = "unitTestPart"
#         revision = "A"
#         mfgspec = "NC"
#         estby = 0 #index
#         date = "09/30/2019"
#         mat = "517" #code for A286
#         headop = 0 #index
#         diam = "0.406" #str
#         shank = "1.5" #str
#         ####BOLT###
#         ##pw 0.093
#         ##hdvol 0.893
#         #slug 2.393
#         ####NUT####
#         ##pw 0.032
#         ##hdvol 0.812
#         ##slug 0.812
#         ##stud
#         ##pw 0.058
#         ##hdvol 0.000
#         ##slug 1.500


#         note ="A note"
#         ops = ['101','103']
#         isNut = False
#         isStud = False
#         self.form = VueNewPartFilled(None, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, isStud)
#         # self.formNut = VueNewPartFilled(None, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, True, isStud)
#         # self.formStud = VueNewPartFilled(None, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, True)
#         # self.form = VueNewPart(None)





#     #Runs after EACH test
#     def tearDown(self):
#         self.form = None

#         self.formNut = None

#         self.formStud = None
#         print("teardown")


#     # '''must start with test for unittest'''
#     # '''python -m unittest test_NewPart_UI.py'''
#     # def test_NewPart(self):
#     #     print("hi")
#     #     a = 1 + 1
#     #     b = 2
#     #     self.assertEqual(a, b)

#     def test_filledpwBolt(self):
#         print("test_filledpwBolt!!!!!!!!!!")
#         # self.form.filledpw()

#         pw =self.form.LE_Diam_2.text()
#         hdvol = self.form.LE_Diam_3.text()
#         slugLength =self.form.LE_Diam_4.text()



#         self.assertIsInstance(hdvol, str)
#         self.assertIsInstance(pw, str)
#         self.assertIsInstance(slugLength, str)

#         self.assertEqual(hdvol, "0.893")
#         self.assertEqual(slugLength, "2.393")

#         self.assertEqual(pw, '0.093')
#         self.assertFalse(self.form.isStudBox.isChecked())
#         self.assertFalse(self.form.isNutBox.isChecked())

#     # def test_filledpw2(self):
#         # self.form.LE_Mat.setText("574") #A286 15/17
#         # self.form.LE_Diam.setText("0.51")
#         # self.form.LE_Shank.setText("2.908")
#         # self.form.filledpw()

#         # pw =self.form.LE_Diam_2.text()
#         # hdvol = self.form.LE_Diam_3.text()
#         # slugLength =self.form.LE_Diam_4.text()



#         # self.assertIsInstance(hdvol, str)
#         # self.assertIsInstance(pw, str)
#         # self.assertIsInstance(slugLength, str)

#         # self.assertEqual(hdvol, "1.122")
#         # self.assertEqual(slugLength, "4.030")
#         # self.assertEqual(pw, '0.247')







#     def test_remplirdescription(self):
#         print("test_remplirdescription!!!!!!!")

#         # 106 COLD HEAD - STANDARD
#         # 118 POINT - HIGH VOLUME
#         # 604 TAP THREADS
#         # 150 CARBURIZE(9310) & H/T

#         self.form.LE_CodeOp.setText("103")
#         self.form.remplirdescription()
#         self.assertEqual(self.form.LE_DescriptionOp.text(), "CUT-OFF SLUGS STD")

#         self.form.LE_CodeOp.setText("106")
#         self.form.remplirdescription()
#         self.assertEqual(self.form.LE_DescriptionOp.text(), "COLD HEAD - STANDARD")

#         self.form.LE_CodeOp.setText("118")
#         self.form.remplirdescription()
#         self.assertEqual(self.form.LE_DescriptionOp.text(), "POINT - HIGH VOLUME")

#         self.form.LE_CodeOp.setText("604")
#         self.form.remplirdescription()
#         self.assertEqual(self.form.LE_DescriptionOp.text(), "TAP THREADS")

#         self.form.LE_CodeOp.setText("150")
#         self.form.remplirdescription()
#         self.assertEqual(self.form.LE_DescriptionOp.text(), "CARBURIZE(9310) & H/T")


#     def test_remplircode(self):
#         print("test_remplircode!!!!!!!!!!")
#         self.form.LE_DescriptionOp.setText("CUT-OFF SLUGS STD")
#         self.form.remplircode()
#         self.assertEqual(self.form.LE_CodeOp.text(), "103")

#         self.form.LE_DescriptionOp.setText("COLD HEAD - STANDARD")
#         self.form.remplircode()
#         self.assertEqual(self.form.LE_CodeOp.text(), "106")

#         self.form.LE_DescriptionOp.setText("POINT - HIGH VOLUME")
#         self.form.remplircode()
#         self.assertEqual(self.form.LE_CodeOp.text(), "118")

#         self.form.LE_DescriptionOp.setText("TAP THREADS")
#         self.form.remplircode()
#         self.assertEqual(self.form.LE_CodeOp.text(), "604")

#         self.form.LE_DescriptionOp.setText("CARBURIZE(9310) & H/T")
#         self.form.remplircode()
#         self.assertEqual(self.form.LE_CodeOp.text(), "150")

#     ''' I don't know if this is actually used??'''
#     # def test_populerdescdiam(self):
#     #     self.form.LE_Mat.setText("517") #A286
#     #     # self.form.LE_Diam.setText("1.26")

#     def test_remplircodemat(self):
#         self.form.LE_DescMat.setText("A286")
#         self.form.LE_Diam.setText("1.26")
#         self.form.remplircodemat()

#         self.assertEqual(self.form.LE_Mat.text(), "517")

#     def test_remplircodematError(self):
#         ##Make sure this fails###
#         # self.assertRaises(TypeError) #catches NoneType / blanks
#         with self.assertRaises(TypeError):

#             self.form.LE_DescMat.setText("a286")
#             self.form.LE_Diam.setText("1.26")
#             self.form.remplircodemat()

# class TestNewPart_VueNewPartFilled_Nut(unittest.TestCase):

#     #Class methods happen once per class
#     #I.E. they happen at the very beginning and end
#     #Not before/after each test, but once per TestNewPart
#     @classmethod
#     def setUpClass(cls):
#         print("set up class")

#     @classmethod
#     def tearDownClass(cls):
#         print("tear down class")




#     #Runs before EACH test
#     def setUp(self):
#         parent = None
#         description = "unitTestPart"
#         revision = "A"
#         mfgspec = "NC"
#         estby = 0 #index
#         date = "09/30/2019"
#         mat = "517" #code for A286
#         headop = 0 #index
#         diam = "0.406" #str
#         shank = "1.5" #str
#         ####BOLT###
#         ##pw 0.093
#         ##hdvol 0.893
#         #slug 2.393
#         ####NUT####
#         ##pw 0.032
#         ##hdvol 0.812
#         ##slug 0.812
#         ##stud
#         ##pw 0.058
#         ##hdvol 0.000
#         ##slug 1.500


#         note ="A note"
#         ops = ['101','103']
#         isNut = True
#         isStud = False

#         self.formNut = VueNewPartFilled(parent, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, isStud)


#     #Runs after EACH test
#     def tearDown(self):
#         self.form = None

#         self.formNut = None

#         self.formStud = None
#         print("teardown")

#     def test_filledpwNut(self):
#        print('test_filledpwBolt!!!!!!!!')
       

#        pw =self.formNut.LE_Diam_2.text()
#        hdvol = self.formNut.LE_Diam_3.text()
#        slugLength =self.formNut.LE_Diam_4.text()
       
       
       
#        self.assertIsInstance(hdvol, str)
#        self.assertIsInstance(pw, str)
#        self.assertIsInstance(slugLength, str)
       
#        self.assertEqual(hdvol, "0.812")
#        self.assertEqual(slugLength, "0.812")
       
#        self.assertEqual(pw, '0.032')
#        self.assertFalse(self.formNut.isStudBox.isChecked())
#        self.assertTrue(self.formNut.isNutBox.isChecked())



# class TestNewPart_VueNewPartFilled_Stud(unittest.TestCase):

#     #Class methods happen once per class
#     #I.E. they happen at the very beginning and end
#     #Not before/after each test, but once per TestNewPart
#     @classmethod
#     def setUpClass(cls):
#         print("set up class")

#     @classmethod
#     def tearDownClass(cls):
#         print("tear down class")




#     #Runs before EACH test
#     def setUp(self):
#         parent = None
#         description = "unitTestPart"
#         revision = "A"
#         mfgspec = "NC"
#         estby = 0 #index
#         date = "09/30/2019"
#         mat = "517" #code for A286
#         headop = 0 #index
#         diam = "0.406" #str
#         shank = "1.5" #str
#         ####BOLT###
#         ##pw 0.093
#         ##hdvol 0.893
#         #slug 2.393
#         ####NUT####
#         ##pw 0.032
#         ##hdvol 0.812
#         ##slug 0.812
#         ##stud
#         ##pw 0.058
#         ##hdvol 0.000
#         ##slug 1.500


#         note ="A note"
#         ops = ['101','103']
#         isNut = False
#         isStud = True
#         self.formStud = VueNewPartFilled(None, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, isStud)

#     #Runs after EACH test
#     def tearDown(self):
#         self.form = None

#         self.formNut = None

#         self.formStud = None
#         print("teardown")



#     def test_filledpwStud(self):


#         pw =self.formStud.LE_Diam_2.text()
#         hdvol = self.formStud.LE_Diam_3.text()
#         slugLength =self.formStud.LE_Diam_4.text()



#         self.assertIsInstance(hdvol, str)
#         self.assertIsInstance(pw, str)
#         self.assertIsInstance(slugLength, str)

#         self.assertEqual(hdvol, "0.000")
#         self.assertEqual(slugLength, "1.500")

#         self.assertEqual(pw, '0.058')

#         self.assertFalse(self.formStud.isNutBox.isChecked())
#         self.assertTrue(self.formStud.isStudBox.isChecked())


class TestNewPart_VueEditPartFilled_Bolt(unittest.TestCase):
    #Class methods happen once per class
    #I.E. they happen at the very beginning and end
    #Not before/after each test, but once per TestNewPart
    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")




    #Runs before EACH test
    def setUp(self):
        parent = None
        partnumber = "9318M85P04($$$)"
        description = "D,OS,718,3/8-24"
        revision = "J"
        mfgspec = "C50TF13 CL-B"
        estby = 0 #index #PS !*+
        date = "2017-04-25"
        mat = "526" #code for ?
        headop = 0 #index
        diam = "0.406" #str
        shank = "1.56" #str
        ##BOLT##
        # pw 0.097
        # Diam 0.406
        # Shank 1.56
        # Hdv 0.893
        # heading hot HEAD
        # slug 2.453


        note ="**P01>P03 = MP159, P04>P06 = INCO718**                          **CLOSE TOLERANCE .0001**"
        ops = ['117','103','121','133','104','311','162','637','115','410','409','188','325','129','130','177','166','349']
        isNut = False
        isStud = False
        self.form = VueEditPartFilled(parent,partnumber, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, isStud)

    #Runs after EACH test
    def tearDown(self):
        self.form = None

        print("teardown")


    def test_filledpwBolt(self):
        print("test_filledpwBolt!!!!!!!!!!")
        # self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "0.893")
        self.assertEqual(slugLength, "2.453")

        self.assertEqual(pw, '0.095')
        self.assertFalse(self.form.isStudBox.isChecked())
        self.assertFalse(self.form.isNutBox.isChecked())



    def test_remplirdescription(self):
        print("test_remplirdescription!!!!!!!")

        # 106 COLD HEAD - STANDARD
        # 118 POINT - HIGH VOLUME
        # 604 TAP THREADS
        # 150 CARBURIZE(9310) & H/T

        self.form.LE_CodeOp.setText("103")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "CUT-OFF SLUGS STD")

        self.form.LE_CodeOp.setText("106")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "COLD HEAD - STANDARD")

        self.form.LE_CodeOp.setText("118")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "POINT - HIGH VOLUME")

        self.form.LE_CodeOp.setText("604")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "TAP THREADS")

        self.form.LE_CodeOp.setText("150")
        self.form.remplirdescription()
        self.assertEqual(self.form.LE_DescriptionOp.text(), "CARBURIZE(9310) & H/T")


    def test_remplircode(self):
        print("test_remplircode!!!!!!!!!!")
        self.form.LE_DescriptionOp.setText("CUT-OFF SLUGS STD")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "103")

        self.form.LE_DescriptionOp.setText("COLD HEAD - STANDARD")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "106")

        self.form.LE_DescriptionOp.setText("POINT - HIGH VOLUME")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "118")

        self.form.LE_DescriptionOp.setText("TAP THREADS")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "604")

        self.form.LE_DescriptionOp.setText("CARBURIZE(9310) & H/T")
        self.form.remplircode()
        self.assertEqual(self.form.LE_CodeOp.text(), "150")

    ''' I don't know if this is actually used??'''
    # def test_populerdescdiam(self):
    #     self.form.LE_Mat.setText("517") #A286
    #     # self.form.LE_Diam.setText("1.26")

    def test_remplircodemat(self):
        self.form.LE_DescMat.setText("A286")
        self.form.LE_Diam.setText("1.26")
        self.form.remplircodemat()

        self.assertEqual(self.form.LE_Mat.text(), "517")

    def test_remplircodematError(self):
        ##Make sure this fails###
        # self.assertRaises(TypeError) #catches NoneType / blanks
        with self.assertRaises(TypeError):

            self.form.LE_DescMat.setText("a286")
            self.form.LE_Diam.setText("1.26")
            self.form.remplircodemat()


class TestNewPart_VueEditPartFilled_Nut(unittest.TestCase):
    #Class methods happen once per class
    #I.E. they happen at the very beginning and end
    #Not before/after each test, but once per TestNewPart
    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")




    #Runs before EACH test
    def setUp(self):
        parent = None
        partnumber = "9318M85P04($$$)"
        description = "D,OS,718,3/8-24"
        revision = "J"
        mfgspec = "C50TF13 CL-B"
        estby = 0 #index #PS !*+
        date = "2017-04-25"
        mat = "526" #code for ?
        headop = 0 #index
        diam = "0.406" #str
        shank = "1.56" #str
        ##NUT##
        # pw 0.032
        # Diam 0.406
        # Shank 0.000
        # Hdv 0.812
        # heading hot HEAD
        # slug 0.812


        note ="**P01>P03 = MP159, P04>P06 = INCO718**                          **CLOSE TOLERANCE .0001**"
        ops = ['117','103','121','133','104','311','162','637','115','410','409','188','325','129','130','177','166','349']
        isNut = True
        isStud = False
        self.form = VueEditPartFilled(parent,partnumber, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, isStud)

    #Runs after EACH test
    def tearDown(self):
        self.form = None

        print("teardown")


    def test_filledpwBolt(self):
        print("test_filledpwBolt!!!!!!!!!!")
        # self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "0.812")
        self.assertEqual(slugLength, "0.812")

        self.assertEqual(pw, '0.032')
        self.assertFalse(self.form.isStudBox.isChecked())
        self.assertTrue(self.form.isNutBox.isChecked())

class TestNewPart_VueEditPartFilled_Stud(unittest.TestCase):
    #Class methods happen once per class
    #I.E. they happen at the very beginning and end
    #Not before/after each test, but once per TestNewPart
    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")




    #Runs before EACH test
    def setUp(self):
        parent = None
        partnumber = "9318M85P04($$$)"
        description = "D,OS,718,3/8-24"
        revision = "J"
        mfgspec = "C50TF13 CL-B"
        estby = 0 #index #PS !*+
        date = "2017-04-25"
        mat = "526" #code for ?
        headop = 0 #index
        diam = "0.406" #str
        shank = "1.56" #str
        ##STUD##
        # pw 0.061
        # Diam 0.406
        # Shank 1.56
        # Hdv 0.000
        # heading hot HEAD
        # slug 1.560


        note ="**P01>P03 = MP159, P04>P06 = INCO718**                          **CLOSE TOLERANCE .0001**"
        ops = ['117','103','121','133','104','311','162','637','115','410','409','188','325','129','130','177','166','349']
        isNut = False
        isStud = True
        self.form = VueEditPartFilled(parent,partnumber, description, revision, mfgspec, estby, date, mat,headop, diam, shank, note, ops, isNut, isStud)

    #Runs after EACH test
    def tearDown(self):
        self.form = None

        print("teardown")


    def test_filledpwBolt(self):
        print("test_filledpwBolt!!!!!!!!!!")
        # self.form.filledpw()

        pw =self.form.LE_Diam_2.text()
        hdvol = self.form.LE_Diam_3.text()
        slugLength =self.form.LE_Diam_4.text()



        self.assertIsInstance(hdvol, str)
        self.assertIsInstance(pw, str)
        self.assertIsInstance(slugLength, str)

        self.assertEqual(hdvol, "0.000")
        self.assertEqual(slugLength, "1.560")

        self.assertEqual(pw, '0.061')

        self.assertTrue(self.form.isStudBox.isChecked())
        self.assertFalse(self.form.isNutBox.isChecked())





'''
This will make python test_NewPart_UI.py work
instead of python -m unittest test_NewPart_UI.py
'''
if __name__ == '__main__':
    unittest.main()