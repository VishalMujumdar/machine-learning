# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:23:23 2020

@author: vismujum
"""

import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

# Read CSV File to capture Marketing Details
df = pd.read_csv('C:\codeRepository\machine-learning\BudgetSpend_Details.csv')
    
# Replace all rows that has missing values
df.dropna(inplace = True)
    
# Information on attributes
df.info()

# Number of Data Entries - Marketing details
df.shape
df.head()

df.rename(columns={'MC Billings':'mc_billings','Billings Target':'billings_target' ,'Pipeline':'pipeline','Spend':'spend','Budget':'budget'},inplace=True)
    
# Remove $ from Attributes to make them Numerics
df['mc_billings']=df['mc_billings'].str[1:]
df['billings_target']=df['billings_target'].str[1:]
df['pipeline']=df['pipeline'].str[1:]
df['spend']=df['spend'].str[1:]
df['budget']=df['budget'].str[1:]
    
#Define object as String and to remove leading / trailing spaces
df['mc_billings']=df['mc_billings'].astype(str)
df['mc_billings']=df['mc_billings'].str.replace(',','')
df['mc_billings']=df['mc_billings'].str.strip()
df['mc_billings']=df['mc_billings'].astype(float)
    
df['billings_target']=df['billings_target'].astype(str) 
df['billings_target']=df['billings_target'].str.replace(',','')
df['billings_target']=df['billings_target'].str.strip()
df['billings_target']=df['billings_target'].astype(float)
    
df['pipeline']=df['pipeline'].astype(str) 
df['pipeline']=df['pipeline'].str.replace(',','').str.strip()
df['pipeline']=df['pipeline'].str.strip()
df['pipeline']=df['pipeline'].astype(float)
    
df['spend']=df['spend'].astype(str)
df['spend']=df['spend'].str.replace(',','').str.strip()
df['spend']=df['spend'].str.strip()
df['spend']=df['spend'].astype(float)
    
df['budget']=df['budget'].astype(str)
df['budget']=df['budget'].str.replace(',','').str.strip()
df['budget']=df['budget'].str.strip()
df['budget']=df['budget'].astype(float)

# pipeline ,  mc_billings , billings_target , spend , budget

# Use Case 001 - Predictions for Subscription Targets based on Pipeline Cost and Subscription Cost
x_uc001 = df.drop(['billings_target','spend','budget'], axis=1)
y_uc001 = df['billings_target']
xtrain_uc001,xtest_uc001,ytrain_uc001,ytest_uc001 = train_test_split(x_uc001,y_uc001,test_size=0.25 , random_state=5 )

print('X-Shape Size: ',x_uc001.shape)
print('Y-Shape Size :',y_uc001.shape)
print('X-Train Size: ',xtrain_uc001.shape)
print('Y-Train Size :',ytrain_uc001.shape)
print('X-Test Size: ',xtest_uc001.shape)
print('Y-Test Size :',ytest_uc001.shape)

model_uc001 = LinearRegression()
model_uc001.fit(xtrain_uc001 , ytrain_uc001)

# Validate Use Case 001
test_uc001 = [[464,1449]]
model_uc001.predict(test_uc001)
ypred_uc001 = model_uc001.predict(xtest_uc001)
from sklearn import metrics
metrics.r2_score(ytest_uc001,ypred_uc001)   # This Model has performance of 99.99%


# Use Case 002 - Predictions for Total Expenditure based on Pipeline Cost and Budget Allocated
x_uc002 = df.drop(['spend','mc_billings','billings_target'], axis=1)
y_uc002 = df['spend']
xtrain_uc002,xtest_uc002,ytrain_uc002,ytest_uc002 = train_test_split(x_uc002,y_uc002,test_size=0.25 , random_state=5 )

print('X-Shape Size: ',x_uc002.shape)
print('Y-Shape Size :',y_uc002.shape)
print('X-Train Size: ',xtrain_uc002.shape)
print('Y-Train Size :',ytrain_uc002.shape)
print('X-Test Size: ',xtest_uc002.shape)
print('Y-Test Size :',ytest_uc002.shape)

model_uc002 = LinearRegression()
model_uc002.fit(xtrain_uc002 , ytrain_uc002)

# Validate Use Case 002
test_uc002 = [[924,11]]
model_uc002.predict(test_uc002)
ypred_uc002 = model_uc002.predict(xtest_uc002)
from sklearn import metrics
metrics.r2_score(ytest_uc002,ypred_uc002)   # This Model has performance of 99.99%


# Use Case 003 - Predictions for Budget Allocation based on Pipeline Cost and Expenditure
x_uc003 = df.drop(['mc_billings','billings_target','budget'], axis=1)
y_uc003 = df['budget']
xtrain_uc003,xtest_uc003,ytrain_uc003,ytest_uc003 = train_test_split(x_uc003,y_uc003,test_size=0.25 , random_state=5 )

print('X-Shape Size: ',x_uc003.shape)
print('Y-Shape Size :',y_uc003.shape)
print('X-Train Size: ',xtrain_uc003.shape)
print('Y-Train Size :',ytrain_uc003.shape)
print('X-Test Size: ',xtest_uc003.shape)
print('Y-Test Size :',ytest_uc003.shape)

model_uc003 = LinearRegression()
model_uc003.fit(xtrain_uc003 , ytrain_uc003)

# Validate Use Case 003
test_uc003 = [[552,4.63]]
model_uc003.predict(test_uc003)
ypred_uc003 = model_uc003.predict(xtest_uc003)
from sklearn import metrics
metrics.r2_score(ytest_uc003,ypred_uc003)   # This Model has performance of 99.99%


# Use Case 004 - Predictions for pipeline cost based on Budget and Expenditure
x_uc004 = df.drop(['pipeline','spend','budget'], axis=1)
y_uc004 = df['pipeline']
xtrain_uc004,xtest_uc004,ytrain_uc004,ytest_uc004 = train_test_split(x_uc004,y_uc004,test_size=0.30 , random_state=5 )

print('X-Shape Size: ',x_uc004.shape)
print('Y-Shape Size :',y_uc004.shape)
print('X-Train Size: ',xtrain_uc004.shape)
print('Y-Train Size :',ytrain_uc004.shape)
print('X-Test Size: ',xtest_uc004.shape)
print('Y-Test Size :',ytest_uc004.shape)

model_uc004 = LinearRegression()
model_uc004.fit(xtrain_uc004 , ytrain_uc004)

# Validate Use Case 004
test_uc004 = [[51,91]]
model_uc004.predict(test_uc004)
ypred_uc004 = model_uc004.predict(xtest_uc004)
from sklearn import metrics
metrics.r2_score(ytest_uc004,ypred_uc004)   # This Model has performance of 53.75%

# Train / Test - 75/25 Efficiency 53.75 
# Train / Test - 80/20 Efficiency 53.65#
# Train / Test - 70/30 Efficiency 53.85#
