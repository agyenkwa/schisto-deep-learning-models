# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:03:25 2021

@author: K. Agyenkwa-Mawuli & Joseph Adams
"""

import tensorflow as tf
import keras 
from numpy import loadtxt
#from keras.models import Sequential
from keras.layers import Dense
from tkinter import filedialog
from keras.models import load_model

import time
import tkinter as Tk


import sklearn as sk
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc,roc_auc_score,cohen_kappa_score,matthews_corrcoef
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.utils import class_weight
from matplotlib import pyplot

m=filedialog.askopenfilename(initialdir = '/Desktop',      
 title = '                         SELECT TEST DATASET     ')
TEST = loadtxt(m,delimiter=',')
print('    RUNNING PROGRAM\n\n')
time.sleep(3)
z = TEST[:,0:778]
y= TEST[:,778]


#Load model
reconstructed_model = tf.keras.models.load_model('DNN_27')

#Summarize model.
reconstructed_model.summary()

#Evaluate the model
score = reconstructed_model.evaluate(z,y, verbose=0)
print("%s: %.2f%%" % (reconstructed_model.metrics_names[1], score[1]*100))

#Test model
TP,FP,TN,FN=0,0,0,0
a,ina=0,0
ac = 0
inac = 0

predictions = reconstructed_model.predict_classes(z)
print('\n\nSTARTING PREDICTIONS\n\n')
time.sleep(3)

for i in range(len(z)):
	
	if int(y[i])==1:
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

ACC = ((TP+TN)/len(z))*100
SEN = (TP/(TP+FN))*100
SPE = (TN/(TN+FP))*100
ACTIVES = a
INACTIVES = ina 

BCR = (SEN+SPE)/2
F1_score = (2*(TP)/((2*TP)+FP+FN))
Recall = TP/(TP+FN)
Precision = TP/(TP+FP)

MCC = matthews_corrcoef(y,predictions)
ROC_AUC = roc_auc_score(y,predictions)
Kappa = cohen_kappa_score(y,predictions)

print('ACTIVES =',a,' ','INACTIVES =',ina)
print('\n')

print('TOTAL SAMPLES =',len(z), 'TP =',TP,'FP =',FP,'TN =',TN,'FN =',FN)
print('\n')

print('ACCURACY:',int(ACC),' ', 'SENSITIVITY:',int(SEN),' ', 'SPECIFICITY:',int(SPE))
print('\n')

print('F1 SCORE: %.3f' % F1_score, 'RECALL: %.3f' % Recall, 'PRECISION: %.3f' %Precision)
print('\n')

print('BALANCED ACCURACY:',int(BCR), 'MCC: %.3f' % MCC, 'COHEN KAPPA: %.3f' % Kappa)
print('\n')

print('ROC AUC SCORE: %.3f' % ROC_AUC)
print('\n')