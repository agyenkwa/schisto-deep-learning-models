# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:20:26 2021

@author: K. Agyenkwa-Mawuli & Joseph Adams
"""
import pandas as pd
import os
import glob
from tkinter import filedialog

#Select files containing datasets
t=filedialog.askdirectory()
os.chdir(t)



#Concatenate files into one .csv file
ext = 'csv'
al_fs = [i for i in glob.glob('*.{}'.format(ext))]
cm_csv=pd.concat([pd.read_csv(f) for f in al_fs])
cm_csv.to_csv("Combined_descriptor.csv",index=False)
