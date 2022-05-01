# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:44:59 2021

A simple implementation of Floyd's algorithm: Recursion Program
1.  Write Floyd’s algorithm to use recursion.
2.  Write performance tests

@author: KHOO TEE WAN
"""

import sys

no_path=sys.maxsize

"""
  g is a distance matrix with distance between a node and the rest of
  the nodes.
"""

g=[[0,7,no_path,8],
   [no_path,0,5,no_path],
   [no_path,no_path,0,2],
   [no_path,no_path,no_path,0]]


def c(lst,n):
    """
       Receive the call function with argument
       
       Required argument:
       lst = length range of index-0 of the matrix, g.
       n = length of index-0 of the matrix, g.
       
       Return parameters:
       (x,)+t = return n-numbers of possible pairs of nodes
    """        
    if n==1:
       return [(x,) for x in lst]
    return [(x,)+t for t in c(lst,n-1) for x in lst]

def floyd(d,k):
    """
       Receive the call function with argument
       
       Required argument:
       d = distance path of each nodes
       k = # of combinations for path findings
        
      Return parameters
      d= shortest path
    """
    if k==0:
        d[0][0]=0
    else:
        d[n[k][1]][n[k][0]]=min(d[n[k][1]][n[k][0]],\
                                d[n[k][1]][n[k][2]]+d[n[k][2]][n[k][0]])
        
        floyd(d,k-1)
        
        return d


n=c(range(len(g[0])),len(g[0]))    
floyd(g,len(n)-1)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    