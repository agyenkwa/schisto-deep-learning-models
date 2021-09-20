# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:14:10 2021

@author: K. Agyenkwa-Mawuli & Joseph Adams
"""

#Import required libraries and classes
import numpy as np
import random
from tkinter import filedialog


w=filedialog.askopenfilename()#read file
data=np.loadtxt(w,delimiter=',')
np.take(data,np.random.permutation(data.shape[0]),axis=0,out=data)
g=data.shape[0]
r=int(0.7*g)
test=data[r:g,:]
train=data[0:r,:]
k=int(0.7*r)
val=train[k:r,:]
Train=train[0:k,:]
np.savetxt('Test.csv',test,delimiter=',')
np.savetxt('Train.csv',Train,delimiter=',')
np.savetxt('Validate.csv',val,delimiter=',')