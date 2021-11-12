


# -*- coding: utf-8 -*-
"""
@author: K. Agyenkwa-Mawuli
"""


#RANDOM FOREST MODEL TRAINING

from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import preprocessing
from sklearn import utils
import joblib
from imblearn.over_sampling import SMOTE

from tkinter import filedialog
import time
import tkinter as Tk
from numpy import loadtxt


#Loading data set
print('\n\n SELECT TRAINING DATASET')
print(time.strftime("%b %d %Y %H:%M", time.localtime()))
time.sleep(2)

m=filedialog.askopenfilename(initialdir = '/Desktop',      
 title = '                         SELECT TRAINING DATASET     ')
Train = loadtxt(m,delimiter=',')

n=filedialog.askopenfilename(initialdir = '/Desktop',      
 title = '                         SELECT VALIDATION DATASET   ')
val = loadtxt(n,delimiter=',')

print('loaded')



#Split into features and labels
x_tr=Train[:,0:778]
y_tr=Train[:,778]
x_val=val[:,0:778]
y_val=val[:,778]
print('data split')

oversample = SMOTE()
x_tr,y_tr = oversample.fit_resample(x_tr,y_tr)
x_val,y_val = oversample.fit_resample(x_val,y_val)
print('transformed')

#Define the model
model=RandomForestClassifier(bootstrap=True,class_weight={0:1,1:2.5},max_depth=6,verbose=1) #
model.fit(x_tr,y_tr)

print('data fit')

#Evaluate model
cv = RepeatedStratifiedKFold(n_splits=10,n_repeats=3, random_state=36)
n_scores = cross_val_score(model, x_val,y_val, scoring='accuracy', cv=cv, n_jobs=1, error_score='raise')

#Report Performance
print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))
#yhat = model.predict(x_val)

print('model saving')
#Save model
joblib.dump(model,"./random_forest1.joblib")

