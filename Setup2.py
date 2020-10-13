# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:14:24 2017

@author: tastetf
"""

"""Fichier d'installation script """

import sys
from cx_Freeze import setup, Executable



# On appelle la fonction setup
setup(
    name = "MSACES",
    version = "0.1",
    description = "Cost Estimating System",
    executables = [Executable("MSACES.py")],
)