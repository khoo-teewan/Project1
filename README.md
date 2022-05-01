# Project1
Title: FLOYD ALGORITHM RECURSION PROGRAM - PERFORMANCE AND UNIT TEST
Date: May 1st, 2022
Author: KHOO TEE WAN
Scope:  Locate shortest path, perform performance and unit test.
History: Initial Development
REV. : A00

A.  Distance matrix: 
    g is a distance matrix with distance between a node and the rest of the nodes.
    No_Path in the matrix indicates that there is no direct path.

          Graph or g = [[0, 7, NO_PATH, 8], 
                        [NO_PATH, 0, 5, NO_PATH], 
                        [NO_PATH, NO_PATH, 0, 2], 
                        [NO_PATH, NO_PATH, NO_PATH, 0]]

B.  Recursion program setup:


    B-1:  Library import: sys.
    B-2:  Function definition:
          c function:  Check for all possibilities combination of paths.          
                       Required argument:
                          lst = length range of index-0 of the matrix, g.
                            n = length of index-0 of the matrix, g.
                       Return parameters:
                           (x,)+t = return n-numbers of possible pairs of nodes.
  
         floyd function: use the value return from c-function, n, to verify the shortest path.            
                        Required argument:
                           d = distance path of each nodes.
                           k = # of combinations for path findings.
                        Return parameters:
                           d= shortest path.
                 
C. Performance test setup:
   
   (Recursion program performance test)
   
   
     C-1:   Function definition:  import timeit library to use timeit.repeat() method.  
                                  Setup code: import floyd,c from recursion.py;
                                              import sys from standard library.
                                  Test code: run c and floyd functrion, and repeatedly measure execution time.
                                  Repeat: 3
                                  Number: 5000
   
   (Imperative program performance test)
   
     C-2:  Function definition:  import timeit library to use timeit.repeat() method.   
                                 Setup code: import floyd from imper.py;
                                             import sys and itertools file from standard library.
                                 Test code: run floyd and repeatedly measure execution time.
                                 Repeat: 3
                                 Number: 5000
  
D. Unit test setup: 
   
   
   
   
   
   
   D-1:  Library setup: import sys
   D-2:  Test setup:
                  
         1.  from recursion import c,floyd.
         2.  Test case 1 (test_on_c) --
             input (test_on_c): 
                  c([0,1,2],2)
             Test case expected output (test_on_c): 
                  [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
         3.  Test case 2 (test_on_floyd) --  
             input (test_on_floyd): 
                 [0,5,sys.maxsize,10],
                 [sys.maxsize,0,3,sys.maxsize],
                 [sys.maxsize,sys.maxsize,0,1],
                 [sys.maxsize,sys.maxsize,sys.maxsize,0]],len(n)-1) 
             Test case expected output (test_on_floyd): 
                 [[0,5,8,9],
                  [sys.maxsize,0,3,4],
                  [sys.maxsize,sys.maxsize,0,1],
                  [sys.maxsize,sys.maxsize,sys.maxsize,0]]
             
             
