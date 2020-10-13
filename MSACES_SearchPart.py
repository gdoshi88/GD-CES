# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSACES_SearchPart.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

##09/19/19 - Added ability to delete part

##10/2/19 - Remove GoToPart, remove links to VueNewPartFilled and replace with VueEditPartFilled
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
import MSACES_NewPart
from MSACES_SearchPart_UI import Ui_SearchPartNumber
# import MSACES
from MSACES_genericFunctions import connectSQLite
from MSACES_genericFunctions import closeSQLite, printError
from PyQt5.QtWidgets import QMessageBox
import traceback


class VueSearchPart(QtWidgets.QDialog,Ui_SearchPartNumber):
 
    def __init__(self, parent):
        super(VueSearchPart, self).__init__(parent)
        self.setupUi(self)

        self.linkUI()
        self.setSearchPartNumberCompleter()



    def linkUI(self):
        #Link the button objects to a function
        # self.PB_GoToPart.clicked.connect(self.PBGoToPart)
        self.PB_GoToPart.clicked.connect(self.PBGoToEditPart) #10/2/19 make them go to same place

        # self.PB_GoToEditPart.clicked.connect(self.PBGoToEditPart)
        self.PB_DeletePart.clicked.connect(self.PBDeletePart)

    def setSearchPartNumberCompleter(self):
        conn =connectSQLite()
        cur = conn.cursor()
        
        cur.execute("SELECT PartNumber FROM Part ORDER BY PartNumber ASC")
        part = cur.fetchall()
#        print("part lookup from search: ", part)
        
        listpart = []
        for prt in part:
            for p in prt:
                listpart.append(str(p))                         
        cmpt = QCompleter(listpart)
        cmpt.setCaseSensitivity(0)
        self.LE_SearchPartNumber.setCompleter(cmpt)
        closeSQLite(conn)

    def PBDeletePart(self):
        print("Delete pressed!")
        try:
            PartNumber = self.LE_SearchPartNumber.text()
            PartNumber = str(PartNumber)
            if (not PartNumber or PartNumber == ""):
                QMessageBox.warning(self, "Warning", "Please select a part that belong to the existing list of the completer.")
                return
            print("PartNumber: ", PartNumber)
        except Exception as ex:
            print(ex)

        try:
            conn =connectSQLite()        
            cur = conn.cursor()
            cur.execute("SELECT PartNumber FROM PART WHERE PartNumber = ?", (PartNumber,))
            parts = cur.fetchall()
            print("number of parts: ", len(parts))

            ##Verify there is a UNIQUE match before deletion
            if(len(parts) == 1):

                buttonReply = QMessageBox.question(self, 'Warning', "This delete is irreversible. Are you sure you want to Delete " + PartNumber +"??", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                
                if buttonReply == QMessageBox.Yes:

                    cur.execute("DELETE FROM PART WHERE PartNumber = ?", (PartNumber,))
                    conn.commit()
                    self.LE_SearchPartNumber.setText("") #Reset text to blank
                    self.setSearchPartNumberCompleter() #Update completer as we have just deleted a part
                if buttonReply == QMessageBox.No:
                    print("nothing done")
            elif(len(parts) > 1):
                QMessageBox.warning(self, "Warning", "Delete operation found multiple matches to this part number and cannot determine which part to delete. This part will not be deleted.")
            else:
                QMessageBox.warning(self, "Warning", "Cannot find that part in the database.")

        except Exception as ex:
            print(ex)


    def translateNut(self, nut):
        if(nut == 1):
            self.isNut = True
        elif(nut == 0):
            self.isNut = False

        return self.isNut

    def translateStud(self, stud):
        if(stud == 1):
            self.isStud = True
        elif(stud == 0):
            self.isStud = False

        return self.isStud

    def translateNoBid(self, nobid):
        if(nobid == 1):
            self.isNoBid = True
        elif(nobid == 0):
            self.isNoBid = False

        return self.isNoBid




    def PBGoToEditPart(self):
        # print("PBGoEditTopart")
        try:
            PartNumber = self.LE_SearchPartNumber.text()
            conn =connectSQLite()        
            cur = conn.cursor()            
            cur.execute("SELECT Description, Rev, MfgSpec, EstBy, Date, Material, Weight, Diam, Shank, HdVol, Heading, Note , Op1,Op2,Op3,Op4,Op5,Op6,Op7,Op8,Op9,Op10,Op11,Op12,Op13,Op14,Op15,Op16,Op17,Op18,Op19,Op20,Op21,Op22,Op23,Op24,Op25,Op26,Op27,Op28,Op29,Op30,Op31,Op32,Op33,Op34,Op35,Op36,Op37,Op38,Op39,Op40 FROM Part WHERE PartNumber = ?",(PartNumber,))
            part = cur.fetchall()
            # print("part: ", part)
            if part == [] :
                QMessageBox.warning(self, "Warning", "Please select a part that belong to the existing list of the completer.")
                return
            try:
                Description = str(part[0][0])
                # print("Description: ", Description)
            except:
                Description = None
            try:
                Revision = str(part[0][1])
                # print("Rev: ", Revision)
            except:
                Revision = None
            try:
                MfgSpec = str(part[0][2])
            except:
                MfgSpec = None
            try:
                EstBy = str(part[0][3])
                if EstBy == 'PS' :
                    EstBy = int(0)
                elif EstBy == 'DD' :
                    EstBy = int(1)
                elif EstBy == 'SO' :
                    EstBy = int(2)
                else :
                    EstBy = int(0)
            except:
                EstBy = None
            try:
                Date = str(part[0][4])
            except:
                Date = None
            try:
                Mat = str(part[0][5])
            except:
                Mat = None
            try:
                Diameter = str(part[0][7])
            except:
                Diameter = None
            try:
                Schank = str(part[0][8])
            except:
                Schank = None
            try:
                HeadOp = str(part[0][10])
                if HeadOp == 'HotHead' :
                    HeadOp = int(0)
                elif HeadOp == 'ColdHead' :
                    HeadOp = int(1)
                elif HeadOp == 'ColdHeadUpset' :
                    HeadOp = int(2)
                elif HeadOp == 'HotHeadUpset' :
                    HeadOp = int(3)
                elif HeadOp == 'MachinePart' :
                    HeadOp = int(4)
            except:
                HeadOp = None
            try:
                Note = str(part[0][11])
            except:
                Note = None
            try:
                Ops = list()
                Ops.clear()
                iii = 12

                    
                while iii <= 51:
                    # print("iii: ", iii)
                    if part[0][iii] == 0:
                        print("breaking")
                        break
                    Ops.append(str(part[0][iii]))

                    iii = iii + 1 
            except:
                Ops = None
            try:
                            ##Check if it's a nut, if not nut assume it is bolt
                self.nut = part[0][52]
                self.translateNut(self.nut)
                # print("nut: ", self.nut)
                # print("isNut: ", self.isNut)
            except:
                self.isNut = False

            try:
                            ##Check if it's a nut, if not nut assume it is bolt
                self.stud = part[0][53]
                self.translateStud(self.stud)
                # print("stud: ", self.stud)
                # print("isStud: ", self.isStud)
            except:
                self.isStud = False

            try:
                self.nobid = part[0][54]
                self.translateNoBid(self.nobid)

            except:
                self.isNoBid = False

            try:
                self.NoBidNote = part[0][55]
            except:
                self.NoBidNote = None

            try:
                self.slugBool = part[0][56]
            except:
                self.slugBool = 0

            try:
                self.HVBool = part[0][57]
            except:
                self.HVBool = 0

            vue = MSACES_NewPart.VueEditPartFilled(self,PartNumber, Description,Revision,MfgSpec,EstBy,Date,Mat,HeadOp,Diameter,Schank,Note,Ops,self.isNut,self.isStud,self.isNoBid,self.NoBidNote,self.slugBool, self.HVBool)
            # vue.showMaximized()
            vue.show()
            
            self.close()
        except Exception as ex:
            printError(ex)

        closeSQLite(conn)




