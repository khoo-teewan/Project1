# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:09:31 2022
A simple implementation of Floyd's algorithm: Performance Program
@author: KHOO TEE WAN

"""
import timeit

# Performance test for recursion program

SETUP_CODE = '''    
"""Import floyd,c and sys file"""
from recursion import floyd,c
import sys'''
             

TEST_CODE = '''
"""Run c and floyd functrion, and repeatedly measure execution time."""
no_path = sys.maxsize
g=[[0,7,no_path,8],
   [no_path,0,5,no_path],
   [no_path,no_path,0,2],
   [no_path,no_path,no_path,0]]
n=c(range(len(g[0])),len(g[0]))    
floyd(g,len(n)-1)'''
times_recursion = timeit.repeat(setup = SETUP_CODE,
                       stmt = TEST_CODE,
                     repeat = 3,
                     number = 5000)
print('Recursion Program Execution time: {}'.format(min(times_recursion)))  


# Performance test for imperative program

SETUP_CODE = '''    
"""Import floyd,sys and itertools file"""
from imper import floyd
import sys
import itertools'''

TEST_CODE = '''
"""Run floyd and repeatedly measure execution time."""
NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
floyd(graph)'''
times_imper = timeit.repeat(setup = SETUP_CODE,
                       stmt = TEST_CODE,
                     repeat = 3,
                     number = 5000)
print('Imperative Program Execution time: {}'.format(min(times_imper)))  