# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:27:23 2019

@author: stefflc


Test Suite for all CES Unit Tests

"""


# ########################
# This file needs additional tests to verify
# Material Management (Raw)
# and Op Management
# #########################

import test_SearchPart
import test_NewPart
import test_Quote
import unittest

'''
Run all tests for the MSACES_SearchPart.py File
existing in the test_SearchPart.py File
'''
suite = unittest.TestLoader().loadTestsFromModule(test_SearchPart)
unittest.TextTestRunner(verbosity=2).run(suite)


'''
Run all tests for the MSACES_NewPart.py File 
existing in the test_NewPart.py File '''

suiteNewPart = unittest.TestLoader().loadTestsFromModule(test_NewPart)
unittest.TextTestRunner(verbosity=2).run(suiteNewPart)

'''
Run all tests for the MSACES_NewPart.py File 
existing in the test_NewPart.py File '''
suiteQuote = unittest.TestLoader().loadTestsFromModule(test_Quote)
unittest.TextTestRunner(verbosity=2).run(suiteQuote)