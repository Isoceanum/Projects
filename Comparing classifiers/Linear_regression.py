
import numpy as np
import sklearn.datasets as datasets
from matplotlib import pyplot as plt
import random
from collections import Counter
from sklearn.datasets import make_blobs

X, t = make_blobs(n_samples=[400,800,400], centers=[[0,0],[1,2],[2,3]],n_features=2, random_state=2019)

indices = np.arange(X.shape[0])
random.seed(2020)
random.shuffle(indices)
indices[:10]

X_train = X[indices[:800],:]
X_val = X[indices[800:1200],:]
X_test = X[indices[1200:],:]
t_train = t[indices[:800]]
t_val = t[indices[800:1200]]
t_test = t[indices[1200:]]

t2_train = t_train == 1
t2_train = t2_train.astype('int')
t2_val = (t_val == 1).astype('int')
t2_test = (t_test == 1).astype('int')


# -------------------------------------Linear regression-----------------------------------------

def add_bias(X):
    sh = X.shape
    if len(sh) == 1:
        return np.concatenate([np.array([1]), X])
    else:
        m = sh[0]
        bias = np.ones((m,1)) 
        return np.concatenate([bias, X], axis  = 1) 

class NumpyClassifier():  
    def accuracy(self,X_test, y_test, **kwargs):
        pred = self.predict(X_test, **kwargs)
        if len(pred.shape) > 1:
            pred = pred[:,0]
        return sum(pred==y_test)/len(pred)

class NumpyLinRegClass(NumpyClassifier):

    def fit(self, X_train, t_train, eta = 0.25, epochs=1000,diff = 0.0001):
   
        
        (k, m) = X_train.shape
        X_train = add_bias(X_train)
        
        self.weights = weights = np.zeros(m+1)

        for e in range(0,epochs,7):
         
            before = self.accuracy(X_val, t2_val)
            weights -= eta / k *  X_train.T @ (X_train @ weights - t_train)
            if (abs(self.accuracy(X_val, t2_val) - before) < diff ):
                break
      
    
    def predict(self, x, threshold=0.5):
        z = add_bias(x)
        score = z @ self.weights
        return score>threshold


lin_cl = NumpyLinRegClass()
lin_cl.fit(X_train, t2_train)
print("LinReg accuracy :  ",lin_cl.accuracy(X_val, t2_val))


