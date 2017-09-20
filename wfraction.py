#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:02:03 2017

@author: steven
"""
from __future__ import division # import division function from python3

class Fraction(object):
    """
    A simple fraction class.
    """
    def __init__(self, numerator, denominator=1):
        """
        Creates a new fraction.
        """
        self._numerator = numerator
        self._denominator = denominator
     
    def __str__(self):
        """
        Defines the printed output for objects of class Fraction
        """
        return "'" +str(self._numerator) + '/' + str(self._denominator) + "'"
        
    def __add__(self, other):
        """
        Introduces output value from adding to Fraction ojects
        """
        return Fraction((self._numerator * other._denominator + other._numerator *self._denominator), (self._denominator * other._denominator))
    
    def invert(self):
        """
        Function inverts the input Fraction
        """
        return "'" +str(self._denominator) + '/' + str(self._numerator) + "'"

    def to_float(self):
        """
        Gives float value form input Fraction
        """
        return (self._numerator / self._denominator)
    
    def integer(self):
        """
        Displays largest integer for Fraction
        """
        return (self._numerator // self._denominator)
        
    
f1 = Fraction(14,6)
f2 = Fraction(2, 3)

print 'Check print out:'
print f1  #check print
print f2
print 'Check addition:'
print f1 + f2 # check add
print 'Check invert:'
print f1.invert() #check invert
print 'Check to_float:'
print f2.to_float() #check to_float
print 'Check integer:'
print f1.integer() #check integer
