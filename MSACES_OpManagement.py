# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:03:20 2019

@author: stefflc
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCompleter


from MSACES_genericFunctions import closeSQLite
from MSACES_genericFunctions import connectSQLite
from MSACES_genericFunctions import printError
from MSACES_OpManagement_UI import Ui_OpManagement

class VueOpManagement(QtWidgets.QDialog,Ui_OpManagement):

    def __init__(self, parent):
        super(VueOpManagement, self).__init__(parent)
        self.setupUi(self) 
        # conn = MSACES.CES.connectSQLite()
        conn = connectSQLite()
        cur = conn.cursor()         
        self.LE_ChooseOP.returnPressed.connect(self.remplirtable)
        ############CHANGED ?? ##########
        # self.LE_ChooseOP.currentIndexChanged.connect(self.remplirtable)

        self.PB_ValidateNewOp.clicked.connect(self.Addnewop)
        self.LookUpEditOp.clicked.connect(self.remplirtable)
        self.FillColumn.clicked.connect(self.fillColumn)
        self.FillRow.clicked.connect(self.fillRow)
        self.saveEdit.clicked.connect(self.saveChanges)

        self.setCompleters()

        cur.execute("SELECT MAX(Number) FROM OP")
        number = cur.fetchone()
        
        nextnumber = str(number[0]+1)
        
        self.LE_OpNumber.setText(nextnumber)

        
        

        
# Table Operation fenetre 1 
  
        cur.execute("SELECT Number, Name, Min FROM Op")
        Op = cur.fetchall()
        
        nbligne = len(Op)
        self.TableOperation.setRowCount(nbligne)
        
        n = 0
        while n <= len(Op)-1:
            
            a1 = str(Op[n][0])        
            a1 = QtWidgets.QTableWidgetItem(a1)
            self.TableOperation.setItem(n,0,a1)   
            
            a2 = str(Op[n][1])        
            a2 = QtWidgets.QTableWidgetItem(a2)
            self.TableOperation.setItem(n,1,a2)
            
            a3 = str(Op[n][2])        
            a3 = QtWidgets.QTableWidgetItem(a3)
            self.TableOperation.setItem(n,2,a3)
            
            n = n+1 
        
        self.TableOperation.cellDoubleClicked.connect(self.UpdateTableOperation)
        # MSACES.CES.closeSQLite(conn)
        closeSQLite(conn)

    '''
    Allow user to fill remainder of row based on starting position.
    If user starts at row 2, row 3 and below will fill in with value of row 2.
    '''
    def fillColumn(self):
        a = self.TableEditOp.currentRow()
        b = self.TableEditOp.currentColumn()
        print("a: ", a)
        print("b: ", b)
        # 0, 0
        # max is row 10, col 4
        try:
            valueToCopy = self.TableEditOp.item(a,b).text()

            if (valueToCopy):
                n = (a+1)
                while n < 10:
                    print('success')
                    print("self.TableEditOp.item(b,0).text(): ", valueToCopy)
                    # a1 = str(EditOp[n+4])
                    a1 = QtWidgets.QTableWidgetItem(valueToCopy)
                    self.TableEditOp.setItem(n, b,a1)
                    n = n + 1
        except AttributeError :
            row = a+1 #Count from 1 not 0 for humans
            column = b+1 #Count from 1 not 0 for humans
            QMessageBox.about(self, "Warning", "Row %s, Column %s is empty." %(row, column))
        except Exception as ex:
            printError(ex)

    def fillRow(self):
        a = self.TableEditOp.currentRow()
        b = self.TableEditOp.currentColumn()
        print("a: ", a)
        print("b: ", b)

        try:
            valueToCopy = self.TableEditOp.item(a, b).text()

            if (valueToCopy):
                n = (b+1)
                while n < 5:
                    print('success')
                    print("self.TableEditOp.item(a, 0).text(): ", valueToCopy)
                    # a1 = str(EditOp[n+4])
                    a1 = QtWidgets.QTableWidgetItem(valueToCopy)
                    self.TableEditOp.setItem(a, n,a1)
                    n = n + 1
        except AttributeError :
            row = a+1 #Count from 1 not 0 for humans
            column = b+1 #Count from 1 not 0 for humans
            QMessageBox.about(self, "Warning", "Row %s, Column %s is empty." %(row, column))
        except Exception as ex:
            printError(ex)


    def setCompleters(self):
        conn = connectSQLite()
        cur = conn.cursor()
        
        #set completer for unit box on Add New Operation tab

        unitList = list()
        unitList.append('pc')
        unitList.append('lb')

        unitCmpt = QCompleter(unitList)
        unitCmpt.setCaseSensitivity(0)
        unitCmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        # self.LE_UnitOp.setCompleter(unitCmpt)
        self.LE_UnitOp.addItem('pc')
        self.LE_UnitOp.addItem('lb')
        self.LE_UnitOp.currentIndexChanged.connect(self.setUnitMeasure)


        ###Set completer for Choose your operation on Edit Operation Cost
        cur.execute("SELECT Name FROM Op ORDER BY Name ASC")
        part = cur.fetchall()
        
        listnum = []
        for prt in part:
            for p in prt:
                listnum.append(str(p))  
                       
        cmpt = QCompleter(listnum)  
        cmpt.setCaseSensitivity(0)
        cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.LE_ChooseOP.setCompleter(cmpt)


        self.EditUnit.setCompleter(unitCmpt)

        closeSQLite(conn)
    def setUnitMeasure(self):
        # print("ombo text: ", self.LE_UnitOp.currentText() )
        # print("222: ", self.LE_UnitOp.text())
        self.LE_UnitOp

    def UpdateTableOperation(self):
        # conn = MSACES.CES.connectSQLite()
        conn = connectSQLite()
        cur = conn.cursor()
        a = self.TableOperation.currentRow()
        a = int(a)
        
        number = self.TableOperation.item(a,0).text()
        
        b = self.TableOperation.currentColumn()
        b = int(b)
        
        if b == 0 :   
            QMessageBox.warning(self, "Warning", "This field is protected, your modification will not be saved. Please choose the -add operation- option to create a new operation")
            return
        elif b == 1 :
            tabcolumn = "Name"   
        elif b == 2 :
            tabcolumn = "Min"        
        
        toedit = self.TableOperation.item(a,b).text()
        
        cur.execute("UPDATE Op SET %s = ? WHERE Number = ?" %tabcolumn,(toedit,number) )
        conn.commit() 
        
        QMessageBox.about(self, "Confimation", "Operation updated.")
        # MSACES.CES.closeSQLite(conn)
        closeSQLite(conn)

# Table Edit Operation  fenetre 2        
         
    def remplirtable(self):
        # conn = MSACES.CES.connectSQLite()
        conn = connectSQLite()
        cur = conn.cursor()

        name = self.LE_ChooseOP.text()
        # print("name: ", name)
        cur.execute("SELECT * FROM Op WHERE Name = ?",(name,))            
        EditOp = cur.fetchone()
        self.EditName.setText(name)
        # print("Edit Op: ", EditOp[0], EditOp[1],EditOp[2],EditOp[3])
        minimum = str(EditOp[2])
        op = str(EditOp[0])
        unit = str(EditOp[3])
        self.EditMin.setText(minimum)
        self.EditOp.setText(op)
        self.EditUnit.setText(unit)

        n = 0
        while n <= 10:
                
            a1 = str(EditOp[n+4])        
            a1 = QtWidgets.QTableWidgetItem(a1)
            self.TableEditOp.setItem(n,0,a1)
                
            a2 = str(EditOp[n+11+4])        
            a2 = QtWidgets.QTableWidgetItem(a2)
            self.TableEditOp.setItem(n,1,a2)
                
            a3 = str(EditOp[n+22+4])        
            a3 = QtWidgets.QTableWidgetItem(a3)
            self.TableEditOp.setItem(n,2,a3)
                
            a3 = str(EditOp[n+33+4])        
            a3 = QtWidgets.QTableWidgetItem(a3)
            self.TableEditOp.setItem(n,3,a3)
                
            a4 = str(EditOp[n+44+4])        
            a4 = QtWidgets.QTableWidgetItem(a4)
            self.TableEditOp.setItem(n,4,a4)
                  
            n = n+1 
            
        self.TableEditOp.cellDoubleClicked.connect(self.UpdateTableEditOp)
        closeSQLite(conn)

    def UpdateTableEditOp(self):
        # conn = MSACES.CES.connectSQLite()
        conn = connectSQLite()
        cur = conn.cursor()
        name = self.LE_ChooseOP.text()
        
        a = self.TableEditOp.currentRow()
        a = int(a)
        
        num = str(a+1)
        
        if a <= 9 :
            tabcolumn = str("DG"+num)
        elif a == 10:
            tabcolumn = "SU"
               
        b = self.TableEditOp.currentColumn()
        b = int(b)
        
        if b == 0 :
            g = "B"
        elif b == 1:
            g = "C"
        elif b == 2:
            g = "D"
        elif b == 3:
            g = "E"
        elif b == 4:
            g = "F"
        
        tabcolumn = str(tabcolumn+g)
        
        toedit = self.TableEditOp.item(a,b).text()
        
        cur.execute("UPDATE Op SET %s = ? WHERE Name = ?" %tabcolumn,(toedit,name) )
        conn.commit()
        
        QMessageBox.about(self, "Confimation", "Operation updated.")
        closeSQLite(conn)

    '''
    Save Chagnes on window 2
    '''
    def saveChanges(self):
        conn = connectSQLite()
        cur = conn.cursor()

        name = self.EditName.text()
        minimum = self.EditMin.text()
        minimum = int(minimum)
        opnum = self.EditOp.text()
        opnum = int(opnum) #int required for SQL query
        unit = self.EditUnit.text()



        dg1b = self.TableEditOp.item(0,0).text()
        dg2b = self.TableEditOp.item(1,0).text()
        dg3b = self.TableEditOp.item(2,0).text()
        dg4b = self.TableEditOp.item(3,0).text()
        dg5b = self.TableEditOp.item(4,0).text()
        dg6b = self.TableEditOp.item(5,0).text()
        dg7b = self.TableEditOp.item(6,0).text()
        dg8b = self.TableEditOp.item(7,0).text()
        dg9b = self.TableEditOp.item(8,0).text()
        dg10b = self.TableEditOp.item(9,0).text()
        sub = self.TableEditOp.item(10,0).text()
        dg1c = self.TableEditOp.item(0,1).text()
        dg2c = self.TableEditOp.item(1,1).text()
        dg3c = self.TableEditOp.item(2,1).text()
        dg4c = self.TableEditOp.item(3,1).text()
        dg5c = self.TableEditOp.item(4,1).text()
        dg6c = self.TableEditOp.item(5,1).text()
        dg7c = self.TableEditOp.item(6,1).text()
        dg8c = self.TableEditOp.item(7,1).text()
        dg9c = self.TableEditOp.item(8,1).text()
        dg10c = self.TableEditOp.item(9,1).text()
        suc = self.TableEditOp.item(10,1).text()
        dg1d = self.TableEditOp.item(0,2).text()
        dg2d = self.TableEditOp.item(1,2).text()
        dg3d = self.TableEditOp.item(2,2).text()
        dg4d = self.TableEditOp.item(3,2).text()
        dg5d = self.TableEditOp.item(4,2).text()
        dg6d = self.TableEditOp.item(5,2).text()
        dg7d = self.TableEditOp.item(6,2).text()
        dg8d = self.TableEditOp.item(7,2).text()
        dg9d = self.TableEditOp.item(8,2).text()
        dg10d = self.TableEditOp.item(9,2).text()
        sud = self.TableEditOp.item(10,2).text()
        dg1e = self.TableEditOp.item(0,3).text()
        dg2e = self.TableEditOp.item(1,3).text()
        dg3e = self.TableEditOp.item(2,3).text()
        dg4e = self.TableEditOp.item(3,3).text()
        dg5e = self.TableEditOp.item(4,3).text()
        dg6e = self.TableEditOp.item(5,3).text()
        dg7e = self.TableEditOp.item(6,3).text()
        dg8e = self.TableEditOp.item(7,3).text()
        dg9e = self.TableEditOp.item(8,3).text()
        dg10e = self.TableEditOp.item(9,3).text()
        sue = self.TableEditOp.item(10,3).text()
        dg1f = self.TableEditOp.item(0,4).text()
        dg2f = self.TableEditOp.item(1,4).text()
        dg3f = self.TableEditOp.item(2,4).text()
        dg4f = self.TableEditOp.item(3,4).text()
        dg5f = self.TableEditOp.item(4,4).text()
        dg6f = self.TableEditOp.item(5,4).text()
        dg7f = self.TableEditOp.item(6,4).text()
        dg8f = self.TableEditOp.item(7,4).text()
        dg9f = self.TableEditOp.item(8,4).text()
        dg10f = self.TableEditOp.item(9,4).text()
        suf = self.TableEditOp.item(10,4).text()




        try:
            # print(type(opnum))
            # print(type(minimum))
            cur.execute('''UPDATE Op SET Name = ?,       
            Min = ?,Unit = ?,DG1B =?,DG2B = ?,DG3B = ?,
            DG4B = ?, DG5B = ?,DG6B = ?, DG7B = ?, DG8B = ?, 
            DG9B = ?,  DG10B = ?,SUB = ?, 
            DG1C  = ?,
            DG2C = ?, 
            DG3C = ?, 
            DG4C = ?, 
            DG5C = ?, 
            DG6C = ?, 
            DG7C = ?, 
            DG8C = ?, 
            DG9C = ?, 
            DG10C = ?, 
            SUC = ?, 
            DG1D  = ?,
            DG2D = ?, 
            DG3D = ?, 
            DG4D = ?, 
            DG5D = ?, 
            DG6D = ?, 
            DG7D = ?, 
            DG8D = ?, 
            DG9D = ?, 
            DG10D = ?, 
            SUD = ?, 
            DG1E  = ?,DG2E = ?, DG3E = ?, DG4E = ?, DG5E = ?, 
            DG6E = ?, DG7E = ?, DG8E = ?, DG9E = ?, DG10E = ?, SUE = ?, 
            DG1F = ? ,DG2F = ?, DG3F = ?, DG4F = ?, DG5F = ?, DG6F = ?, 
            DG7F = ?, DG8F = ?, DG9F = ?, DG10F = ?, SUF = ?
            WHERE Number = ?''',(name,minimum,unit,dg1b,dg2b,dg3b,dg4b,dg5b,dg6b,dg7b,dg8b,dg9b,dg10b,sub,dg1c,dg2c,dg3c,dg4c,dg5c,dg6c,dg7c,dg8c,dg9c,dg10c,suc,dg1d,dg2d,dg3d,dg4d,dg5d,dg6d,dg7d,dg8d,dg9d,dg10d,sud,dg1e,dg2e,dg3e,dg4e,dg5e,dg6e,dg7e,dg8e,dg9e,dg10e,sue,dg1f,dg2f,dg3f,dg4f,dg5f,dg6f,dg7f,dg8f,dg9f,dg10f,suf,opnum))
            conn.commit()

            QMessageBox.about(self, "Confimation", "The operation "+ str(opnum) + " has been updated successfully.")
        except Exception as ex:
            printError(ex)






# Table add new operation fenetre 3
    
    def Addnewop(self):
        conn = connectSQLite()
        cur = conn.cursor() 
        number = self.LE_OpNumber.text()
        name = self.LE_OpName.text()
        minimum = self.LE_OpMin.text()
        try:
            unit = self.LE_UnitOp.text()
        except:
            unit = self.LE_UnitOp.currentText()

        dg1b = self.TableNewOp.item(0,0).text()
        dg2b = self.TableNewOp.item(1,0).text()
        dg3b = self.TableNewOp.item(2,0).text()
        dg4b = self.TableNewOp.item(3,0).text()
        dg5b = self.TableNewOp.item(4,0).text()
        dg6b = self.TableNewOp.item(5,0).text()
        dg7b = self.TableNewOp.item(6,0).text()
        dg8b = self.TableNewOp.item(7,0).text()
        dg9b = self.TableNewOp.item(8,0).text()
        dg10b = self.TableNewOp.item(9,0).text()
        sub = self.TableNewOp.item(10,0).text()
        dg1c = self.TableNewOp.item(0,1).text()
        dg2c = self.TableNewOp.item(1,1).text()
        dg3c = self.TableNewOp.item(2,1).text()
        dg4c = self.TableNewOp.item(3,1).text()
        dg5c = self.TableNewOp.item(4,1).text()
        dg6c = self.TableNewOp.item(5,1).text()
        dg7c = self.TableNewOp.item(6,1).text()
        dg8c = self.TableNewOp.item(7,1).text()
        dg9c = self.TableNewOp.item(8,1).text()
        dg10c = self.TableNewOp.item(9,1).text()
        suc = self.TableNewOp.item(10,1).text()
        dg1d = self.TableNewOp.item(0,2).text()
        dg2d = self.TableNewOp.item(1,2).text()
        dg3d = self.TableNewOp.item(2,2).text()
        dg4d = self.TableNewOp.item(3,2).text()
        dg5d = self.TableNewOp.item(4,2).text()
        dg6d = self.TableNewOp.item(5,2).text()
        dg7d = self.TableNewOp.item(6,2).text()
        dg8d = self.TableNewOp.item(7,2).text()
        dg9d = self.TableNewOp.item(8,2).text()
        dg10d = self.TableNewOp.item(9,2).text()
        sud = self.TableNewOp.item(10,2).text()
        dg1e = self.TableNewOp.item(0,3).text()
        dg2e = self.TableNewOp.item(1,3).text()
        dg3e = self.TableNewOp.item(2,3).text()
        dg4e = self.TableNewOp.item(3,3).text()
        dg5e = self.TableNewOp.item(4,3).text()
        dg6e = self.TableNewOp.item(5,3).text()
        dg7e = self.TableNewOp.item(6,3).text()
        dg8e = self.TableNewOp.item(7,3).text()
        dg9e = self.TableNewOp.item(8,3).text()
        dg10e = self.TableNewOp.item(9,3).text()
        sue = self.TableNewOp.item(10,3).text()
        dg1f = self.TableNewOp.item(0,4).text()
        dg2f = self.TableNewOp.item(1,4).text()
        dg3f = self.TableNewOp.item(2,4).text()
        dg4f = self.TableNewOp.item(3,4).text()
        dg5f = self.TableNewOp.item(4,4).text()
        dg6f = self.TableNewOp.item(5,4).text()
        dg7f = self.TableNewOp.item(6,4).text()
        dg8f = self.TableNewOp.item(7,4).text()
        dg9f = self.TableNewOp.item(8,4).text()
        dg10f = self.TableNewOp.item(9,4).text()
        suf = self.TableNewOp.item(10,4).text()
          
        
        req = "INSERT INTO Op(Number, Name , Min, Unit, DG1B ,DG2B, DG3B, DG4B, DG5B, DG6B, DG7B, DG8B, DG9B, DG10B, SUB, DG1C ,DG2C, DG3C, DG4C, DG5C, DG6C, DG7C, DG8C, DG9C, DG10C, SUC, DG1D ,DG2D, DG3D, DG4D, DG5D, DG6D, DG7D, DG8D, DG9D, DG10D, SUD, DG1E ,DG2E, DG3E, DG4E, DG5E, DG6E, DG7E, DG8E, DG9E, DG10E, SUE, DG1F ,DG2F, DG3F, DG4F, DG5F, DG6F, DG7F, DG8F, DG9F, DG10F, SUF) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(req, (number,name,minimum,unit,dg1b,dg2b,dg3b,dg4b,dg5b,dg6b,dg7b,dg8b,dg9b,dg10b,sub,dg1c,dg2c,dg3c,dg4c,dg5c,dg6c,dg7c,dg8c,dg9c,dg10c,suc,dg1d,dg2d,dg3d,dg4d,dg5d,dg6d,dg7d,dg8d,dg9d,dg10d,sud,dg1e,dg2e,dg3e,dg4e,dg5e,dg6e,dg7e,dg8e,dg9e,dg10e,sue,dg1f,dg2f,dg3f,dg4f,dg5f,dg6f,dg7f,dg8f,dg9f,dg10f,suf))
        conn.commit()
        
        num = str(number)
        QMessageBox.about(self, "Confimation", "The operation "+ num + " has been added successfully.")
        
        cur.execute("SELECT MAX(Number) FROM OP")
        number = cur.fetchone()
        
        nextnumber = str(number[0]+1)
        
        self.LE_OpNumber.setText(nextnumber)
        
        self.LE_OpName.clear()
        self.LE_OpMin.clear()
        self.LE_UnitOp.clear()
        
        ii = 0
        while ii <= 4 :
            iii = 0
            while iii <= 10 :
                self.TableNewOp.item(iii,ii).clear()
                iii=iii+1
            ii = ii+1
        closeSQLite(conn)
