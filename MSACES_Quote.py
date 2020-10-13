# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:39:41 2019

@author: stefflc
"""
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication

import xlsxwriter
from datetime import datetime

import os
import getpass

import re

from MSACES_Quote_UI import Ui_Quote
from MSACES_genericFunctions import trouvercout
from MSACES_genericFunctions import printError
from MSACES_genericFunctions import closeSQLite
from MSACES_genericFunctions import connectSQLite
from MSACES_genericFunctions import calculatePW

#============================================================================


'''
All instances of shank are self.shank and are safe to use
All instances of diam are self.diam and are safe to use
self.self.partnumber
self.partNumberValid
self.matcost
'''


# Class to display the main Quote window

class VueQuote(QtWidgets.QDialog,Ui_Quote):

    def __init__(self, parent):
        super(VueQuote, self).__init__(parent)
        # print("Starting a quote")
        self.setupUi(self)  
        self.PB_ClearContent.clicked.connect(self.PBClearContent)
        self.PB_Quote.clicked.connect(self.PBQuote)

        self.copy = 0
        self.currentrow = 0
        self.currentcolumn = 0
        
        self.setCompleters()

 

        self.PB_CopyPaste.clicked.connect(self.clipboardChanged)
        self.TableQuote.cellClicked.connect(self.getCurrentCell)
        self.PB_EraseForPaste.clicked.connect(self.eraseForPaste)

    '''
    Set the text completers that help user complete entry
    Choices should be all part numbers in the database
    '''
    def setCompleters(self):
        conn =connectSQLite()
        cur = conn.cursor()

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
        closeSQLite(conn)

    def eraseForPaste(self):
        self.TableQuote.clearContents()
        self.TableQuote.setCurrentCell(self.currentrow, self.currentcolumn) 
        
        
    def getCurrentCell(self):
        ####Need to make this work for text boxes not just items###
        
        bb = self.TableQuote.currentColumn()
#        try:
#            self.
        print("bb, current column: ", bb)
        self.currentcolumn = bb
        a = self.TableQuote.currentRow()
        a = int(a)
        print("a, current row: ", a)
        self.currentrow = a
        

        
                        
            
   # Get the system clipboard contents
    def clipboardChanged(self):
        
        self.copy = 1
        ROW_ZERO = 0
        COLUMN_ZERO = 0

        print("current col: ", self.TableQuote.currentColumn() )
        
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
        n = ROW_ZERO 
        print("len(textl): ", len(textl))
        while n <= len(textl)-1:
            print("inside loop 832")
            ##\t is a tab
            textc = textl[n].split('\t')
            print("textc split tab: ", textc)
            print("len(textc): ", len(textc))
            i = COLUMN_ZERO 
#            while i <=len(textc)-1: #Original
            while i <len(textc):
                a1 = str(textc[i])
                print("a1 init: ", a1)
                
                '''QLineEdit needs to be separate, 
                so that QCompleter can be associated. 
                Use text, not QTableWidget as that causes issues'''
                self.column0 = QLineEdit(str(textc[i])) 
                a1 = QtWidgets.QTableWidgetItem(a1)

                try:
                    '''Only the first column should work with cell widget.
                    Second column (price breaks) cannot process cell widgets'''
                    if(i == COLUMN_ZERO and b == 0 and textc[i] != ""): ##Should be first column
                        ###Need to active QCompleter to get completions suggestions to come up
    #                    self.TableQuote.cellWidget(n+a,i+b).text() = a1

                        ##############this is basically completer stuff again ######################
                        conn =connectSQLite() ## Defined from *star imports, this is OK
                        cur = conn.cursor()
                
                        cur.execute("SELECT PartNumber FROM Part ORDER BY PartNumber ASC")
                        part = cur.fetchall()
                        closeSQLite(conn)
                        listpart = []
                        for prt in part:
                            for p in prt:
                                listpart.append(str(p)) 
                        '''
                        Assign QCompleter - a completion widget, with all parts in SQLite database into the table cell widget
                        '''
                        cmpt = QCompleter(listpart) 
                        cmpt.setCaseSensitivity(0)   
                        
#                        testB = QLineEdit(words)
                        self.column0.setCompleter(cmpt)
                        print("if, self.column0: ", self.column0)
                        self.TableQuote.setCellWidget(n+a,i+b, self.column0)
                    else:
                        print("else, self.column0: ", self.column0)
                        self.TableQuote.setItem(n+a,i+b,a1)

                except Exception as ex:
                    printError(ex)
                    
                i = i + 1            
            n = n + 1
    
    def PBClearContent(self):
        
        self.TableQuote.clearContents()
        self.currentrow = 0
        self.currentcolumn = 0
        self.copy = 0
        conn =connectSQLite() ## Defined from *star imports, this is OK
        cur = conn.cursor()

        cur.execute("SELECT PartNumber FROM Part ORDER BY PartNumber ASC")
        part = cur.fetchall()
        closeSQLite(conn)
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
            
        
    
    '''Checks whether a part number is valid, I.E. if query can return a description it exists'''
    def isPartNumberValid(self):
        conn =connectSQLite()
        cur = conn.cursor()

        partNumberValid = True
        cur.execute("SELECT Description FROM Part WHERE PartNumber = ?",(self.partnumber,))
        desc = cur.fetchone()
        closeSQLite(conn)
        
        if desc == None:
            print("part number is not in the database: ", self.partnumber)
            partNumberValid = False
        self.partNumberValid = partNumberValid


        
            
    def PBQuote(self):
        self.missingPNs = list()
        self.allPNs = list()
        self.numOps = list() #Contains the number of operations in order.
        self.QTYList = list()
        self.unitPriceList = list()
        
        #Contains all part numbers, but making substitutions if there is a duplicate. A 
        ##A second list isrequired, as allPNs is used to lookup exact match PN in SQLite database
        self.allPNwithDuplicates = list()
        
        
        #Total price is always on 24 + # operations
        #Need to keep number of operations independent so its tied to part number, but can't use dictionary in case duplicates of part number
        
        # try :
        #     self.skipQuote = False #Does this do anything at all??
        #     ligne = 0
        #     while ligne <= 99 :

        #         if self.copy == 0:
        #             if self.TableQuote.cellWidget(ligne,0).text() != "": 
        #                 self.partnumber = self.TableQuote.cellWidget(ligne,0).text()
        #             else:
        #                 break
               
        #         ## if copy == 1, then cell is just a free text cell
        #         elif self.copy == 1 :
        #             try:
        #                 if(self.TableQuote.item(ligne,0) and self.TableQuote.item(ligne,0).text() != "" ):
        #                     self.partnumber = self.TableQuote.item(ligne,0).text()
        #                 elif(self.TableQuote.cellWidget(ligne,0) and self.TableQuote.cellWidget(ligne,0).text() != "" ):
        #                     self.partnumber = self.TableQuote.cellWidget(ligne,0).text()
        #                 else:
        #                     break
        #             except Exception as ex:
        #                 printError(ex)

        #         else : ###New Code
        #             self.isPartNumberValid()
        #             break
                
        #         ligne = ligne + 1
        # except Exception as ex : 
        #     printError(ex)
        #     QMessageBox.warning(self, "Warning", "Error during treatment of the part number entered.")
        #     return


        self.setExportTitle()
        self.setDesktopPath()
        self.createExcelFile()
        self.formatExcelFile()
        self.createFolder()
        

        
        



        self.newrawmat = 0
        ligne = 0
        while ligne <= 99 :
            # self.partNumberValid = True

            try :
                print("self.copy: ", self.copy)

                if self.copy == 0:
                    if self.TableQuote.cellWidget(ligne,0).text() != "": 
                        self.partnumber = self.TableQuote.cellWidget(ligne,0).text()
                    else:
                        break                
                ## if copy == 1, then cell is just a free text cell
                elif self.copy == 1 :
                    try:
                        if(self.TableQuote.item(ligne,0) and self.TableQuote.item(ligne,0).text() != "" ):
                            self.partnumber = self.TableQuote.item(ligne,0).text()
                        elif(self.TableQuote.cellWidget(ligne,0) and self.TableQuote.cellWidget(ligne,0).text() != "" ):
                            self.partnumber = self.TableQuote.cellWidget(ligne,0).text()
                        else:
                            break                    

                    except Exception as ex:
                        printError(ex)
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                self.isPartNumberValid()
                self.allPNs.append(self.partnumber)
                
            except Exception as ex :
                printError(ex)
                QMessageBox.warning(self, "Warning", "Error (2.2) while proccessing the Part number.")
                    

            #MAT CHANGE of the given line
            self.setNewMaterialCost(ligne)

            self.makeSafePartNumber(ligne)

            self.writeExcelHeader()



            self.colQty = list()

            if(self.partNumberValid):
                conn =connectSQLite()
                cur = conn.cursor()     

                try : #####################################################
                #########Each ligne/line is a row /part number #############
                #########Each colonne/column is a column/price break##########
                    colonne = 1
                    # print('colonne ::', colonne)
                    while colonne <= 10:
                        try:
                            if(self.TableQuote.item(ligne,colonne) and self.TableQuote.item(ligne,colonne).text() != '' ):
                                # print("something is here")
                                self.qty = int(self.TableQuote.item(ligne,colonne).text())
                                # print("qty: ", self.qty)
                                self.colQty.append(self.qty)
                            ###First column, price break 1, is required
                            elif colonne == 1:
                                print("part is missing first price break : ", self.printpart, self.partnumber)
                                QMessageBox.warning(self, "Warning", "Price break qty missing: " + self.partnumber)
                                #do not assign qty = 0
                                self.colQty.append(0)
    #                            
                                break
                            ###Second column and on is not required, do not notify user
                            else:
                                #do not assign qty = 0
                                self.colQty.append(0)
                                break
                        except ValueError:
                            QMessageBox.warning(self, "Warning", "Please ensure price break contains numbers only. No letters or ,")

#                        print("past the break point!!!!!!!!!!!")

                        self.getNumberOps(cur)
                        


                        MAT_LOC = 0
                        DIAM_LOC = 1
                        SHANK_LOC = 2

                        ISNUT_LOC = 42
                        ISSTUD_LOC = 43

                        requestA = "SELECT Material, Diam, Shank, Op2, Op3, Op4, Op5, Op6, Op7, Op8, Op9, Op10, Op11, Op12, Op13, Op14, Op15, Op16, Op17, Op18, Op19, Op20, Op21, Op22, Op23, Op24, Op25, Op26, Op27, Op28, Op29, Op30, Op31, Op32, Op33, Op34,Op35, Op36, Op37, Op38, Op39, Op40,isNut,isStud FROM Part WHERE PartNumber = ?"
                        cur.execute(requestA, (self.partnumber,))

                        Part = cur.fetchone()

                        self.mat = str(Part[MAT_LOC])
                        # self.mat = mat
                        self.diam = Part[DIAM_LOC]




                        if(Part[ISNUT_LOC] == 1):
                            self.isNut = True
                        else:
                            self.isNut = False
                        if(Part[ISSTUD_LOC] == 1):
                            self.isStud = True
                        else:
                            self.isStud = False

                        if(self.isNut):
                            self.shank = 0
                        else:
                            self.shank = Part[SHANK_LOC]

                        ### Put operations in op list####################
                        try:
                            op = list()        
                            n = 3
                            nOffset = n

                            while n < (self.synopticNumOps + nOffset):
                                operation = Part[n]
        #                            print("operation to check ", operation)
                                if operation == 0 or operation == "" or operation == 100: ## add or operation == 100 #3/1/19, 100 gets added to each op
                                    # print("Breaky breaky achey")
                                    break
                                else:
                                    # print("operation to append to lowercase op: ", operation)
                                    op.append(operation)           
                                n = n+1

                        except Exception as ex:
                            printError(ex)
                        #####################################################

                        #######find material stuff########################
                        cur.execute("SELECT Type,Groupe,Cost FROM Mat WHERE Number = ?",(self.mat,))
                        Mat = cur.fetchone()
                        
                        try:    
                            self.mattype = str(Mat[0])
                            self.matgroupe = str(Mat[1])
                            self.matcost = Mat[2]
                            if (self.matcost == 0 or self.matcost == 0.0):
                                QMessageBox.warning(self, "Warning", "Material cost is 0 for "+self.mat+ " for p/n: "+ self.partnumber)

                        except Exception as ex :

                            printError(ex)
                            message = "Material number: " + self.mat + " is missing."
                            QMessageBox.warning(self, "Warning", message)
                        #############################################

                        #########set scrap
                        try:
                            self.calculateScrap() #Sets self.scrap
                        except Exception as ex:
                            printError(ex)

                        ###Override raw material cost if entered into UI ####
                        try:
                            if self.newrawmat != None and self.newrawmat != 0 :
                                self.matcost = int(self.newrawmat)
                        except Exception as ex:
                            printError(ex)
                        ####################################

                        ####Lookup setupcost, cost #########
                        try:
                            self.setupcost,self.cost = trouvercout(self.matgroupe,self.diam)
                        except Exception as ex:
                            printError(ex)

                        #####################################
                        Opname = list()
                        Opmin = list()
                        Opunit = list()
                        self.Opsetup = list()
                        Opcost = list()
                        op_list = [138,142,144,148,150,155,156,157,164,165,167,168,169,170,171,172,185,191,203,205,206,208,213,214,215,216,217,224,226,227,234,237,238,241,244,247,250,252,253,255,259,267,268,275,278,285,288,294,295,297,304,307,312,313,314,315,318,324,327,328,332,334,335,341,348,350,352,356,357,360,361,362,366,372,373,374,379,380,381,382,386,387,389,392,393,394,395,396,397,398,399,403,404,406,425,427,428,429,434,436,442,444,445,446,451,452,453,454,456,460,462,464,466,468,473,475,477,480,483,485,486,487,488,490,491,493,494,501,508,511,523,527,535,541,543,546,559,561,576,583,591,592,599,606,619,620,621,626,627,638,650,652,653,654,655,656,657,658,659,661,663,669,670,673,675,679,680,695,696,699,700,701,702,704,706,709,715,716,719,720,721,723,724,725,738,739,740,741,742,743,745,746,754,759,760,761,762,763,766,768,770,771,772,773,774,775,776,777,778,779,783,785,786,787,788,789,792,793,794,798,799,800,803,804,805,806,807,808,811,812,813,814,815,821,824,827,828,829,831,837,841,842,845,846,850,852,858,859,861,866,867,868,869,872,873,874,875,876,877,878,893,895,897,899,915,916,917,919,921,922,925,941,944,945,949,950,954,957,960,964,972,977,980,981,984,986,987,988,993,994,995,996,997,1000,1001,1004,1005,1022,1023,1024,1025,1032,1034,1036,1037,1040,1041,1042,1043,1044,1045,1046,1047,1050,1051,1052,1053,1057,1058,1059,1060,1061,1063,1064,1067,1069,1070,1071,1072,1073,1074,1092,1093,1094,1099,1100]
                        Spec_op_setupcost = list()
                        Spec_op_cost = list()
                          
                        n = 0
                        #####For each operation, lookup values and append to respective list #######
                        while n < len(op) :
                            pn = str(op[n])
                            try : 
                                cur.execute("SELECT Name, Min, Unit,%s,%s FROM Op WHERE Number = ?" %(self.setupcost,self.cost),(pn,))
                                Op = cur.fetchone()
                                
                                if int(pn) in op_list:
                                    Spec_op_cost.append(Op[4])
                                    Spec_op_setupcost.append(Op[3])
                                else:
                                    Spec_op_setupcost.append(0)
                                    Spec_op_cost.append(0)

                                
                                Opname.append(Op[0])
                                if Op[1] == "":
                                    Opmin.append(0)
                                else :
                                    Opmin.append(Op[1])
                                Opunit.append(Op[2])
                                if Op[3] == "":
                                    self.Opsetup.append(Op[3])
                                else :
                                    self.Opsetup.append(Op[3])
                                    
                                Opcost.append(Op[4])
                            except Exception as ex:
                                printError(ex)
    #                                n = n + 1 #This was remove 03/01/2019 @ 3:40 PM
                            
                            n = n + 1
                        ###########################################################



                        try:
                            self.calculateSETUP() ##self.SETUP

                            self.calculateHeadVol()

                            self.calculateSlugLength()


                            PW = calculatePW(self.mattype, self.SLUG, self.diam)

                            # print("PW: ", PW)
                        except Exception as ex:
                            errorMessage = str(ex)
                            # errorArgs = ex.args
                            # print('errorArgs: ', errorArgs)
                            # print("errorMessage: ", errorMessage)

                            QMessageBox.warning(self, "Warning", errorMessage)

                            printError(ex)

                # '''creation of the cost list and calculation of the subtotal                '''

                ###
                #Scrap process cost is 0 if the cost/pc * qty is < minimum lot
                #the minimum lot already includes padding for scrap processing cost.
                        SCRAPPROCBOOL = False
                        try: 
                            listprocess = list()
                            scrapprocess = list() #scrapprocess is list process EXCLUDING cost/pc*qty < minimum lot
                            coutprocess = 0
        
                            n = 0
                            while n < len(op) :
                                setup = self.Opsetup[n]
                                setup = setup/self.qty
                                
                                unit = str(Opunit[n])
                                if unit == "pc" :
                                    
                                    cost = Opcost[n]
                                    
                                elif unit == "lb":
                                    # print("PW: ", PW)
                                    cost = Opcost[n]
                                    cost = cost * PW
                                    
                                minimumlot = Opmin[n]
                                minimumlot = minimumlot/self.qty
                                opmin = Opmin[n]

                                if ((cost * self.qty) < opmin):
                                    SCRAPPROCBOOL = True
                                else:
                                    SCRAPPROCBOOL = False
                                ####Per JPN - cost is always cost
                                #### SETUP is calculated separately in its own column/row called set-up / pc
                                coutprocess = cost

                                if coutprocess > minimumlot:
    #                                    print("c coutprocess > minimumlot: ", coutprocess, ">", minimumlot)
                                    coutprocess = coutprocess 
                                else : 
                                    coutprocess = minimumlot
    #                                    print("d coutprocess < minimumlot: ",coutprocess,"<", minimumlot)
                                
                                if Opcost[n] == 0:
                                    coutprocess = 0
                                
                                listprocess.append(coutprocess)
                                if(not SCRAPPROCBOOL):
                                    scrapprocess.append(coutprocess)

                                n = n+1
                                
                        except IndexError as errorVariable2:
                            if hasattr(errorVariable2, 'errno'):
                                print ("reason: ", errorVariable2.errno)
                            if hasattr(errorVariable2, 'code'):
                                print("code: ", errorVariable2.code)
                            if hasattr(errorVariable2, 'reason'):
                                print("reason: ", errorVariable2.reason)
                            printError(errorVariable2)

                            
                        except Exception as q:
                            printError(q)


                        try: 
                            SUBTOTAL = sum(listprocess)
                            SUBTOTAL_FOR_SCRAP_PROC = sum(scrapprocess)
                            SUBTOTAL = round(SUBTOTAL,3)
        
                    # Calcul Raw mateiral cost per piece
        
                            RAWMATCOST = PW * self.matcost
        
                            RAWMATCOST = round(RAWMATCOST,3)
                
                    # Calcul du scrap allowance material cost per piece
                            # PW = part weight
                            # scrap = scrap quantity
                            # matcost = $dollars / pound
                            # qty = quantity ordered/ desired
                            SCRAPMATCOST = (((PW * self.scrap)*self.matcost)/self.qty)
    #                            print("Scrapmatcost: ", SCRAPMATCOST)
                            SCRAPMATCOST = round(SCRAPMATCOST,3)
        
                    # Calcul du scrap allowance processus cost per piece   
                            #
                            #SCRAPPROCCOST = 0 IF QTY * COST/PC < MIN LOT COST ######################
                            SCRAPPROCCOST = (((SUBTOTAL * 0.5)*self.scrap)/self.qty)
                            SCRAPPROCCOST = (((SUBTOTAL_FOR_SCRAP_PROC * 0.5)*self.scrap)/self.qty)
    #                            print("Scrap process cost: ", SCRAPPROCCOST)
    #                            print("SUBTOTAL: ", SUBTOTAL)
    #                            print("scrap: ", scrap)
    #                            print("qty: ", qty)
                            SCRAPPROCCOST = round(SCRAPPROCCOST,3)
    
    ###This section should be superceded by using scrapprocess list (SUBTOTAL_FOR_SCRAP_PROC) instead.
                            #If for every part qty order * cost/piece (or cost / lb) is <= minimum lot cost then
                            #scrap process cost is $0 as it scrap prcoess allowance is already factored into minimum lot costs
    ###                            if(SCRAPPROCBOOL):
    ###                                SCRAPPROCCOST = 0




                    ############COST LIST and CALCULATE SUBTOTAL ##########
        
                            qtytotal = self.qty + self.scrap
                            
                            longueurtotal = (self.SLUG + 0.04) * qtytotal
                            
                            nbbar = longueurtotal / 144 
                            
                            nbbartotal = int(nbbar)+1
                            
                            nbbarperdu = nbbartotal - nbbar 
                            
                            longueurperdu = (nbbarperdu * 144) + ( self.scrap * 0.04 )

                            '''This calculates PW of scrap
                            languer perdu is "Length Lost"
                            normally this would be slug
                            def calculatePW(mattype, SLUG, diam):

                            '''
                            lossw = calculatePW(self.mattype, longueurperdu, self.diam)


                            LOSS = (lossw * self.matcost) / qtytotal
                            
                            LOSS = round(LOSS,3)
                        except Exception as ex:
                            printError(ex)
                        ##################################################



                        ################calculate final cost#################
                        try:
                            TOTAL = SUBTOTAL + self.SETUP + RAWMATCOST + SCRAPMATCOST + SCRAPPROCCOST + LOSS
                            
                            TOTAL= round(TOTAL,3)
                            
                            Miscellaneous = TOTAL * 0.10
                            
                            TOTALMFG = TOTAL + Miscellaneous
    
    #                       MINCOSTVALUE = 5000 #Per Mike Ross 1/11/2019
                            MINCOSTVALUE = 6000 #Per Shannon Ouelette 08/12/2019
                            MARGE = 30
        
                            
                            PRX = TOTALMFG/((100-MARGE)/100)
                            Finalresult = PRX * self.qty
            
                            if Finalresult < MINCOSTVALUE :
            
                                while Finalresult <= MINCOSTVALUE :
                                    
                                    MARGE = MARGE + 1
                                    PRX = TOTALMFG/((100-MARGE)/100)
                                    Finalresult = PRX * self.qty

                            ##################################################

                             ############Calculate Total Raw Material Cost######
                            TOTAL_RAW_MAT_COST = RAWMATCOST + SCRAPMATCOST + LOSS
                            print("TOTAL_RAW_MAT_COST: ", TOTAL_RAW_MAT_COST)

                            '''
                            Raw Material % Total cost is Total Raw Material Costs (Raw Material, Scrap Material, Material Loss)
                            Divided by
                            Total Manufacturing COST

                            Update 11/15/19 per Phil Stella
                            Total Raw Mat Cost / total unit Price
                            As unit price is based on Margin this has to be dynamically calculated now
                            '''
                            # self.RAW_MAT_PERC_TOTAL_COST = ( TOTAL_RAW_MAT_COST / PRX)

                            # print("self.RAW_MAT_PERC_TOTAL_COST: ", self.RAW_MAT_PERC_TOTAL_COST)

###################################################WRITE QUOTE for Each Price Break(colonne) #####################
                            self.feuille.write(9,(3+colonne),self.qty)
                            self.feuille.write(10,(3+colonne),self.scrap)
                            self.feuille.write(11,(3+colonne),qtytotal)
                            
                            ii = 0
                            print("len(listprocess):############## ", len(listprocess))
                            while ii <= len(listprocess)-1 :
                                
                                k = int(ii)
                                self.feuille.write((13+k),(3+colonne),listprocess[ii])
                                
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
                        except Exception as ex:
                            printError(ex)
    #                            print("error D")
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
                        except Exception as ex:
                            printError(ex)
                            print("error C")
                        try:
                            self.feuille.write((13+k+2),(3+colonne),'=SUM(%s:%s)'%(debut,fin) , self.currency_format)
                            self.feuille.write((13+k+3),(3+colonne),self.SETUP, self.currency_format)
                            self.feuille.write((13+k+4),(3+colonne),RAWMATCOST, self.currency_format)
                            self.feuille.write((13+k+5),(3+colonne),SCRAPMATCOST, self.currency_format)
                            self.feuille.write((13+k+6),(3+colonne),SCRAPPROCCOST, self.currency_format)
                            self.feuille.write((13+k+7),(3+colonne),LOSS, self.currency_format)
                            self.feuille.write((13+k+8),(3+colonne),'=SUM(%s:%s)'%(debuttot,fintot), self.currency_format)
                            self.feuille.write((13+k+9),(3+colonne),'=%s*1.1'%(supertot), self.currency_format)
                            self.feuille.write((13+k+10),(3+colonne),MARGE, self.red_format)
                            self.feuille.write((13+k+11),(3+colonne),'=%s/((100-%s)/100)'%(mfgtotal,mrgtot), self.final_currency_format)
                            self.feuille.write((13+k+12),(3+colonne),'=(%s*%s)'%(prxtot,self.qty), self.final_currency_format)
                            #RAW_MAT_PERC_TOTAL_COST = ( TOTAL_RAW_MAT_COST / PRX)
                            # TOTAL_RAW_MAT_COST = RAWMATCOST + SCRAPMATCOST + LOSS  / prxtot
                            # self.feuille.write((13+k+13),(3+colonne),self.RAW_MAT_PERC_TOTAL_COST,self.percent_format)
                            self.feuille.write((13+k+13),(3+colonne),'=(((%s+%s+%s)/(%s))*100)'%(RAWMATCOST, SCRAPMATCOST,LOSS,prxtot),self.red_format)
                            self.feuille.write((13+k+14),(3+colonne),self.qty)
                            self.feuille.write((13+k+15),(3+colonne),'=((%s/%s)+(%s))'%(sum(Spec_op_setupcost),self.qty,sum(Spec_op_cost)), self.currency_format)
                            self.feuille.write((13+k+16),(3+colonne),'=(((%s/%s)+(%s))/(%s/((100-%s)/100))*100)'%(sum(Spec_op_setupcost),self.qty,sum(Spec_op_cost),mfgtotal,mrgtot),self.red_format)
                            print("prxtot: ", prxtot)

                        except Exception as ex:
                            printError(ex)
    #                            print("error b")
                        try:
                            self.unitPriceList.append(prxtot)
                        except Exception as ex:
                            printError(ex)


                        colonne = colonne+1
                    ##################################
                    try:
                        self.numOps.append(self.synopticNumOps)
    #                    print("self.colQty: ", self.colQty)
                    except Exception as ex:
                        printError(ex)
                    
                    try:
                        self.QTYList.append(self.colQty)
                    except Exception as ex:
                        printError(ex)
    #                    print("self.QTYList: ", self.QTYList)


                except TypeError as ex: ##########################################
                    printError(ex)
                    QMessageBox.warning(self, "Warning", "Type Error (2.3) in the computation process.")                

#
                   
                try:
                    self.feuille.write((13+k+2),3,'Subtotal process :')
                    self.feuille.write((13+k+3),3,'Set up cost:')
                    self.feuille.write((13+k+4),3,'Raw Matl cost:')
                    self.feuille.write((13+k+5),3,'Scrap Matl cost :')
                    self.feuille.write((13+k+6),3,'Scrap Process cost :')
                    self.feuille.write((13+k+7),3,'Matl Loss cost :')
                    self.feuille.write((13+k+8),3,'Total:')
                    self.feuille.write((13+k+9),3,'Total Mfg:')
                    self.feuille.write((13+k+10),3,'Marge ( % ):')
                    self.feuille.write((13+k+11),3,'Price:')
                    self.feuille.write((13+k+12),3,'Total Value:')
                    self.feuille.write((13+k+13),3,'Raw Matl % Price: ')
                    self.feuille.write((13+k+14),3, 'Req Qty :')
                    self.feuille.write((13+k+15),3, 'Total OP Cost :')
                    self.feuille.write((13+k+16),3, 'OP % :')
                except Exception as ex:
                    printError(ex)

                self.findPartInfo(cur)
                self.findEstimator()
                self.findMaterialInfo(cur)





                try:
                    self.feuille.write(3,1,self.partNote,self.note_format)
                    self.feuille.write(4,1,self.partnumber)
                    self.feuille.write(5,1,self.partRev)
                    self.feuille.write(6,1,self.partDesc,self.bold_format)
                    self.feuille.write(7,1,self.partMfgSpec)
                    # self.feuille.write(8,1,self.partNote)
                    self.feuille.write(9,1,self.creationDate) #creation date
                    self.feuille.write(10,1,self.estimator) #Estimator
                    self.feuille.write(11,1,getpass.getuser())



                    self.feuille.write(4,4,self.matnamespec, self.note_format)
                    self.feuille.write(5,4,self.matcost, self.bold_format)
                    self.feuille.write(6,4,self.diam, self.bold_format)
                    self.feuille.write(7,4,PW, self.bold_format)
                    self.feuille.write(4,7,self.SLUG, self.bold_format)
                    self.feuille.write(5,7,self.HDVOL, self.bold_format)
                    self.feuille.write(6,7,self.shank, self.bold_format) #DO NOT USE part[5] shank is checked earlier in the program because Nuts have no shank length
                    self.feuille.write(4,9,self.isNut, self.bold_format)
                    self.feuille.write(5,9,self.isStud, self.bold_format)
                    self.feuille.write(6,9,not(self.isNut or self.isStud), self.bold_format)
                except Exception as ex:
                    printError(ex)                
                try:
                    i = 0
                    while i <= len(Opname)-1 :
                        
                        k = int(i)
                        self.feuille.write((13+k),1,Opname[i])
        
                        i = i+1
                except Exception as ex:
                    printError(ex)
                    
                ligne = ligne+1  

            ##This fires if self.partNumberValid is false
            else: ##Not skipQuote
#                print("else statement of self.partvalid")
                try:
                    self.numOps.append(0)
                    self.colQty = [0]
                    self.QTYList.append(self.colQty)
                    self.unitPriceList.append(0)
    #                self.QTYList.append(0)
                except Exception as ex:
                    printError(ex)
                    print("Part is invalid. Additional errors.")
                    
                if(not self.partNumberValid):
                        self.missingPNs.append(self.partnumber)
                ligne = ligne + 1
        
        if( len(self.missingPNs) != 0 ):
#            print("len(self.missingPNs): ", len(self.missingPNs))
#            print("self.missingPNs: ", self.missingPNs)
            try:
                if(self.missingPNs[0] == ""):
                    QMessageBox.warning(self, "Warning", "One or all partnumbers is blank.")
                else:
#                    print("self.missingPNs: ", self.missingPNs)
                    toPrintString = None
                    for x in self.missingPNs:
                        if(toPrintString is None):
                            toPrintString = str(x)
                        else:
                            toPrintString = toPrintString +", " +str(x)
#                    print("toprintstring: ", toPrintString)
                    QMessageBox.warning(self, "Warning", "The following partnumber(s) do not exist in the database: " + toPrintString)
                    print(self.missingPNs)
            except Exception as ex:
                printError(ex)
                QMessageBox.warning(self, "Warning", "Unable to show missing part numbers." )
            
        ##########################################SUMMARY#####################
        try:
#            rowOfTotal = 0
            summary = self.workbook.add_worksheet("Summary")
            summary.set_column('A:A',30)
            summary.set_column('B:K',15)
            # self.feuille.set_column('A:K', 20)
            ##HEADER INFORMATION
            summary.write(0, 0, "All PNs")
            summary.write(0, 1, "Price Break 1")
            summary.write(0, 2, "Price Break 2")
            summary.write(0, 3, "Price Break 3")
            summary.write(0, 4, "Price Break 4")
            summary.write(0, 5, "Price Break 5")
            summary.write(0, 6, "Price Break 6")
            summary.write(0, 7, "Price Break 7")
            summary.write(0, 8, "Price Break 8")
            summary.write(0, 9, "Price Break 9")
            summary.write(0, 10, "Price Break 10")





            for i in range(len(self.allPNs)):
#                print("i : ", i)

                # for x in self.unitPriceList:
                #     print(x)
                rowOfTotal = None

                rowOfUnitPrice = 24+self.numOps[i]
                rowOfTotal = 25+self.numOps[i]
#                rowOfTotal = 25+self.numOps
#                print("self.numOps[i]: ", self.numOps[i])
#                print("self.numOps[i]: ", self.numOps)
                rowOfTotal1 = "E"+str(rowOfTotal)
                rowOfTotal2 = "F"+str(rowOfTotal)
                rowOfTotal3 = "G"+str(rowOfTotal)
                rowOfTotal4 = "H" +str(rowOfTotal)
                rowOfTotal5 = "I"+str(rowOfTotal)
                rowOfTotal6 = "J"+str(rowOfTotal)
                rowOfTotal7 = "K"+str(rowOfTotal)
                rowOfTotal8 = "L"+str(rowOfTotal)
                rowOfTotal9 = "M" +str(rowOfTotal)
                rowOfTotal10 = "N"+str(rowOfTotal)





                rowOfUnitPrice1 = "E"+str(rowOfUnitPrice)
                rowOfUnitPrice2 = "F"+str(rowOfUnitPrice)
                rowOfUnitPrice3 = "G"+str(rowOfUnitPrice)
                rowOfUnitPrice4 = "H"+str(rowOfUnitPrice)
                rowOfUnitPrice5 = "I"+str(rowOfUnitPrice)
                rowOfUnitPrice6 = "J"+str(rowOfUnitPrice)
                rowOfUnitPrice7 = "K"+str(rowOfUnitPrice)
                rowOfUnitPrice8 = "L"+str(rowOfUnitPrice)
                rowOfUnitPrice9 = "M"+str(rowOfUnitPrice)
                rowOfUnitPrice10 = "N"+str(rowOfUnitPrice)





#                print("rowOfTotal", rowOfTotal)
                
                CONSTANT_FIRST = 1
                CONSTANT_SECOND = 2
                CONSTANT_THIRD = 3
                if(i==0):
                    FIRST = CONSTANT_FIRST
                    SECOND = CONSTANT_SECOND
                    THIRD = CONSTANT_THIRD
                    # OFFSET = 4
                    summary.write(FIRST, 0, "For Quantity: ")
                    for q in range(len(self.QTYList[0])):
                        summary.write(FIRST, q+1, self.QTYList[i][q]) #write Quantity
                        # summary.write(FIRST, q+1+OFFSET, self.QTYList[i][q]) #re-write quantity for unit prices

#                    summary.write(FIRST, 1, self.QTYList[i][0])
#                    summary.write(FIRST, 2, self.QTYList[i][1])
#                    summary.write(FIRST, 3, self.QTYList[i][2])
#                    summary.write(FIRST, 4, self.QTYList[i][3])
                        
#                    ##Does not work with duplicate part numbers
#                    summary.write(SECOND, 0, self.allPNs[i])
#                    summary.write(SECOND, 1, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal1))
#                    summary.write(SECOND, 2, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal2))
#                    summary.write(SECOND, 3, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal3))
#                    summary.write(SECOND, 4, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal4)) 
#                    ##


                    summary.write(SECOND, 0, str(self.allPNwithDuplicates[i])+" unit price")
                    summary.write(SECOND, 1, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice1),self.currency_format)
                    summary.write(SECOND, 2, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice2),self.currency_format)
                    summary.write(SECOND, 3, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice3),self.currency_format)
                    summary.write(SECOND, 4, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice4),self.currency_format)
                    summary.write(SECOND, 5, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice5),self.currency_format)
                    summary.write(SECOND, 6, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice6),self.currency_format)
                    summary.write(SECOND, 7, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice7),self.currency_format)
                    summary.write(SECOND, 8, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice8),self.currency_format)
                    summary.write(SECOND, 9, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice9),self.currency_format)
                    summary.write(SECOND, 10, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice10),self.currency_format)



                    summary.write(THIRD, 0, str(self.allPNwithDuplicates[i])+ " total price")
                    summary.write(THIRD, 1, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal1),self.currency_format)
                    summary.write(THIRD, 2, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal2),self.currency_format)
                    summary.write(THIRD, 3, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal3),self.currency_format)
                    summary.write(THIRD, 4, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal4),self.currency_format)
                    summary.write(THIRD, 5, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal5),self.currency_format)
                    summary.write(THIRD, 6, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal6),self.currency_format)
                    summary.write(THIRD, 7, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal7),self.currency_format)
                    summary.write(THIRD, 8, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal8),self.currency_format)
                    summary.write(THIRD, 9, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal9),self.currency_format)
                    summary.write(THIRD, 10, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal10),self.currency_format)



                else:
                    FIRST = 3*i + CONSTANT_FIRST
                    SECOND = 3*i + CONSTANT_SECOND
                    THIRD = 3*i + CONSTANT_THIRD

                    summary.write(FIRST, 0, "For Quantity: ")
#                    if(self.QTYL)
#                    for q in range(len(self.QTYList[0])): ##Do not use this
                    for q in range(len(self.QTYList[i])):  ##Using "i" index makes sure to get the length of the sublist contained in the list of lists so you don't get an IndexError
#                        print("i: ", i)
#                        print("q: ", q)
                        summary.write(FIRST, q+1, self.QTYList[i][q])

#                    summary.write(FIRST, 1, self.QTYList[i][0])
#                    summary.write(FIRST, 2, self.QTYList[i][1])
#                    summary.write(FIRST, 3, self.QTYList[i][2])
#                    summary.write(FIRST, 4, self.QTYList[i][3])
                        
#                    ##Does not work with duplicate PNs in same quote
#                    summary.write(SECOND, 0, self.allPNs[i])
#                    summary.write(SECOND, 1, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal1))
#                    summary.write(SECOND, 2, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal2))
#                    summary.write(SECOND, 3, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal3))
#                    summary.write(SECOND, 4, "=\'"+str(self.allPNs[i]+"\'"+"!"+rowOfTotal4))
                    
                    summary.write(SECOND, 0, str(self.allPNwithDuplicates[i])+" unit price")
                    summary.write(SECOND, 1, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice1),self.currency_format)
                    summary.write(SECOND, 2, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice2),self.currency_format)
                    summary.write(SECOND, 3, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice3),self.currency_format)
                    summary.write(SECOND, 4, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice4),self.currency_format)
                    summary.write(SECOND, 5, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice5),self.currency_format)
                    summary.write(SECOND, 6, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice6),self.currency_format)
                    summary.write(SECOND, 7, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice7),self.currency_format)
                    summary.write(SECOND, 8, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice8),self.currency_format)
                    summary.write(SECOND, 9, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice9),self.currency_format)
                    summary.write(SECOND, 10, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfUnitPrice10),self.currency_format)



                    summary.write(THIRD, 0, str(self.allPNwithDuplicates[i])+ " total price")
                    summary.write(THIRD, 1, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal1),self.currency_format)
                    summary.write(THIRD, 2, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal2),self.currency_format)
                    summary.write(THIRD, 3, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal3),self.currency_format)
                    summary.write(THIRD, 4, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal4),self.currency_format)
                    summary.write(THIRD, 5, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal5),self.currency_format)
                    summary.write(THIRD, 6, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal6),self.currency_format)
                    summary.write(THIRD, 7, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal7),self.currency_format)
                    summary.write(THIRD, 8, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal8),self.currency_format)
                    summary.write(THIRD, 9, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal9),self.currency_format)
                    summary.write(THIRD, 10, "=\'"+str(self.allPNwithDuplicates[i]+"\'"+"!"+rowOfTotal10),self.currency_format)

                    
        except IndexError as w:
            printError(w)
            # if hasattr(w, 'errno'):
            #     print ("reason: ", w.errno)
            # if hasattr(e, 'code'):
            #     print("code: ", w.code)
            # if hasattr(e, 'reason'):
            #     print("reason: ", w.reason)
            # print("Error G2: ", traceback.format_exc())            
#            print("Cannot generate summary due to error." + w)
        except Exception as ex:
            printError(ex)
        #####################END SUMMARY #########################################
            
        self.closeWorkbook()

        self.openExcelFile(conn)

            
        return





    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Equations per Jean-Paul Nicolle
    # if cost > 100 they take a lot more precautions on reworking and not scrapping parts
    ## as material cost goes down, in general, it's better to scrap than to try to rework a part
    ##E.G. as material cost goes down, scrap (and thus total parts) goes up
    def calculateScrap(self):
        if(self.matcost > 0 and self.qty > 0):
            if self.matcost >= 100:
                self.scrap = int (25 + (self.qty + 25) * 0.062)
            elif self.matcost >= 22:
                # if cost > 22
                self.scrap = int(40 + (self.qty + 40) * 0.062)
            else:
                #Original synoptic is 40, this is more conservative per JP
                self.scrap = int(56 + ((self.qty + 56) * 0.062))
        else:
            raise ValueError("Error with material cost or quantity.")


        # return scrap

    '''
    Calculate head volume
    '''
    def calculateHeadVol(self):
        if(self.isNut and self.isStud):
            raise ValueError(self.partnumber +"is both a stud AND a nut!!!")
        elif(self.diam <= 0):
            raise ValueError(self.partnumber + " diameter is <= 0 ")
        else:
            if(self.isNut):
                HDVOL = self.diam * 2.0
            #STUD
            elif(self.isStud):
                HDVOL = 0
            #Regular BOLT
            else:
                HDVOL = self.diam * 2.2

        HDVOL = round(HDVOL,3)
        self.HDVOL = HDVOL
        # return HDVOL

    '''
    Calculate the slug length - the overall length
    including head and shank
    '''
    def calculateSlugLength(self):
        SLUG = self.HDVOL +self.shank
        
        SLUG = round(SLUG,3)
        self.SLUG = SLUG
        # return SLUG

    def setExportTitle(self):
        e = datetime.now()
        timestamp = str(e.month)+"-"+str(e.day)+"-"+str(e.year)+"--"+str(e.hour)+"h-"+str(e.minute)+"m"
                
        self.titleexport = 'ExportQuote '+str(timestamp)+'.xlsx'
        self.timestamp = timestamp

    def setDesktopPath(self):
        try :
            self.desktoppath = os.path.join(os.path.expanduser("~"), "Desktop")
        except : 
            QMessageBox.warning(self, "Warning", "Could not find desktop path.")
            return



    ##Define save path for .XLSX file name saved in titleexport variable
    def createExcelFile(self):
        try:
            self.way = str(self.desktoppath)+"\\Export-CES\\"+str(self.titleexport)

            self.workbook = xlsxwriter.Workbook(self.way)
        except Exception as ex :
            printError(ex)
            print("desktoppatherror")

    '''
    Perform Excel formatting
    Things like bold, fill, border, text color, size
    https://xlsxwriter.readthedocs.io/format.html
    https://xlsxwriter.readthedocs.io/worksheet.html
    '''
    def formatExcelFile(self):
        self.bold_format = self.workbook.add_format()
        self.bold_format.set_bold()

        #https://xlsxwriter.readthedocs.io/format.html @ Currency
        self.currency_format = self.workbook.add_format({'num_format': '$#,##0.00'})
        self.currency_format.set_bold()
        # self.currency_format.set_bg_color('green')

        self.final_currency_format = self.workbook.add_format({'num_format': '$#,##0.00'})
        self.final_currency_format.set_bold()
        self.final_currency_format.set_bg_color('yellow')
        self.final_currency_format.set_border()

        self.red_format = self.workbook.add_format()
        self.red_format.set_font_color('red')
        self.red_format.set_num_format('0.00"%"') #Custom 0.00 + % format, MARGE is already in %

        self.percent_format = self.workbook.add_format()
        self.percent_format.set_num_format(9) #0% format

        self.note_format =self.workbook.add_format()
        self.note_format.set_text_wrap()
        self.note_format.set_bold()

    def createFolder(self):
        ### Create desktop folder "Export-CES" if it does not exist
        try:
            folder = str(self.desktoppath)+"\\Export-CES"
            if not os.path.exists(folder):
                os.makedirs(folder)

            # self.folder = folder
        except:
            QMessageBox.warning(self, "Warning", "Could not create folder 'Export-CES' on Desktop.")

    def setNewMaterialCost(self, ligne):
        try :  
            newrawmat = self.TableQuote.item(ligne,11).text()
        except :
            newrawmat = 0
        self.newrawmat = newrawmat

    def openExcelFile(self, conn):
        try:
            file = self.way
            os.startfile(file)
            try:
               closeSQLite(conn)
            except UnboundLocalError:
                print("Connection is already closed")
            except Exception as ex:
                printError(ex)


        except Exception as ex:
            printError(ex)

    def writeExcelHeader(self):
        try:
            self.feuille.set_column('A:K',20)
            self.feuille.set_column('C:C',10)
            self.feuille.set_column('B:B',30)
            self.feuille.set_column('F:F',10)
            self.feuille.set_column('G:G',15)
            self.feuille.set_column('H:J',10)


            self.feuille.write(3,0,'Notes :')
            self.feuille.write(4,0,'Part Number :')
            self.feuille.write(5,0,'Revision :')
            self.feuille.write(6,0,'Description :',self.bold_format)
            self.feuille.write(7,0,'Mfg. Spec. :')
            # self.feuille.write(8,0,'Notes :')
            self.feuille.write(9,0,'Part Built Date: ')
            self.feuille.write(10,0,'Part Estimator: ')
            self.feuille.write(11,0,'Quote Preparer: ')
            self.feuille.write(13,0,'Operations :')
            self.feuille.write(4,3,'Material :', self.bold_format)
            self.feuille.write(5,3,'Matl Cost :', self.bold_format)
            self.feuille.write(6,3,'Diameter :', self.bold_format)
            self.feuille.write(7,3,'Part Weight :', self.bold_format)
            self.feuille.write(9,3,'Req Qty :')
            self.feuille.write(10,3,'Scrap Qty :')
            self.feuille.write(11,3,'Total Qty :')
            self.feuille.write(4,6,'Slug Length :', self.bold_format)
            self.feuille.write(5,6,'Hd. Vol Len :', self.bold_format)
            self.feuille.write(6,6,'Shank Length :', self.bold_format)
            self.feuille.write(4,8,'Nut?:', self.bold_format)
            self.feuille.write(5,8,'Stud?:', self.bold_format)
            self.feuille.write(6,8,'Bolt?:', self.bold_format)

            self.feuille.write(0,0,'Export :')
                
            self.feuille.write(2,0,'Date of the Quote :' + self.timestamp +".")
        except Exception as ex:
            printError(ex)
            print("Error writing row headers to export quote.")

    '''Find the number of operations in total held in the database
    Number of ops is held in the first operations (Op1) spot in the database
    This is how Synoptic held the database
    '''
    #The Op1 position is actually the total number of operations in the EXP-PART.txt export from Synoptic. I.E. if export is 5 306 401 309 99 42 16 17 then 306, 401, 309, 99, 42 are operations. !16, 17 are not operations!
    def getNumberOps(self, cur):
        requestNumOps = "SELECT Op1 FROM Part WHERE PartNumber = ?"
        try:
            cur.execute(requestNumOps, (self.partnumber,))
        except Exception as ex:
            printError(ex)
        SynopticNumOps = cur.fetchone()
        synopticNumOps = SynopticNumOps[0]
        if(synopticNumOps > 100):
            synopticNumOps -= 100

        self.synopticNumOps = synopticNumOps


    def findPartInfo(self, cur):
        cur.execute("SELECT Rev, Description, MfgSpec, Note, Material, Shank, EstBy, Date, isNut, isStud FROM Part WHERE PartNumber = ?",(self.partnumber,))
        part = cur.fetchone()

        try:
            self.estimator = part[6]
            self.partRev = part[0]
            self.partDesc = part[1]
            self.partMfgSpec = part[2]
            self.partNote = part[3]
            self.partMaterial = part[4]
            self.creationDate = part[7]
        except Exception as ex:
            printError(ex)

    def findMaterialInfo(self,cur):
        cur.execute("SELECT Name, Spec FROM Mat WHERE Number = ?",(self.partMaterial,))
        matdescription = cur.fetchone()
        
        
        try:
            # print("matdescription: ", matdescription)
            # print("matdescription[0]", matdescription[0])
            # print("matdescription[1]", matdescription[1])
            
            self.matnamespec = str(matdescription[0])+"--"+str(matdescription[1])
        except TypeError as ex:
            printError(ex)
            
            message = "Error relates to: " + str(self.partMaterial) + " part number: " + str(self.partnumber)
            QMessageBox.warning(self, "warning", message)
        
        except Exception as ex:
            printError(ex)
            QMessageBox.warning(self, "Warning", message)

    def findEstimator(self):


        #3 original estimators are Jim, PS (Phil Stella), and Joy
        #Also keep ***For Info Only*** notes
        ##Ignore !*X, ^*X, etc. type text, L=G+0.6 94 etc. etc.
        try:

            #####Use self.shank from above, do not use part[5] as shank!####



            # print("estimator[0]: ", self.estimator[0])
            if(self.estimator[0].isalpha()):
                separator = " "
                # print("self.estimator: ", self.estimator)
                try:
                    first = self.estimator.split(separator, 1)[0]
                    # print("first: ", first)
                    second =self.estimator.split(separator, 1)[1]
                    # print("second: ", second)
                    # print("first.isalpha(): ", first.isalpha())
                    # print("second.isalpha(): ", second.isalpha())
                    if(first.isalpha() and second.isalpha()):
                        if re.match('^[a-zA-Z]+$', second):
                            self.estimator = first + " " + second
                            # print("estimator2:", self.estimator)
                    elif(first.isalpha()):
                        self.estimator = first
                        # print("else")

                    else:
                        self.estimator = re.split('[^a-zA-Z]', self.estimator)[0]
                        # print("estimator: ", self.estimator)

                except Exception as ex:
                    try:
                        printError(ex)
                        self.estimator = first
                    except Exception as ex:
                        printError(ex)
                        self.estimator = ""
            elif(self.estimator[0] == '*'):
                if(self.estimator[0] == '*' and self.estimator[1] == '*' and self.estimator[2] == '*'):
                    pass #return unedited self.estimator
                elif( self.estimator[0] == '*' and self.estimator[1] == '*'):
                    pass
                        # self.estimator = "FOR INFO ONLY"
                        # print("FOR INFO ONLY")
                elif(self.estimator[0] == '*' and self.estimator[1] == 'C'):
                    # print("CROSS REF. ONLY")
                    self.estimator = "CROSS REF. ONLY"
                    # print("first: ", first)
                    # print("second: ", second)


            else:
                print("estimator unknown: ", self.estimator)
                # estimator = 'Unknown'
        except Exception as ex:
            printError(ex)

    def makeSafePartNumber(self, ligne):
        try :

            self.printpart = re.sub("\\|\?|\[|\]|\:|\*|\?|\/", "", self.partnumber)
            # print("self.feuille a after sub: ", printpart)
            
            self.feuille = self.workbook.add_worksheet(self.printpart)
            self.allPNwithDuplicates.append(self.partnumber)
        except Exception as errorVariable :
            printError(errorVariable)
            self.printpart = re.sub("\\|\?|\[|\]|\:|\*|\?|\/", "", self.partnumber)
            if(len(self.partnumber)>=31):
                self.printpart = self.printpart[:30] + "D" #Get first 30 characters, then add "D"
            else:
                duplicatepn =  str(self.printpart)+"D#"+str(ligne+1)
            if(len(duplicatepn)>31):
                duplicatepn = duplicatepn[:30]+ "D"
                
            
            self.feuille = self.workbook.add_worksheet(duplicatepn)
            self.allPNwithDuplicates.append(duplicatepn) ##This will
    def closeWorkbook(self):
        try :
            self.workbook.close()
            ##This line will not trigger if above line is not executed successfully
            # QMessageBox.about(self, "Confimation", "Your quote has been saved.")
        except IOError as errorVariable3:
            QMessageBox.warning(self, "Warning", "I/O error({0}): {1}".format(errorVariable3.errno, errorVariable3.strerror) +" " + "Is your Excel file still open?" )
            print("I/O error({0}): {1}".format(errorVariable3.errno, errorVariable3.strerror) )
        except Exception as ex :
            printError(ex)
            QMessageBox.warning(self, "Warning", "Cannot save Excel quote.")
            return

    def calculateSETUP(self):
        SETUP = sum(self.Opsetup)/self.qty
        
        self.SETUP = round(SETUP,3)
