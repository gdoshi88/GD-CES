# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSACES_NewPart_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

##10/1/19 - Update filledpw to account for nut/stud if you check the box.
##E.G. If you check nut the shank length gets set to 0

##10/2/19 - Delete VueNewPartFilled - replaced entirely by VueEditPartFilled

##10/3/19 - Attempt to split up into more of a MVC paradigm - sort of.

from PyQt5 import QtCore, QtWidgets\
# from PyQt5 import  QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QMessageBox

from datetime import datetime

# import MSACES
from MSACES_genericFunctions import printError
from MSACES_genericFunctions import trouvercout, calculatePW
from MSACES_genericFunctions import connectSQLite, closeSQLite
from MSACES_NewPart_UI import Ui_NewPart


class VueNewPart(QtWidgets.QDialog,Ui_NewPart):
    def __init__(self, parent):
        super(VueNewPart, self).__init__(parent)

        self.setupUi(self)
        
        self.listop = list()

        self.isStud = False
        self.isNut = False
        self.isNoBid = False

        #default to 0 otherwise bolts will fail
        # self.nut = 0 #integer representation of False for SQLITE
        # self.stud = 0 #integer representation of False for SQLITE
        self.nut = 0
        self.stud = 0
        self.nobid = 0
        self.isOverrideSlug = 0
        self.isOverrideHV = 0


        e = datetime.now()
        e.strftime('%m/%d/%Y')
        self.LE_EstDate.setText(e.strftime('%m/%d/%Y'))
        self.PB_ValidateOperation.clicked.connect(self.PBValidateOperation)
        self.PB_SaveOperation.clicked.connect(self.PBSaveProgress)
        self.PB_AddOp.clicked.connect(self.PBAddOp)     
        self.PB_RemoveOp.clicked.connect(self.PBRemoveOp)
                
        self.LE_NumeroOp.setText("1")
#        self.LE_Mat.setText("beefy testy")

        self.setCompleters()

        self.setPressedAction()

        self.TableOp.clicked.connect(self.on_click)



    '''Define action when someone clicks in the grid of the "operation" window of New Part'''
    def on_click(self):

        try:
            row = self.TableOp.currentRow()
            row = row + 1
            print("row5: ", row)
            row = str(row)
            self.LE_NumeroOp.setText(row)
        except Exception as ex:
            printError(ex)



    '''Set the completers - the objects that give suggestions in a dropdown box'''
    def setCompleters(self):

        conn = connectSQLite()
        cur = conn.cursor() 
        
        ####
        try:
            cur.execute("SELECT Number FROM Op ORDER BY Number ASC")
            part = cur.fetchall()
            
            listnum = []
            for prt in part:
                for p in prt:
                    listnum.append(str(p))  
                           
            cmpt = QCompleter(listnum)  
            cmpt.setCaseSensitivity(0)
            cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            self.LE_CodeOp.setCompleter(cmpt)
        except Exception as ex:
            printError(ex)
  
        try:
            cur.execute("SELECT NAME FROM OP ORDER BY NAME ASC")
            desc = cur.fetchall()
            
            listdesc = []
            for dsc in desc:
                for d in dsc:
                    listdesc.append(str(d))  
                           
            cmpt = QCompleter(listdesc) 
            cmpt.setCaseSensitivity(0)
            cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            self.LE_DescriptionOp.setCompleter(cmpt)
        except Exception as ex:
            printError(ex)
        ####
        try:
            cur.execute("SELECT DISTINCT Name FROM Mat ORDER BY Name ASC")
            descmat = cur.fetchall()
            
            listdescmat = []
            i = 0
            while i <= len(descmat)-1:
                
                a = str(descmat[i][0])          
                listdescmat.append(a)  
                
                i=i+1  
            
            cmpt = QCompleter(listdescmat)
            cmpt.setCaseSensitivity(0)
            cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)

            self.LE_DescMat.setCompleter(cmpt)
        except Exception as ex:
            printError(ex)

        closeSQLite(conn)
        
        
    '''
    Set link an action/event to the function it calls.
    For example if operation is done editing -> call remplirdescription
    '''
    def setPressedAction(self):
        # print("set pressed action running")
        # print("testing Checkbox initial state: ", self.isNutBox.isChecked()) #defaults to False, not null good
        self.LE_CodeOp.editingFinished.connect(self.remplirdescription)
        self.LE_DescriptionOp.editingFinished.connect(self.remplircode)
        self.LE_DescMat.editingFinished.connect(self.dropdiam)
        self.LE_Mat.returnPressed.connect(self.populerdescdiam)
        self.LE_Shank.editingFinished.connect(self.filledpw)
        self.LE_PartNumber.setFocus()
        # self.isNutBox(self.testIsNut)
        self.isNutBox.stateChanged.connect(self.testIsNut)
        self.isStudBox.stateChanged.connect(self.testIsStud)
        self.isNoBidBox.stateChanged.connect(self.testIsNoBid)

        self.overrideHeadVolume.stateChanged.connect(self.overrideHeadVolumeChanged)
        self.overrideSlugLength.stateChanged.connect(self.overrideSlugLengthChanged)

        ###Nothing needed for NUT - it's just a Boolean ###




    ##08/20/19 - Update code so operation1 is not inserted into Op1 slot
    ##Op1 Slot needs to be the total number of operations + 100
    ##E.G Op1 = 105, then Op2 through Op6 (5 total) are actual operations

    ##This is the one and only for both classes!!!!!!####    
    def updateOps(self, cur, conn, partnumber):
            # print("I'm in update ops function right now")
            n = 0
            totalNumOps = 0
            TOTAL_OPS = 40
            FIRST_OP = 2
            while n <= (TOTAL_OPS - FIRST_OP) :
                    
                try :
                    op = self.listop[n]
                    totalNumOps = totalNumOps + 1
                except:
                    op = '0'
                
        #                num = int(n+1)
                num = int(n+FIRST_OP) #start at Op2
                cur.execute("UPDATE Part SET Op%s = ? WHERE PartNumber = ?" %num ,(op,partnumber))
                conn.commit()
                
                n = n + 1             
            
            ##Assign Op1 which is total number of operations
            if(totalNumOps != 0):
                # print("totalNumOps: ", totalNumOps)
                totalNumOps = totalNumOps + 100 #For whatever reason Synoptic logic has all operations > 100
                cur.execute("UPDATE Part SET Op1 = ? WHERE PartNumber = ?" ,(totalNumOps,partnumber))
                conn.commit()
            else:
                print("Error in New Part with totalNumOps")
                
            QMessageBox.about(self, "Confirmation", "The new part has been added successfully.")          

    '''For the purposes of unit testing have this function without any error handling
    unit test will call this directly.
    Do not use this directly in live. Use the filledpw which is safe
    '''
    def unsafe_filledpw(self, cur):
        mat = self.LE_Mat.text()
        diam = self.LE_Diam.text()
        if(self.nut == 1):
            self.LE_Shank.setText("0.000")
        else:
            shank = self.LE_Shank.text()
        cur.execute("SELECT Type FROM Mat WHERE Number = ?",(mat,))
        Groupe = cur.fetchone() 
        mattype = str(Groupe[0])
        
        d = float(diam)
        if(self.nut == 1):
            s = 0.000
        else:
            s = float(shank)

        if(self.nut == 1):
            hdv = round(d*2.0, 3)
        elif(self.stud == 1):
            hdv = 0.000
        else:
            hdv = round(d * 2.2,3)
        if(self.nobid == 1):
            print("self.nobid == 1")
        HDV = str('%.3f'%hdv)
        slug = round(hdv + s ,3)
        # SLUG = str(slug)
        SLUG = str('%.3f'% slug) ##For 3 decimal places even if round is two. I.e. 4.030 instead of 4.03


        PW = calculatePW(mattype, slug, d)
        PW = str(PW)

        self.LE_Diam_2.setText(PW)

    # self.isStudBox.isChecked()
        if(self.overrideHeadVolume.isChecked()):
            print("override Head Vol checked")
        else:
            self.LE_Diam_3.setText(HDV)

        if(self.overrideSlugLength.isChecked()):
            print("override slug length checked")
        else:
            self.LE_Diam_4.setText(SLUG)


    '''
    Find hdvol, part weight, etc after entering the shank length
    This is used in production code
    '''
    def filledpw(self):
        # print("VueNewPart filledpw go")

        conn = connectSQLite()
        cur = conn.cursor()


        try :
            self.unsafe_filledpw(cur)
        except Exception as ex :
            printError(ex)
            # print("VueNewPart filledpw except")
            checkList = [self.LE_Mat, self.LE_Diam, self.LE_Shank]
            
            for frog in checkList:
                #Only complete this once so the focus is set to the most recent text box
                if(frog.text() is None or frog.text() == ""):
                    frog.setFocus()
                    break

        closeSQLite(conn)

        
    def remplirdescription(self):
        conn = connectSQLite()
        cur = conn.cursor()  
        
        try : 
            code = self.LE_CodeOp.text()
            code = str(code)
            cur.execute("SELECT Name FROM Op WHERE Number = ?",(code,))
            Desc = cur.fetchone()
            desc = str(Desc[0])
            
            self.LE_DescriptionOp.setText(desc)
        except : 
            QMessageBox.about(self, "Warning", "Error. The description corrsponding to this operation code cannot be found. ")
        
        closeSQLite(conn)

    def remplircode(self):

        conn = connectSQLite()
        cur = conn.cursor()  
        try:
            desc = self.LE_DescriptionOp.text()
            desc = str(desc)
            cur.execute("SELECT Number FROM Op WHERE NAME = ?",(desc,))
            Code = cur.fetchone()
            code = str(Code[0])
            
            self.LE_CodeOp.setText(code)
        except : 
            QMessageBox.about(self, "Warning", "Error. The code corrsponding to this description cannot be found. ")
        closeSQLite(conn)


    '''
    Fill material designation/name
    and diameter
    once the material code is entered
    '''
    def populerdescdiam(self):
        conn = connectSQLite()
        cur = conn.cursor()  
        try : 
            
            self.LE_DescMat.clear()
            ### If it's not none or not blank then clear it
            if (self.LE_Diam.text() != "" and self.LE_Diam.text() is not None):
                self.LE_Diam.clear()
            ###Above is different from VueNewPart###
            code = self.LE_Mat.text()
            
    
            cur.execute("SELECT Name, Diam FROM Mat WHERE Number = ?",(code,))
            Code = cur.fetchone()
            desc = str(Code[0])
            diam = str(Code[1])
            
            self.LE_DescMat.setText(desc)   
            self.LE_Diam.setText(diam) 
            
        except : 
            
            QMessageBox.about(self, "Warning", "Error. Could not find matching Designation and diameter for this material code. Please try another one.")
            
        closeSQLite(conn)


    def remplircodemat(self): # remplie code mat apres que la designation + diam soit rentrer 
        conn = connectSQLite()
        cur = conn.cursor()  

        description = self.LE_DescMat.text()
        diam = self.LE_Diam.text()
        # print("description: ", description)
        # print("diam: ", diam)

        cur.execute("SELECT Number FROM Mat WHERE Name = ? AND Diam = ?",(description,diam))
        Code = cur.fetchone()
        code = str(Code[0])
        
        self.LE_Mat.setText(code)

        ####I removed this popup. The systemhook will catch the error and print to console##########
        # QMessageBox.about(self, "Warning", "Error. To select a material code from its description and diameter you have to select one option of the dropdown list provided.")
        
        #Point user to field in question if it is blank
        if(self.LE_DescMat.text() is None or self.LE_DescMat.text() == "" ):
            self.LE_DescMat.setFocus()
        if(self.LE_Mat.text() is None or self.LE_Mat.text() == "" ):
            self.LE_Mat.setFocus()
            
        closeSQLite(conn)



    
    def dropdiam(self):
        conn = connectSQLite()
        cur = conn.cursor()  
        try : 
            ###################this is different from filled ############
            if (self.LE_Diam is not None or self.LE_Diam != ""):
                self.LE_Diam.clear()
                #############
            description = self.LE_DescMat.text()
            
            cur.execute("SELECT Diam FROM Mat WHERE Name = ? ORDER BY Diam ASC",(description,))
            desc = cur.fetchall()
            
            listdesc = []
            for dsc in desc:
                for d in dsc:
                    listdesc.append(str(d))  
                           
            cmpt = QCompleter(listdesc) 
            cmpt.setCaseSensitivity(0)
            cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            self.LE_Diam.setCompleter(cmpt)
            
            self.LE_Diam.editingFinished.connect(self.remplircodemat)  
        
        except : 
            
            QMessageBox.about(self, "Warning", "Error. Not matching material designation. Please select a designation proposed in the dropdown list. ")
            
        closeSQLite(conn)
    
    def RepresentsInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False 
        

    
    ##The one and only, inherited by newpartfilled class
#    @classmethod

    def PBAddOp(self):
        try:
            conn =connectSQLite()        
            cur = conn.cursor()         
            mat = self.LE_Mat.text()
            diam = self.LE_Diam.text()
            rowposition = self.LE_NumeroOp.text()
            code = self.LE_CodeOp.text()
            description = self.LE_DescriptionOp.text()  
        except Exception as ex:
            printError(ex)
        
            
        rowlabel = self.label_14.text()
        codelabel = self.label_15.text()
        desclabel = self.label_16.text()


        if mat == "":
            QMessageBox.warning(self, "Warning", "Please choose a valid material.")
            return 
        if rowposition is None or rowposition == "" :
            QMessageBox.warning(self, "Warning",  rowlabel + " Must not be empty.")
            return
        if code is None or code == "":
            QMessageBox.warning(self, "Warning", codelabel +" Must not be empty.")
            return
        if description is None or description == "":
            QMessageBox.warning(self, "Warning", desclabel +" Must not be empty.")
            return  
        
        ##Assert string conversion turns into int
        if (VueNewPart.RepresentsInt(rowposition)):
            index = int(rowposition)-1
        else:
            QMessageBox.warning(self, "Warning", rowposition +" Does not appear to be a number.")
        try:
            index = int(rowposition)-1
            self.listop.insert(index,code)

            self.TableOp.clearContents()
            
            ii = 0
            while ii <= len(self.listop)-1 : 
                
                code = str(self.listop[ii])  
                
                cur.execute("SELECT Name FROM Op WHERE Number = ?",(code,))
                Description = cur.fetchone() 
                description = str(Description[0])
                
                a2 = code    
                a2 = QtWidgets.QTableWidgetItem(a2)
                self.TableOp.setItem(ii,0,a2)                 
                a3 = description
                a3 = QtWidgets.QTableWidgetItem(a3)
                self.TableOp.setItem(ii,1,a3)
          
                cur.execute("SELECT Groupe FROM Mat WHERE Number = ?",(mat,))
                Groupe = cur.fetchone() 
                group = str(Groupe[0])
                
                Diam =  float(diam) 
                setupcost,cost = trouvercout(group,Diam)
                print("setupcost: ", setupcost)
                print("cost: ", cost)
                
                pnum = str(code)           
                cur.execute("SELECT %s,%s FROM Op WHERE Number = ?" %(setupcost,cost),(pnum,))
                Cout = cur.fetchone()
                    
                a4 = str(Cout[0])
                a4 = QtWidgets.QTableWidgetItem(a4)
                self.TableOp.setItem(ii,2,a4)  
                a5 = str(Cout[1])
                a5 = QtWidgets.QTableWidgetItem(a5)
                self.TableOp.setItem(ii,3,a5)
                
                ii = ii + 1
                
            ##Auto increment the row#/position counter after adding an operation
            rowposition = int(rowposition) + 1
            rowposition = str(rowposition)
            self.LE_NumeroOp.setText(rowposition)    
        except Exception as ex:
            printError(ex)
    
        closeSQLite(conn)
    
 
        
      
    #The one and only 
    def PBRemoveOp(self):
        conn =connectSQLite()        
        cur = conn.cursor() 
        try:
            rowposition = self.LE_NumeroOp.text()      
            deleterow = int(rowposition)-1
        except Exception as ex:
            printError(ex)
            
        try :
            del self.listop[deleterow]
        except IndexError as ex : 
            QMessageBox.about(self, "Warning", "Error. The row you want to delete doesn't exist. ")
            printError(ex)
            return
         
        self.TableOp.clearContents()
        try:   
            mat = self.LE_Mat.text()
            diam = self.LE_Diam.text()
            
            ii = 0
            while ii <= len(self.listop)-1 : 
                
                code = str(self.listop[ii])  
                
                cur.execute("SELECT Name FROM Op WHERE Number = ?",(code,))
                Description = cur.fetchone() 
                description = str(Description[0])
                
                a2 = code    
                a2 = QtWidgets.QTableWidgetItem(a2)
                self.TableOp.setItem(ii,0,a2)                 
                a3 = description
                a3 = QtWidgets.QTableWidgetItem(a3)
                self.TableOp.setItem(ii,1,a3)
          
                cur.execute("SELECT Groupe FROM Mat WHERE Number = ?",(mat,))
                Groupe = cur.fetchone() 
                group = str(Groupe[0])
                
                Diam =  float(diam) 
                setupcost,cost = trouvercout(group,Diam)
                
                pnum = str(code)           
                cur.execute("SELECT %s,%s FROM Op WHERE Number = ?" %(setupcost,cost),(pnum,))
                Cout = cur.fetchone()
                    
                a4 = str(Cout[0])
                a4 = QtWidgets.QTableWidgetItem(a4)
                self.TableOp.setItem(ii,2,a4)  
                a5 = str(Cout[1])
                a5 = QtWidgets.QTableWidgetItem(a5)
                self.TableOp.setItem(ii,3,a5)
                
                ii = ii + 1
        except Exception as ex:
            printError(ex)

        closeSQLite(conn)

    '''
    Final validation for part
    All fields are required
    '''
    def PBValidateOperation(self):
        try:
            conn =connectSQLite()        
            cur = conn.cursor()                 
            partnumber = self.LE_PartNumber.text()
            description = self.LE_Description.text()
            revision = self.LE_Revision.text()
            mfgspec = self.LE_MfgSpec.text()
            mat = self.LE_Mat.text()
            headop = self.CB_HeadOp.currentText()
            diam = self.LE_Diam.text()
            shank = self.LE_Shank.text()
            # note = self.LE_Note.text()
            #QTextEdit uses different method than QLineEdit
            note = self.LE_Note.toPlainText()
            estby = self.CB_EstBy.currentText()
            dateest = self.LE_EstDate.text()
            stud = self.stud
            nut = self.nut
            nobid = self.nobid
            slugBool = self.isOverrideSlug #1 or 0 because sqlite doesn't have booleans
            HVBool = self.isOverrideHV #1 or 0 because sqlite doesn't have booleans
            #QTextEdit uses different method than QLineEdit
            nobidnote = self.txtNoBid.toPlainText()

            nut = int(nut)
            stud = int(stud)
            nobid = int(nobid)

            print("")
        except Exception as ex:
            printError(ex)
        
        ##New- was missing in 1.7.3
        try:
            partWeight = self.LE_Diam_2.text()
            headVol = self.LE_Diam_3.text()
        except Exception as ex:
            printError(ex)

        ################
        self.updateInsertPart(cur,conn, partnumber, description, revision, mfgspec, estby, dateest, mat, partWeight, diam, shank, headVol, headop, note, nut, stud, nobid, nobidnote, slugBool, HVBool)

        closeSQLite(conn)

    '''
    Saving progress is like a File- > Save
    Not everything is required to save progress
    If something is blank save it as None
    '''
    def PBSaveProgress(self):
        # print("validate entering")
        conn =connectSQLite()
        cur = conn.cursor()    
        try:
            try:
                partnumber = self.LE_PartNumber.text()
            except:
                QMessageBox.about(self, "Warning", "A valid part number is required to save. ")
                return
                
            try:
                description = self.LE_Description.text()
            except:
                description = None
            try:
                revision = self.LE_Revision.text()
            except:
                revision = None
            try:
                mfgspec = self.LE_MfgSpec.text()
            except:
                mfgspec = None
            try:
                mat = self.LE_Mat.text()
            except:
                mat = None
            try:
                headop = self.CB_HeadOp.currentText()
            except:
                headop = None
            try:
                diam = self.LE_Diam.text()
            except:
                diam = None
            try:
                shank = self.LE_Shank.text()
            except:
                shank = None
            try:
                # note = self.LE_Note.text()
                note = self.LE_Note.toPlainText()
            except:
                note = None
            try:
                estby = self.CB_EstBy.currentText()
            except:
                estby = None
            try:
                dateest = self.LE_EstDate.text()    
            except:
                dateest = None

            try:
                nut = self.nut
            except:
                nut = 0

            try:
                stud = self.stud
            except:
                stud = 0

            try:
                nobid = self.nobid
            except:
                nobid = 0

            try:
                nobidnote = self.txtNoBid.text()
            except:
                nobidnote = None

            try:
                slugBool = self.isOverrideSlug
            except:
                slugBool = 0

            try:
                HVBool = self.isOverrideHV
            except:
                HVBool = 0



        except Exception as ex:
            printError(ex)
        
        ##New- was missing in 1.7.3
        try:
            partWeight = self.LE_Diam_2.text()
            print("partWeight: ", partWeight)
        except:
            partWeight = None
        try:
            headVol = self.LE_Diam_3.text()
            print("headVol: ", headVol)
        except:
            headVol = None


        self.updateInsertPart(cur,conn, partnumber, description, revision, mfgspec, estby, dateest, mat, partWeight, diam, shank, headVol, headop, note, nut, stud, nobid,nobidnote, slugBool, HVBool)

        closeSQLite(conn)

    '''
    Rather than assigning all the variables into self instance
    Passed all the variables explicitly in case there was some overwrite
    Best practice in future would be to hold all variables like partnumber in self instance instead
    '''
    def updateInsertPart(self,cur,conn, partnumber, description, revision, mfgspec, estby, dateest, mat, partWeight, diam, shank, headVol, headop, note, nut, stud, nobid, nobidnote, slugBool, HVBool):
        cur.execute("SELECT PartNumber FROM Part")
        comp = cur.fetchall()
        
        partnumber = str(partnumber)
        a = 0
        try:
            for cmp in comp:
                for c in cmp:
                    c = str(c)
                    if partnumber == c :
                        a = 1
                        break  
                    
            if a == 1 :
                buttonReply = QMessageBox.question(self, 'Warning', "The part number you enter already exist. To update the existing part click Yes, to go back click No.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                
                if buttonReply == QMessageBox.Yes:
                    cur.execute("UPDATE Part SET Description = ?, Rev = ?, MfgSpec = ?, EstBy = ?, Date = ?, Material = ?, Diam = ?, Shank = ?, Heading = ?, Note = ?,isNut =?, isStud=?, isNoBid = ?, NoBidNote = ?, slugBool = ?, HVBool = ? WHERE PartNumber = ?",(description,revision,mfgspec,estby,dateest,mat,diam,shank,headop,note,nut, stud, nobid, nobidnote, slugBool, HVBool, partnumber,))
                    conn.commit()
                    
                    VueNewPart.updateOps(self, cur, conn, partnumber)
    
                else:
                    return
       
            elif a == 0 :
        #######################need to add weight and hdvol ####################
                req = "INSERT INTO Part(PartNumber, Description, Rev, MfgSpec, EstBy, Date, Material,Weight, Diam, Shank,HdVol, Heading, Note,isNut,isStud,isNoBid,NoBidNote,slugBool, HVBool) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(req, (partnumber,description,revision,mfgspec,estby,dateest,mat,partWeight,diam,shank,headVol,headop,note,nut, stud, nobid, nobidnote,slugBool, HVBool))
                conn.commit()

                VueNewPart.updateOps(self, cur, conn, partnumber)
        except Exception as ex:
            printError(ex)



    def setStudNutState(self):
        self.isNut = self.isNutBox.isChecked()
        self.isStud = self.isStudBox.isChecked()

        self.nut = 1 if self.isNut else 0 #Convert python boolean into SQlite integer
        self.stud = 1 if self.isStud else 0 #Convert python boolean into SQlite integer

        return

    def setOverrideState(self):

        if(self.overrideSlugLength.isChecked()):
            self.isOverrideSlug = 1

        if(self.overrideHeadVolume.isChecked()):
            self.isOverrideHV = 1

    def setNoBidState(self):
        self.isNoBid = self.isNoBidBox.isChecked()
        # print("isNoBid: ", self.isNoBid)

        self.nobid = 1 if self.isNoBid else 0
        # print("self.nobid: ", self.nobid)

    def testIsNoBid(self):
        self.setNoBidState()

    def testIsNut(self):
        #uncheck stud box
        self.isStudBox.blockSignals(True)
        self.isStudBox.setChecked(False)
        self.isStudBox.blockSignals(False)

        self.setStudNutState()
        self.filledpw() ##Recalculate head vol, shank length, etc.



        '''
        
        ALTER TABLE PART ADD isNut INTEGER NOT NULL default 0;
        '''


    def testIsStud(self):
        #uncheck Nutbox
        self.isNutBox.blockSignals(True)
        self.isNutBox.setChecked(False)
        self.isNutBox.blockSignals(False)


        self.setStudNutState()
        self.filledpw() ##Recalculate head vol, shank length, etc.


        '''
        ALTER TABLE PART ADD isStud INTEGER NOT NULL default 0;

        '''
    def overrideSlugLengthChanged(self):
        self.filledpw()
        self.setOverrideState()
        print("slug length changed, filledpw run")

    def overrideHeadVolumeChanged(self):
        self.filledpw()
        self.setOverrideState()
        print("head volume changed, filledpw run")
        
class VueEditPartFilled(QtWidgets.QDialog,Ui_NewPart):

    def __init__(self, parent,partnumber,description,revision,mfgspec,estby,date,mat,headop,diam,shank,note,ops,isNut,isStud,isNoBid,NoBidNote,slugBool, HVBool):
        # print("VueEditPartFilled ")
        super(VueEditPartFilled, self).__init__(parent)
        conn =connectSQLite()        
        cur = conn.cursor()
        self.setupUi(self)

        ##Implement some OOP best practices:
        self.partnumber = partnumber
        self.description = description
        self.revision = revision
        self.mfgspec = mfgspec
        self.estby = estby
        self.date = date
        self.mat = mat
        self.headop = headop
        self.diam = diam
        self.shank = shank
        self.note = note
        self.ops = ops
        # print("ops: ", ops)
        # print("typeops3:", type(ops))
        self.isNut =isNut
        self.isStud = isStud
        self.isNoBid = isNoBid
        ####
        self.nut = 0 #self.nut is like self.isOverrideSlug holds 1/0 for true/false
        self.stud = 0
        self.nobid = 0
        self.numOps = 0 #default
        print("VueEditPartFilled slugBool: ", slugBool)
        print("VueEditPartFilled HVBool: ", HVBool)
        self.isOverrideSlug = slugBool
        self.isOverrideHV = HVBool


        self.setCompleters()
        self.setPressedAction()

        self.listop = list()
        e = datetime.now()
        e.strftime('%m/%d/%Y')
        self.LE_EstDate.setText(e.strftime('%m/%d/%Y'))
        self.nbligne = 0

        ##Init UI Fields
        self.LE_PartNumber.setText(partnumber)
        self.LE_Description.setText(description)
        self.LE_Revision.setText(revision)
        self.LE_MfgSpec.setText(mfgspec)
        self.CB_EstBy.setCurrentIndex(estby)
        # print("mat: ", mat)
        self.LE_Mat.setText(mat)
        self.CB_HeadOp.setCurrentIndex(headop)
        # print("headop: ", headop)

        self.LE_Diam.setText(diam)
        self.LE_Shank.setText(shank)
        self.LE_Note.setText(note)
        
        self.LE_NumeroOp.setText("1")   ##Initialize Operation add to row 1
        
        self.PB_ValidateOperation.clicked.connect(self.PBValidateOperation)
        self.PB_SaveOperation.clicked.connect(self.PBSaveProgress)

        self.PB_AddOp.clicked.connect(self.PBAddOp)
        self.PB_RemoveOp.clicked.connect(self.PBRemoveOp)
        self.TableOp.clicked.connect(self.on_click)

        self.isNut = isNut
        self.isStud = isStud
        self.isNoBid = isNoBid

        self.NoBidNote = NoBidNote

        self.initStudNut()
        self.initNoBidBox()
        self.initOverrideBox()

        self.setNoBidText(self.NoBidNote)
        # self.txtNoBid.setText(self.NoBidNote)



        try:
            cur.execute("SELECT Groupe FROM Mat WHERE Number = ?",(mat,))
            Groupe = cur.fetchone() 
            group = str(Groupe[0])
        except:
            group = None
        try:
            Diam =  float(diam)
        except:
            Diam = None
        try:  
            if(group and Diam):
                setupcost,cost = trouvercout(group,Diam)
        except Exception as ex:
            print("ex: ", ex)
            print("group and/or diam required")
            setupcost = None
            cost = None
        try:
            # self.numOps = VueNewPartFilled.getNumberOfOps(self)
            self.numOps = self.getNumberOfOps()

            # numOps = VueNewPartFilled.getNumberOfOps(self, ops)
        except Exception as ex:
            print("getNumberOfOps ex: ", ex)
            print("cannot calculate number of operations")
        try:
            setupcost,cost = trouvercout(group,Diam)
        except:
            print("cannot calculate setupcost, cost")
        
        ###This is supposed to load Operation tab table with stuff
        if(self.ops and setupcost and cost and self.numOps):
            # self.loadOperations(ops,setupcost, cost, numOps)
            # self.loadOperations()
            self.loadOperations(setupcost, cost)
        else:
            print("cannot load operations")
        ###Load autocalculated stuff like part weight, head vol, slug length
        if(mat and diam and shank):
            self.filledpw()
        else:
            print("cannot fill in part weight")





        closeSQLite(conn)

    def setNoBidText(self, text):
        self.txtNoBid.setText(text)

    def setStudNutState(self):
        VueNewPart.setStudNutState(self)

    def setNoBidState(self):
        VueNewPart.setNoBidState(self)

    def setOverrideState(self):
        VueNewPart.setOverrideState(self)

    # def initStudNut(self):
    #     VueNewPartFilled.initStudNut(self)
    def initStudNut(self):
        # print("self.isNut: ", self.isNut)
        # print("self.isStud: ", self.isStud)

        if(self.isNut):
            self.isNutBox.setChecked(self.isNut)
            # print("This is a nut")
        if(self.isStud):
            self.isStudBox.setChecked(self.isStud)
            # print("This is a stud")

    def initNoBidBox(self):
        if(self.isNoBid):
            self.isNoBidBox.setChecked(self.isNoBid)

    '''Initialize the override checkboxes for head volume and slug length '''
    def initOverrideBox(self):
        print("init override boxes")
        print("self.isOverrideHV: ", self.isOverrideHV)
        print("self.isOverrideSlug: ", self.isOverrideSlug)
        self.overrideHeadVolume.setChecked(self.isOverrideHV == 1)
        self.overrideSlugLength.setChecked(self.isOverrideSlug == 1)

    def testIsNut(self):
        VueNewPart.testIsNut(self)

    def testIsStud(self):
        VueNewPart.testIsStud(self)

    def testIsNoBid(self):
        VueNewPart.testIsNoBid(self)

    def overrideSlugLengthChanged(self):
        VueNewPart.overrideSlugLengthChanged(self)

    def overrideHeadVolumeChanged(self):
        VueNewPart.overrideHeadVolumeChanged(self)


    def on_click(self):
        VueNewPart.on_click(self)

    def loadOperations(self,setupcost, cost):
        if(not self.ops):
            print("operations is empty")
            return
        
        conn =connectSQLite()        
        cur = conn.cursor()
        i = 0

        # print("self.numOps: ", self.numOps)
        while i < self.numOps and self.numOps != 0: #-2 because Op1 isn't an op
            # print("Loading operation tab", i)
            # print("%s : self.ops[i]: %s "%(i, self.ops[i]))

            if self.ops[i] == '0' or self.ops[i] == ''  or self.ops[i] == None or self.ops[i] =='100' :
                # print("i: ", i)
                # print("breaking: ", self.ops[i], i)
                break
            
            self.listop.append(self.ops[i])
#            p = int(i)
            
            a2 = str(self.ops[i]) 
            # print("a2: ", a2)
            if(int(a2) > 1100):
                break
            a2 = QtWidgets.QTableWidgetItem(a2)
            self.TableOp.setItem(i,0,a2)
        
            pnum = str(self.ops[i])
            
#            if (int(pnum) > 1100): #max in Synoptic is 1099 PN00080067-001 CNR Drill
#                break
#            print("pnum: ", pnum)
            
            cur.execute("SELECT Name FROM Op WHERE Number = ?",(pnum,))
            Name = cur.fetchone() 
            # print("Name: ", Name)
            
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

        closeSQLite(conn)

    def getNumberOfOps(self):
        #in Synoptic op1 is numOps + 100. E.G. 117 = 17 operations saved
        # print("VueNewPart.getNumberOfOps.self.ops: ", self.ops)
        if(self.ops):
        
            numOps = int(self.ops[0])
            if(numOps >100):
                numOps = numOps - 100
            # print("getNumberOfOps.numOps: ", numOps)
            
            self.ops.pop(0) #remove the total operation counter from ops
            # print("getNumberOfOps.ops post pop: ", self.ops)
        else:
            numOps = 0
        # self.numOps = numOps
        return numOps


    def setCompleters(self):
        VueNewPart.setCompleters(self)
    def setPressedAction(self):
        VueNewPart.setPressedAction(self)
        
    # def eventFilter(self, object, event):
    #     VueNewPartFilled.eventFilter(self, object, event)
    def eventFilter(self, object, event):
        
        if event.type()==QtCore.QEvent.FocusOut:
            print("helllo")
            QMessageBox.about(self, "Warning", "EVENT FILLLLLLLLLLLTER. ")


        
    def updateOps(self, cur, conn, partnumber):
        VueNewPart.updateOps(self)

    def unsafe_filledpw(self, cur):
        VueNewPart.unsafe_filledpw(self,cur)

        
    def filledpw(self):  # rempli hdvol weight etc apres avoir entrer le shank
        VueNewPart.filledpw(self)

        
    def remplirdescription(self):
        VueNewPart.remplirdescription(self)
 
        
    def remplircode(self):
        VueNewPart.remplircode(self)

        
        #?? translate: fill in material designation and diamter of material when code is entered
    # def populerdescdiam(self):  # rempli designation et diametre du materiel lorsque code est entree
    #     VueNewPartFilled.populerdescdiam(self)

    def populerdescdiam(self):  # rempli designation et diametre du materiel lorsque code est entree
        conn =connectSQLite()        
        cur = conn.cursor() 
        try : 
            
            self.LE_DescMat.clear()
            self.LE_Diam.clear()
            code = self.LE_Mat.text()
            
    
            cur.execute("SELECT Name, Diam FROM Mat WHERE Number = ?",(code,))
            Code = cur.fetchone()
            desc = str(Code[0])
            diam = str(Code[1])
            
            self.LE_DescMat.setText(desc)   
            self.LE_Diam.setText(diam) 
            
        except : 
            
            QMessageBox.about(self, "Warning", "Error. Could not find matching Designation and diameter for this material code. Please try another one.")
        closeSQLite(conn)

            
        
    def remplircodemat(self): # remplie code mat apres que la designation + diam soit rentrer 
        VueNewPart.remplircodemat(self)



    def dropdiam(self):
        conn =connectSQLite()        
        cur = conn.cursor() 
        try : 

            self.LE_Diam.clear()
            description = self.LE_DescMat.text()
            
            cur.execute("SELECT Diam FROM Mat WHERE Name = ? ORDER BY Diam ASC",(description,))
            desc = cur.fetchall()
            
            listdesc = []
            for dsc in desc:
                for d in dsc:
                    listdesc.append(str(d))  
                           
            cmpt = QCompleter(listdesc) 
            cmpt.setCaseSensitivity(0)
            cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
            self.LE_Diam.setCompleter(cmpt)

            self.LE_Diam.editingFinished.connect(self.remplircodemat)  
        
        except : 
            
            QMessageBox.about(self, "Warning", "Error. Not matching material designation. Please select a designation proposed in the dropdown list. ")
        closeSQLite(conn)


        
    #inherit from VueNewPart class
    def PBAddOp(self):
        print("vuenewpartfilled lemat: ", self.LE_Mat.text())
        VueNewPart.PBAddOp(self)

    def PBRemoveOp(self):
        VueNewPart.PBRemoveOp(self)

    
    def PBValidateOperation(self):
        VueNewPart.PBValidateOperation(self)
    def PBSaveProgress(self):
        VueNewPart.PBSaveProgress(self)

    def updateInsertPart(self,cur,conn, partnumber, description, revision, mfgspec, estby, dateest, mat, partWeight, diam, shank, headVol, headop, note, nut, stud, nobid, nobidnote, slugBool, HVBool):
        VueNewPart.updateInsertPart(self,cur,conn, partnumber, description, revision, mfgspec, estby, dateest, mat, partWeight, diam, shank, headVol, headop, note, nut, stud, nobid, nobidnote, slugBool, HVBool)