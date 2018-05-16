# -*- coding: utf-8 -*-
"""
Created on Fri May 04 23:51:08 2018

@author: Administrator
"""


import numpy as np

class Random_gradient_descent(object):
    
    def __init__(self,data,space=0.001,epsilon = 1e-10):
        '''data为输入的数据,输入的为列表'''
        self.epsilon = epsilon              #收敛的参数误差
        self.space = space                  #随机梯度的步长      
        self.data = np.array(data)
        self.data_x = self.data[:,:-1]      #训练集的X
        self.data_y = self.data[:,-1]       #训练集的Y
        self.theta = np.array([1.0 for i in range(self.data_x.shape[1])])  #初始化theta都为0
        
    def calculate(self,one_train_example_x,one_train_example_y):
        '''one_train_example_x,one_train_example_y
        分别是一组数据的x和y,类型是np.array和float   
        函数目标是 只利用一个数据更新一轮的theta
        '''         
        for i in range(len(self.theta)):            #用其中一个训练集，更新所有的theta
            j_theta_func = (np.sum(self.theta*one_train_example_x)-one_train_example_y)**2
            loss_func = self.space*j_theta_func*one_train_example_x[i]
            self.theta[i] -= loss_func         
        
    def rgd_main(self):
        ''' 
        遍历所有的数据集，得到最后的theta   
        '''  
        for i in range(self.data_x.shape[0]):
            last_theta = self.theta.copy()          #复制上一轮更新的参数
            self.calculate(self.data_x[i],self.data_y[i])   #更新参数          
            #检验是否收敛
            loss_value = np.power(last_theta-self.theta,2)
            if loss_value < self.epsilon:
                print "theta已经收敛"
                break
            
            
if __name__ == "__main__":
    
    data = [[-1,-2],[0,-1],[1,0],[2,1],[-0.5,-1.2],[0.5,-0.8],[1.5,0.9],[3,1.8]]
    r = Random_gradient_descent(data)
    r.rgd_main()
