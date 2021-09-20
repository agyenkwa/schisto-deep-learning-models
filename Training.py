# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:03:25 2021

@author: K. Agyenkwa-Mawuli & Joseph Adams
"""


from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from tkinter import filedialog

import time
import tkinter as Tk


import sklearn as sk
import matplotlib.pyplot as plt
from tkinter import filedialog

from tensorflow.keras.callbacks import EarlyStopping
from sklearn.utils import class_weight
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import matthews_corrcoef
from matplotlib import pyplot


#loading data set
print('\n\n SELECT TRAINING DATASET')
print(time.strftime("%b %d %Y %H:%M", time.localtime()))
time.sleep(2)

m=filedialog.askopenfilename(initialdir = '/Desktop',      
 title = '                         SELECT TRAINING DATASET     ')
Train = loadtxt(m,delimiter=',')

n=filedialog.askopenfilename(initialdir = '/Desktop',      
 title = '                         SELECT VALIDATION DATASET   ')
val = loadtxt(n,delimiter=',')

#Splitting datasets into input and output variables
x=Train[:,0:778]
y=Train[:,777]
x_val=val[:,0:778]
y_val=val[:,777]


#Defining the model
def create_model(x,y):
    predict1 = Sequential()
    predict1.add(Dense(520, input_dim=778,activation='relu'))
    predict1.add(Dense(520, activation='relu'))
    predict1.add(Dense(1, activation='sigmoid'))
    predict1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    weights = {0:1, 5:1}
    custom_early_stopping=EarlyStopping(monitor='accuracy',patience=8,min_delta=0.001,mode='max',restore_best_weights=True)
    predict1.fit(x,y,validation_data=(x_val,y_val),class_weight=weights,epochs=150,batch_size=100,callbacks=[custom_early_stopping])
    return predict1


#Testing
m=filedialog.askopenfilename(initialdir = '/Desktop',      
 title = '                         SELECT TEST DATASET     ')
TEST = loadtxt(m,delimiter=',')
print('    RUNNING PROGRAM\n\n')
time.sleep(3)
m = TEST[:,0:778]
n= TEST[:,777]

TP,FP,TN,FN=0,0,0,0
a,ina=0,0
ac = 0
inac = 0

#Fit model
model = create_model(m,n)

predictions = model.predict_classes(m)
print('\n\nSTARTING PREDICTIONS\n\n')
time.sleep(3)

for i in range(len(m)):
	
	if int(n[i])==1:
		a+=1
		if int(predictions[i])==1:
			TP+=1
		if int(predictions[i])==0:
			FN+=1
	
	if int(y[i])==0:
		ina+=1
		if int(predictions[i])==1:
			FP+=1
		if int(predictions[i])==0:
			TN+=1

SEN = (TP/(TP+FN))*100
SPE = (TN/(TN+FP))*100
ACTIVES = a
INACTIVES = ina 

print('ACTIVES =',a,' ','INACTIVES =',ina)
print('\n')

print('TOTAL SAMPLE =',len(m), 'TP =',TP,'FP =',FP,'TN =',TN,'FN =',FN)

print('SENSITIVITY:',int(SEN),' ', 'SPECIFICITY:',int(SPE))

