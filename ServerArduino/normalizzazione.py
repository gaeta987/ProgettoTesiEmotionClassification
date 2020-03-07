import pandas
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def calcola(X,i,j):
    temp=[]
    for i in range(i,j):
        temp.append(X[i])
    scaler = MinMaxScaler (feature_range = (-1,1))
    dummy_x = scaler.fit_transform(temp)
    
    return dummy_x

def normalize(X):
    init = 0
    end = 80

    g = calcola(X,init,end)

    init = init + 80
    end = end + 80

    d = (len(X) - 80) / 80
    
    s = int(d)

    for d in range(s):
        r = calcola(X,init,end)
        g = np.concatenate((g,r),axis = 0)
        init = init + 80
        end = end + 80

    return g




