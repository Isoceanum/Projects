import numpy as np
import sklearn.datasets as datasets
from matplotlib import pyplot as plt
import random
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

#visualize dataset

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', c=t_train,s=25, edgecolor='k')
plt.subplot(222)
plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', c=t2_train,s=25, edgecolor='k') 
plt.show()



