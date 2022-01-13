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


# -------------------------------------Simple perceptron-----------------------------------------


class PyClassifier():

    def accuracy(self,X_test, y_test, **kwargs):

        predicted = [self.predict(a, **kwargs) for a in X_test]
        equal = len([(p, g) for (p,g) in zip(predicted, y_test) if p==g])
        return equal / len(y_test)

class PyPerClassifier(PyClassifier):
   
    
    def fit(self, X_train, y_train, eta=1, epochs=1):

        X_train = [[1]+list(x) for x in X_train] # Put bias in position 0 
        self.dim = dim = len(X_train[0])
        self.weights = weights = [0 for _ in range(dim)]
        # Initialize all weights to 0.

        for e in range(epochs):
            for x, t in zip(X_train, y_train):
                y = int(self.forward(x)>0)
                for i in range(dim):
                    weights[i] -= eta * (y - t) * x[i]
        
    def forward(self, x):

        score = sum([self.weights[i]*x[i] for i in range(self.dim)])
        return score       
    
    def predict(self, x):

        x = [1] + list(x)
        score = self.forward(x)
        return int(score > 0)


#run test on Simple perceptron with diffrent epochs

x = range(1,50)
accuracies = []
for i in x:
    cl = PyPerClassifier()
    cl.fit(X_train, t2_train, eta= 0.05, epochs = i)

    print("epochs",i,"accuracy",cl.accuracy(X_val, t2_val) )
    accuracies.append(cl.accuracy(X_val, t2_val))
 
plt.plot(x, accuracies, label="Valset X_val, t2_val")
plt.show()

print("best-----------------------")
print(max(accuracies))

