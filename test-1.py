import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#training data
shirt    = pd.read_csv('Shirt.csv',header=None,sep='\t')
phant    = pd.read_csv('phant.csv',header=None,sep='\t')
belt     = pd.read_csv('belt.csv',header=None,sep='\t')
wallet   = pd.read_csv('wallet.csv',header=None,sep='\t')
watches  = pd.read_csv('watches.csv',header=None,sep='\t')

shirt    = shirt.iloc[:,:].values
phant    = phant.iloc[:,:].values
belt     = belt.iloc[:,:].values
wallet   = wallet.iloc[:,:].values
watches  = watches.iloc[:,:].values

for i in range(len(shirt)):
    print(shirt[i][0])
    print(shirt[i][1])
else:
    print('finished')