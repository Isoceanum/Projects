
import numpy as np
import sklearn.datasets as datasets
from matplotlib import pyplot as plt
import sklearn
import random
import math
from collections import Counter
import time
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


# ------------------------------------Logistic regression-----------------------------------------
def sigmoid(x):
    return 1/(1 + np.exp(-x))


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



class NumpyLogReg(NumpyClassifier):
    def fit(self, X_train, t_train, eta = 0.1, epochs=101):
        (k, m) = X_train.shape
        X_train = add_bias(X_train)
        self.weights = weights = np.zeros(m+1)
        
        for e in range(epochs):
            weights -= eta / k *  X_train.T @ (self.forward(X_train) - t_train)      
    
    def forward(self, X):
        return sigmoid(X @ self.weights)
    
    def score(self, x):
        z = add_bias(x)
        score = self.forward(z)
        return score
    
    def predict(self, x, threshold=0.5):
        z = add_bias(x)
        score = self.forward(z)
        return (score>threshold).astype('int')


#run test on Logistic regression with different  epochs and eta and plot results

lr_cl = NumpyLogReg()
lr_cl.fit(X_train, t2_train)
print("LogReg  ",lr_cl.accuracy(X_val, t2_val))


x = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
accuracies = []


print("------------------------------------------")
for eta in x:
    lr_cl = NumpyLogReg()
    lr_cl.fit(X_train, t2_train, epochs=1000, eta = eta)
    accuracies.append(lr_cl.accuracy(X_val, t2_val))
    print("Learning rate: {:7}  Epochs: {:4}  Accuracy: {}".format(
        eta, 1000, lr_cl.accuracy(X_val, t2_val)))
plt.plot(x, accuracies, label="Valset X_val, t2_val")

plt.show()

x = range (1,1500,2 )
accuracies = []

print("------------------------------------------")
for e in x:
    lr_cl = NumpyLogReg()
    lr_cl.fit(X_train, t2_train, epochs=e, eta=0.01)
    accuracies.append(lr_cl.accuracy(X_val, t2_val))
    print("Learning rate: {:7}  Epochs: {:8}  Accuracy: {}".format(
        0.01, e, lr_cl.accuracy(X_val, t2_val)))
plt.plot(x, accuracies, label="Valset X_val, t2_val")

plt.show()

