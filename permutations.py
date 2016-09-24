# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 15:54:28 2016

@author: Administrator
"""

def Mideng(li):
  if(type(li)!=list):
    return
  if(len(li)==1):
    return [li]
  result=[]
  for i in range(len(li)):
    bak=li[:]
    head=bak.pop(i) #head of the recursive-produced value
    for j in Mideng(bak):
      j.insert(0,head)
      result.append(j)
  return result
def MM(n):
  if(type(n)!=int or n<2):
    return
  return Mideng(list(range(1,n)))

def permutations(string):
    if len(string)==1:
        return [string]
    result=[]
    for i in range(len(string)):
        arr=list(string)
        head=arr.pop(i)
        for j in permutations(''.join(arr)):
            sun=list(j)
            sun.insert(0,head)         
            result.append(''.join(sun))
    return sorted(set(result))
    
if __name__=='__main__':
    permutations('aabb') #['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    permutations('abcd')
    #['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc',
    #'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad','cbda',
    #'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
     
        
        
        
        
        
        
        
        
        