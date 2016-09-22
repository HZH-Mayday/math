# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:07:10 2016

@author: Administrator
"""
import numpy as np
from numpy.linalg import solve

def chance_1(arr,value):
    narr=np.array(arr)
    nvalue=np.array(value)
    Lx=list(solve(narr,nvalue))
    result={'x_'+str(i):Lx[i-1] for i in range(1,len(value)+1)}
    return result

if __name__=="__main__":
   print chance_1([[10,-7,0],
                  [-3,2,6],
                  [5,-1,5]],[7,4,6])
