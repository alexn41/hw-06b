# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 8, 9), 'Scalene')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 188), 'NotATriangle')

    def testInvalidLow(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput')

    def testInvalidHigh(self):
        self.assertEqual(classifyTriangle(3, 543678, 6), 'InvalidInput')

    def testNotANumber(self):
        self.assertEqual(classifyTriangle(3, 5, 'hi'), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

