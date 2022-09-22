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
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 should not be a Invalid input')

    def testdecimalsides(self):
        self.assertEqual(classifyTriangle(3.0,4.0,5.0),"InvalidInput",'3.0,4.0,5.0 is a Invalid Input')

    def testnegativeinput(self):
        self.assertEqual(classifyTriangle(-2,5,10),"InvalidInput","-2,5,10 is a Invalid Input")

    def testnotatriangle(self):
        self.assertEqual(classifyTriangle(5,2,10),"NotATriangle","5,2,10 is not a triangle")

    def teststringinput(self):
        try:
            self.assertEqual(classifyTriangle("s1","s2","s3"),"Error","s1,s2,s3 is a typeerror")
        except TypeError:
            print("InvalidInput")




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
