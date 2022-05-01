# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:09:25 2021
A simple implementation of Floyd's algorithm: Unit Test

@author: KHOO TEE WAN
"""

import sys
from recursion import c,floyd


def test_on_c():
    expected=[(0, 0), (1, 0), \
              (2, 0), (0, 1), \
              (1, 1), (2, 1), \
              (0, 2), (1, 2), \
              (2, 2)]
    actual=c([0,1,2],2)
    
    message='Expected return value{0},Actual return value{1}'.format(expected,actual)
    
    assert actual==expected, message

    
def test_on_floyd():
    expected=[[0,5,8,9],
              [sys.maxsize,0,3,4],
              [sys.maxsize,sys.maxsize,0,1],
              [sys.maxsize,sys.maxsize,sys.maxsize,0]]
    
    n=c([0,1,2,3],4)
    actual=floyd([[0,5,sys.maxsize,10],
                 [sys.maxsize,0,3,sys.maxsize],
                 [sys.maxsize,sys.maxsize,0,1],
                 [sys.maxsize,sys.maxsize,sys.maxsize,0]],len(n)-1)
    
    message='Expected return value{0},Actual return value{1}'.format(expected,actual)
    
    assert actual==expected, message