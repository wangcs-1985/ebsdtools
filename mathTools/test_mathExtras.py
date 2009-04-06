#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe Pinard (philippe.pinard@gmail.com)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2008 Philippe Pinard"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = ""
__svnDate__ = ""
__svnId__ = ""

# Standard library modules.
import unittest
from math import pi, acos

# Third party modules.

# Local modules.
import EBSDTools.mathTools.mathExtras as mathExtras
from RandomUtilities.testing.testOthers import almostEqual

class TestEulers(unittest.TestCase):

  def setUp(self):
    unittest.TestCase.setUp(self)
    
  def tearDown(self):
    unittest.TestCase.tearDown(self)
    
  def testSkeleton(self):
    #self.fail("Test if the TestCase is working.")
    self.assert_(True)
  
  def testConstants(self):
    self.assert_(almostEqual(mathExtras.h, 6.62606809633e-34))
    self.assert_(almostEqual(mathExtras.m_e, 9.1093818e-31))
    self.assert_(almostEqual(mathExtras.e, 1.60217646e-19))
    self.assert_(almostEqual(mathExtras.c, 2.99792458e8))
    
    self.assert_(almostEqual(mathExtras.zeroPrecision, 1e-5))
  
  def test_acos(self):
    self.assertEqual(mathExtras._acos(4), 0)
    self.assertEqual(mathExtras._acos(-4), pi)
    self.assert_(almostEqual(mathExtras._acos(0.5), 60/180.0*pi))
    self.assert_(almostEqual(mathExtras._acos(0.45675), acos(0.45675)))

if __name__ == '__main__':
  unittest.main()