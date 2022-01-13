Comparing classifiers


Datasets



Linear regression

LinReg 0.56
The reported accuracy of linear regression is 0.56 if I remove
the if check in the epochs for loop that takes diff into
account, I get a better accuracy of 0.6075. I believe this is
due to the flat array where the prediction does not improve
between epochs 40 and 50 in fig2. I will be using the best
accuracy in reporting because I believe the error is a bug on
my part and not a function of the Linear regression.
The regression can be seen in action in fig3 where the green
line is the initial starting plain and the function is trying to fit
it best to the data. I have tried different epochs and eta with
little success. Fig4 is the final and best result plotted



Logistic regression
LogReg 0.6375
I ran multiple for loops testing both the learning rate and epochs. For eta the best setting seems to
be 0.01. values over this end up decreasing the accuracy as we can see in fig5
Learning rate: 0.01 Accuracy: 0.6375



Figure 5
On the epochs it seems the best setting is around 651 with a record accuracy of 0.6475
demonstrated by the high points in fig6
Epochs: 651 Accuracy: 0.6475


k-nearest neighbors (kNN)
kNN = 0.7675
running a for loop with different K. K being the number of neighbors to include in the distance
calculation. The best k seems to be 14. The following is the for loop plotted 


Simple perceptron
Running the simple perceptron on different epochs I found that the best accuracy occurred with 17
epochs. Plotting all accuracy gives the following graph. I am not sure why the accuracy jumps so
much. 


Summary
Model accuracy Epochs eta
LinReg 0.56 1000 0.25
LogReg 0.6375 651 0.01
kNN 0.7675 na na
perceptron 0.6625 17 0.05
From the results we can observe that the Linier classifier is struggling the most because the data is
not linearly separable. From fig4 we can see that the line it drew manages to separate the lower
cluster of purple from the central yellow cluster. But a liner classifier can do little to classify the
purple cluster over the yellow one, on the account of it being a straight line. The Log model can do a
better job at conforming to the clusters. Hence the better accuracy.
What surprised me is the KNN classifier that was better than all the other by a substantial margin. It
does make sense because it looks at the closest 14 neighbors and it will therefore have a higher
success rate when classifying objects in the center of the yellow and two purple blobs.
Lastly the simple perceptron. I did not expect it to outperform KNN. But I expected it to be much
better vs the two Reg models then it turned out to be. Maybe this highlights the important of
multiple hidden layers in a neural network as the simple perceptron is not able to store and modify
enough weights and biases to capture the nuances of the dataset 