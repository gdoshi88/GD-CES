# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:19:49 2019

@author: stefflc
"""
import traceback
import os
import sqlite3
from math import pi


def connectSQLite():
    try:
        desktoppath = os.path.join(os.path.expanduser("~"), "Desktop") ###PRODUCTION
        way = str(desktoppath)+"\\CES\\" +"db_Synoptic" ###PRODUCTION
        conn = sqlite3.connect(way) ###PRODUCTION
        
        return conn
    except Exception as ex:
        printError(ex)


def closeSQLite(conn):
    try:
        if(conn is not None):
            conn.close()
    except UnboundLocalError:
        print("Connection is already closed")
    except Exception as ex:
        printError(ex)


def printError(ex):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    traceback.print_exc()


def trouvercout(group,Diam):
    # print("trouvercout running")
    if group == "B":
        if Diam <= 0.188 :
            return "SUB","DG1B"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUB","DG2B"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUB","DG3B"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUB","DG4B"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUB","DG5B"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUB","DG6B"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUB","DG7B"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUB","DG8B"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUB","DG9B"
        elif Diam > 1.125:
            return "SUB","DG10B"
    elif group == "C":
        if Diam <= 0.188 :
            return "SUC","DG1C"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUC","DG2C"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUC","DG3C"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUC","DG4C"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUC","DG5C"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUC","DG6C"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUC","DG7C"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUC","DG8C"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUC","DG9C"
        elif Diam > 1.125:
            return "SUC","DG10C"
    elif group == "D":
        if Diam <= 0.188 :
            return "SUD","DG1D"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUD","DG2D"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUD","DG3D"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUD","DG4D"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUD","DG5D"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUD","DG6D"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUD","DG7D"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUD","DG8D"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUD","DG9D"
        elif Diam > 1.125:
            return "SUD","DG10D"
    elif group == "E":
        if Diam <= 0.188 :
            return "SUE","DG1E"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUE","DG2E"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUE","DG3E"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUE","DG4E"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUE","DG5E"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUE","DG6E"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUE","DG7E"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUE","DG8E"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUE","DG9E"
        elif Diam > 1.125:
            return "SUE","DG10E"
    elif group == "F":
        if Diam <= 0.188 :
            return "SUF","DG1F"
        elif Diam > 0.188 and Diam <= 0.250:
            return "SUF","DG2F"
        elif Diam > 0.250 and Diam <= 0.375:
            return "SUF","DG3F"
        elif Diam > 0.375 and Diam <= 0.500:
            return "SUF","DG4F"
        elif Diam > 0.500 and Diam <= 0.625:
            return "SUF","DG5F"
        elif Diam > 0.625 and Diam <= 0.750:
            return "SUF","DG6F"
        elif Diam > 0.750 and Diam <= 0.875:
            return "SUF","DG7F"
        elif Diam > 0.875 and Diam <= 1.000:
            return "SUF","DG8F"
        elif Diam > 1.000 and Diam <= 1.125:
            return "SUF","DG9F"
        elif Diam > 1.125:
            return "SUF","DG10F"

'''
Calculate part weight given
material type, slug length, shank diameter

'''
def calculatePW(mattype, SLUG, diam):
# Calcul du Part Weight
#THESE CALCULATIONS ARE ALSO DONE IN MASCES_NEWPART_UI
#IF YOU MAKE CHANGES MAKE SURE THEY ARE CHANGED THERE AS WELL

    # print("mattype: ", mattype)
    # print("SLUG: ", SLUG)
    # print("diam: ", diam)

    # print("mattype: ", type(mattype))
    # print("SLUG: ", type(SLUG))
    # print("diam: ", type(diam))

    if mattype == "Steel" or mattype == "NiBase" :
        
        PW = (pi*((diam*diam)/4)*SLUG)*0.3
                
    elif mattype == "Titan" :
        
        PW = (pi*((diam*diam)/4)*SLUG)*0.17
        
    elif mattype == "Alum" :
        
        PW = (pi*((diam*diam)/4)*SLUG)*0.2
    else:
        raise NameError("Please choose a valid material!")


    PW = round(PW,3)

    return PW
