import numpy as np
from sklearn.linear_model.logistic import LogisticRegression

class logistic(object):
    
    #初始化训练集，步长，特征数    
    def __init__(self,x_train,y_train,alpha):
        self.x_train = np.mat(x_train)           #train_x,x=[[],[],.....]
        self.y_train = np.mat(y_train)           #train_y,y=[.....]
        self.alpha = alpha                       #迭代步长
        self.feature_n = len(x_train[0])      #特征数量
        self.data_n = len(x_train)            #训练集数量
        self.thea =  np.ones((self.feature_n,1))   
    
    def htheat(self,x_train_num):
        return np.exp(x_train_num)/(1+np.exp(x_train_num))
        
    
    def interate(self):
        for k in range(500): 
            xx = self.x_train * (self.thea)
            error = self.y_train.T - logistic.htheat(self,xx)
            self.thea = self.thea + self.alpha * self.x_train.T * error                
        return self.thea
        

if __name__ == "__main__":
    x_train = np.array([[1,2,3,4],
                       [2,3,4,5],
                       [3,4,5,6]])    
    y_train = np.array([1,0,1])
   
    aaa = logistic(x_train,y_train,0.001)
    print aaa.interate()  
    # [[ 0.47142438]
       [ 0.24186416]
       [ 0.01230394]
       [-0.21725628]]
   
    #验证，与skleern的结果相比较
    a = LogisticRegression()
    a.fit(x_train,y_train)
    print a.coef_ 
    #[[-0.00690527  0.02088796  0.04868119  0.07647442]]
