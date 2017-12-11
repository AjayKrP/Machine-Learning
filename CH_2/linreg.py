

from numpy import *

def linreg(inputs,targets):
    #print(-ones((shape(inputs)[0],1)))
    inputs = concatenate((inputs,-ones((shape(inputs)[0],1))),axis=1) # add input for bias node
    print(inputs)
    beta = dot(dot(linalg.inv(dot(transpose(inputs),inputs)),transpose(inputs)),targets)

    outputs = dot(inputs,beta)
    #print shape(beta)
    #print outputs
    return beta
