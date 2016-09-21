# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:24:56 2016

@author: Administrator
"""
import numpy as np

def chance_0(arr):
    arr[0][0]=float(arr[0][0])      #把数据转变成浮点数形式
    data=np.array(arr)              #数组转换为narray
    #判断行列式有无错误
    Fcol_T=list(set(list(data.T)[0]))
    if len(Fcol_T)==1 and Fcol_T[0]==0 :
        return False
    row,col=np.shape(data)           #data的形状
      
    '''每一列取最大主元，并与第一行交换'''
    for coltime in range(col-2):
        #创造最大主元
        s_b={data[j,coltime]:i+coltime for i,j in enumerate(range(coltime,row))}
        maxkey=max([key for key in s_b])
        item=s_b[maxkey]            #最大主元的行索引
        data1=data.copy()
        data[coltime]=data1[item];data[item]=data1[coltime]
        
        #相应的coltime 消掉后变零  
        for i in range(coltime,len(data)-1):
            n=data[i+1,coltime]/float(data[coltime,coltime])
            data[i+1]=data[i+1]-data[coltime]*n
            data[i+1,coltime]=0  
    print '线性方程组（换主元）经过变换的最后结果:'
    print data

    '''求解x1,x2...'''
    data=data.astype(np.float32)    #把np.folat64的精度变成单精度
    dicx={'x_'+str(i+1):0 for i in range(row)} #创建一个x：值的字典    
    dicx['x_'+str(row)]=data[row-1,col-1]/data[row-1,col-2]  #确定x_row的值
    #求出剩下的x_...
    for n in range(row-1,0,-1):
        son=data[n-1,n-1]
        mother=data[n-1,col-1]-sum([data[n-1,i]*dicx['x_'+str(i+1)] 
                                    for i in range(row-1,n-1,-1)])
        dicx['x_'+str(n)]=mother/son
    return dicx                               
                
            
if __name__=='__main__':
   print chance_0([[10,-7,0,7],
                  [-3,2,6,4],
                  [5,-1,5,6]])
 
                   
                   
                   
                   
                   
                   