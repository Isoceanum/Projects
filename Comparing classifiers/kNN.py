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



# -------------------------------------k-nearest neighbors (kNN)---------------------------------------
def show(X, y, marker='.'):
    labels = set(y)
    cl = {lab : [] for lab in labels}
    # cl[lab] shall contain the datapoints labeled lab
    for (a, b) in zip(X, y):
        cl[b].append(a)
    for lab in labels:
        plt.plot([a[0] for a in cl[lab]], [a[1] for a in cl[lab]], 
                 marker, label="class {}".format(lab))
    plt.legend()
    plt.show()


#calculat the distance 
def dist_proc(a, b):
    # Euclidean distance in a procedural way
    s = 0
    for (x,y) in zip(a,b):
        s += (x - y) ** 2
    return s ** 0.5


def distance_L2(a, b):
    s = sum((x - y) ** 2 for (x,y) in zip(a,b))
    return s ** 0.5


def majority(a):
    counts = Counter(a)
    return counts.most_common()[0][0]

#show(X_train, t2_train)


class PyClassifier():

    def accuracy(self,X_test, y_test, **kwargs):

        predicted = [self.predict(a, **kwargs) for a in X_test]
        equal = len([(p, g) for (p,g) in zip(predicted, y_test) if p==g])
        return equal / len(y_test)

class PykNNClassifier(PyClassifier):
 
    
    def __init__(self, k=3, dist=distance_L2):
        self.k = k
        self.dist = dist
        
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, a):
        X = self.X_train
        y = self.y_train
        distances = [(self.dist(a, b), b, c) for (b, c) in zip(X, y)]
        distances.sort()
        predictors = [c for (_,_,c) in distances[0: k]]
        return majority(predictors)



#run test with different K and plot result 

x = range(1, 40, 1)
accuracies = []

for k in x:
    cls = PykNNClassifier(k=k)
    cls.fit(X_train, t2_train)
    accuracies.append(cls.accuracy(X_val, t2_val))
    print("K = " ,k,"accuracy : ", cls.accuracy(X_val, t2_val))
plt.plot(x, accuracies, label="Valset X_val, t2_val")
plt.xticks(x)
plt.legend()
plt.show()

