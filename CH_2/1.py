import os
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import pcn
pima = loadtxt('../dataset/pima-indians-diabetes.data', delimiter=',')

indices0 = where(pima[:, 8] == 0)
indices1 = where(pima[:, 8] == 1)

plt.plot(pima[indices0, 0], pima[indices0, 1], 'go')
plt.plot(pima[indices1, 0], pima[indices1, 1], 'rx')


print("Output original data: ")
p = pcn.pcn(pima[:, :8], pima[:, 8:9])
p.pcntrain(pima[:, :8], pima[:, 8:9], 0.25, 100)
p.confmat(pima[:, :8], pima[8:9])

pima[where(pima[:,0]>8),0] = 8


pima[where(pima[:,7]<=30),7] = 1
pima[where((pima[:,7]>30) & (pima[:,7]<=40)),7] = 2
pima[where((pima[:,7]>40) & (pima[:,7]<=50)),7] = 3
pima[where((pima[:,7]>50) & (pima[:,7]<=60)),7] = 4
pima[where(pima[:,7]>60)] = 5

pima[:,:8] = pima[:,:8]-pima[:,:8].mean(axis=0)
pima[:,:8] = pima[:,:8]/pima[:,:8].var(axis=0)

print (pima.mean(axis=0))
print(pima.var(axis=0))
print(pima.max(axis=0))
print(pima.min(axis=0))

trainin = pima[::2,:8] # For even
testin = pima[1::2,:8] # For odd
traintgt = pima[::2,8:9]
testtgt = pima[1::2,8:9]

# Perceptron training on the preprocessed dataset
print("Output after preprocessing of data")
p1 = pcn.pcn(trainin,traintgt)
p1.pcntrain(trainin,traintgt,0.25,100)
p1.confmat(testin,testtgt)

