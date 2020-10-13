# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:18:10 2019

@author: stefflc
"""
from MSACES_MM_UI import Ui_MaterialManagement
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


import os
from MSACES_genericFunctions import closeSQLite
from MSACES_genericFunctions import connectSQLite
import sqlite3
#==============================================================================
# Classe permettant l'affichage de la fenetre
        
# conn = sqlite3.connect("db_Synoptic")

# desktoppath = os.path.join(os.path.expanduser("~"), "Desktop") ###PRODUCTION
# way = str(desktoppath)+"\\CES\\" +"db_Synoptic" ###PRODUCTION
# conn = sqlite3.connect(way) ###PRODUCTION
# cur = conn.cursor()

class VueMaterialManagement(QtWidgets.QDialog,Ui_MaterialManagement):

    def __init__(self, parent):
        super(VueMaterialManagement, self).__init__(parent)
        self.setupUi(self) 
        self.PB_SetAllCost.clicked.connect(self.setall)
        self.PB_SetFromTo.clicked.connect(self.setfromto)
        self.PB_EnterMat.clicked.connect(self.remplirmat)
        self.PB_NewRawMat.clicked.connect(self.addrawmat)
        self.PB_ShowAll.clicked.connect(self.showAllMat)


        conn =connectSQLite()
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT Name FROM Mat ORDER BY Name ASC")
        name = cur.fetchall()
        
        listnum = []
        for prt in name:
            for p in prt:
                listnum.append(str(p))  
                       
        cmpt = QCompleter(listnum)  
        cmpt.setCaseSensitivity(0)
        cmpt.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.LE_MatName.setCompleter(cmpt)
  
        cur.execute("SELECT MAX(Number) FROM Mat")
        number = cur.fetchone()
        
        nextnumber = str(number[0]+1)
        
        self.LE_RawNumber.setText(nextnumber)
        closeSQLite(conn)

    def setfromto(self):
        
        name = self.LE_MatName.text()
        cost = self.LE_SetFromTo.text()
        diamfrom = self.LE_SetFromDiam.text()
        diamto = self.LE_SetToDiam.text()
        conn =connectSQLite()
        cur = conn.cursor()
        cur.execute("UPDATE MAT SET Cost = ? WHERE Name = ? AND Diam > ? AND Diam < ?",(cost,name,diamfrom,diamto))
        conn.commit()
        
        self.remplirmat()
        
        QMessageBox.about(self, "Confimation", "Cost updated")
        
        self.LE_SetFromTo.clear()
        self.LE_SetFromDiam.clear()
        self.LE_SetToDiam.clear()
        closeSQLite(conn)


    def setall(self):
        
        name = self.LE_MatName.text()
        cost = self.LE_SetAllCost.text()
        conn =connectSQLite()
        cur = conn.cursor()
        cur.execute("UPDATE MAT SET Cost = ? WHERE Name = ?",(cost,name))
        conn.commit()
        
        self.remplirmat()
        
        QMessageBox.about(self, "Confimation", "Cost updated")
        self.LE_SetAllCost.clear()
        closeSQLite(conn)

    def showAllMat(self):
        self.tableMM.clearContents()
        
        # name = self.LE_MatName.text()
        conn =connectSQLite()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Mat  ORDER BY Number ASC")
        Mat = list(cur)
        
        nbligne = len(Mat)
        self.tableMM.setRowCount(nbligne)
        
        n = 0
        while n <= len(Mat)-1:
            
            a1 = str(Mat[n][0])        
            a1 = QtWidgets.QTableWidgetItem(a1)
            self.tableMM.setItem(n,0,a1)   
            
            a3 = str(Mat[n][2])        
            a3 = QtWidgets.QTableWidgetItem(a3)
            self.tableMM.setItem(n,3,a3)
            
            a4 = str(Mat[n][3])        
            a4 = QtWidgets.QTableWidgetItem(a4)
            self.tableMM.setItem(n,4,a4)
            
            a5 = str(Mat[n][4])        
            a5 = QtWidgets.QTableWidgetItem(a5)
            self.tableMM.setItem(n,5,a5)
            
            a6 = str(Mat[n][5])        
            a6 = QtWidgets.QTableWidgetItem(a6)
            self.tableMM.setItem(n,6,a6)
            
            a7 = str(Mat[n][6])        
            a7 = QtWidgets.QTableWidgetItem(a7)
            self.tableMM.setItem(n,1,a7)
            
            a8 = str(Mat[n][7])  
            a8 = QtWidgets.QTableWidgetItem(a8)
            self.tableMM.setItem(n,2,a8)
            
            n = n+1
        
        self.tableMM.cellDoubleClicked.connect(self.UpdateTable)
        closeSQLite(conn)


    def remplirmat(self):
        
        self.tableMM.clearContents()
        
        name = self.LE_MatName.text()
        conn =connectSQLite()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Mat WHERE Name = ? ORDER BY Diam ASC",(name,))
        Mat = list(cur)
        
        nbligne = len(Mat)
        self.tableMM.setRowCount(nbligne)
        
        n = 0
        while n <= len(Mat)-1:
            
            a1 = str(Mat[n][0])        
            a1 = QtWidgets.QTableWidgetItem(a1)
            self.tableMM.setItem(n,0,a1)   
            
            a3 = str(Mat[n][2])        
            a3 = QtWidgets.QTableWidgetItem(a3)
            self.tableMM.setItem(n,3,a3)
            
            a4 = str(Mat[n][3])        
            a4 = QtWidgets.QTableWidgetItem(a4)
            self.tableMM.setItem(n,4,a4)
            
            a5 = str(Mat[n][4])        
            a5 = QtWidgets.QTableWidgetItem(a5)
            self.tableMM.setItem(n,5,a5)
            
            a6 = str(Mat[n][5])        
            a6 = QtWidgets.QTableWidgetItem(a6)
            self.tableMM.setItem(n,6,a6)
            
            a7 = str(Mat[n][6])        
            a7 = QtWidgets.QTableWidgetItem(a7)
            self.tableMM.setItem(n,1,a7)
            
            a8 = str(Mat[n][7])  
            a8 = QtWidgets.QTableWidgetItem(a8)
            self.tableMM.setItem(n,2,a8)
            
            n = n+1
        
        self.tableMM.cellDoubleClicked.connect(self.UpdateTable)
        closeSQLite(conn)


    def UpdateTable(self):
             
        a = self.tableMM.currentRow()
        a = int(a)
        
        number = self.tableMM.item(a,0).text()
        
        b = self.tableMM.currentColumn()
        b = int(b)
        
        if b == 0 :  
            QMessageBox.warning(self, "Warning", "This field is protected, your modification will not be saved. Please choose the -add raw material- option to create a new number")
            return
        elif b == 1 :
            tabcolumn = "Diam"
        elif b == 2 :
            tabcolumn = "Cost"
        elif b == 3 :
            tabcolumn = "Spec"
        elif b == 4 :
            tabcolumn = "Type"
            toedit = self.tableMM.item(a,b).text()
            if toedit != "Steel" and toedit != "NiBase" and toedit != "Alum" and toedit != "Titan" :
                QMessageBox.warning(self, "Warning", "Wrong input, this field must be one of the following type : Steel, NiBase, Alum or Titan")
                return      
        elif b == 5 :
            tabcolumn = "Form"
            toedit = self.tableMM.item(a,b).text()
            if toedit != "Bar" and toedit != "Coil" and toedit != "Hex" :
                QMessageBox.warning(self, "Warning", "Wrong input, this field must be one of the following form : Bar, Coil or Hex")
                return 
        elif b == 6 :
            tabcolumn = "Groupe"
            toedit = self.tableMM.item(a,b).text()
            if toedit != "B" and toedit != "C" and toedit != "D" and toedit != "E" and toedit != "F":
                QMessageBox.warning(self, "Warning", "Wrong input, this field must be one of the following form : B, C, D, E or F")
                return 
              
        toedit = self.tableMM.item(a,b).text()
        conn =connectSQLite()
        cur = conn.cursor()
        cur.execute("UPDATE Mat SET %s = ? WHERE Number = ?" %tabcolumn,(toedit,number) )
        conn.commit() 
        
        QMessageBox.about(self, "Confirmation", "Update done" )
                
        
        closeSQLite(conn)


    def addrawmat(self):
        
        cur.execute("SELECT MAX(Number) FROM Mat")
        number = cur.fetchone()
        
        nextnumber = str(number[0]+1)
        
        number = self.LE_RawNumber.text()
        if number != nextnumber :
            number = nextnumber
            QMessageBox.warning(self, "Warning", "The number of the raw material has been automaticaly set to "+number+"." )
        name = self.LE_RawName.text()
        spec = self.LE_RawSpec.text()
        diam = self.LE_RawDiam.text()
        cost = self.LE_RawCost.text()
        
        rawtype = self.CB_Type.currentIndex()
        if rawtype == 0 :
            rawtype = "Steel"
        elif rawtype == 1 :
            rawtype = "NiBase"
        elif rawtype == 2 :
            rawtype = "Alum"
        elif rawtype == 3 :
            rawtype = "Titan"
        form = self.CB_Form.currentIndex()
        if form == 0 :
            form = "Bar"
        elif form == 1 :
            form = "Coil"  
        elif form == 2 :
            form = "Hex" 
        group = self.CB_Group.currentIndex()
        if group == 0 :
            group = "B"
        elif group == 1 :
            group = "C"
        elif group == 2 :
            group = "D"
        elif group == 3 :
            group = "E"
        elif group == 4 :
            group = "F"

        conn =connectSQLite()
        cur = conn.cursor()
        req = "INSERT INTO Mat(Number, Name , Spec, Type, Form, Groupe, Diam, Cost) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(req, (number,name,spec,rawtype,form,group,diam,cost))
        conn.commit()
        
        name = self.LE_RawName.clear()
        spec = self.LE_RawSpec.clear()
        diam = self.LE_RawDiam.clear()
        cost = self.LE_RawCost.clear()
                
        QMessageBox.about(self, "Confirmation", "Raw Material number :"+number+ "has been added successfully" )
        
        newnextnumber = int(number) + 1
        newnextnumber = str(newnextnumber)
        self.LE_RawNumber.setText(newnextnumber)
        closeSQLite(conn)

