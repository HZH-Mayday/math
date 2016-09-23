# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 22:54:17 2016

@author: Administrator
"""

#Way 1
def fibonacii(x):
    if x in [0,1]:
       return x   
    return fibonacii(x-1)+fibonacii(x-2)
    

#Way 2
def dic(func):
    ndic={}
    def myfunc(x):
        v=ndic.get(x)
        if v is None:
            v=ndic[x]=func(x)
            return v
    return myfunc
@dic
def fibonacii_long(n):
    if n in [0,1]:
       return n   
    return fibonacii(n-1)+fibonacii(n-2)


# the best way
def fibonacii_nice(x,a=1,b=1):
    if x == 3:
        return  a+b
    return fibonacii_nice(x-1,b,b+a)


    
    
    
    
    
    
    