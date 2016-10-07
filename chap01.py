# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:56:34 2016

@author: Administrator
"""
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
'''
3.4	26.2
1.8	17.8
4.6	31.3
2.3	23.1
3.1	27.5
5.5	36.0
0.7	14.1
3.0	22.3
2.6	19.6
4.3	31.3
2.1	24.0
1.1	17.3
6.1	43.2
4.8	36.4
3.8	26.1
'''

data=sp.genfromtxt('C:/Users/Administrator/Desktop/hire.txt',delimiter='\t')
x=data[:,0]
y=data[:,1]
'''散点图'''
plt.scatter(x,y)
plt.xlabel('Distance')
plt.ylabel('Lost of hire')
plt.autoscale(tight=True)
plt.grid()
'''拟合线，一次'''
fp1=sp.polyfit(x,y,1) #最高次数为一次
f1=sp.poly1d(fp1)     #用fp1的参数创建一个模型函数
fx=np.linspace(0,np.max(x),1000)
plt.plot(fx,f1(fx),linewidth=4)
plt.legend(['d=%d'% f1.order],loc='upper left')
'''预测在Lost=100，Distance?'''
result=fsolve(f1,100)[0]     #fsolve() 输入参数的值即可求出函数的根











