# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:41:58 2020

@author: vismujum
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:\codeRepository\machine-learning\Marketing_Details.csv')
# Replace all rows that has missing values
df.dropna(inplace = True)
# Information on attributes
df.info()
# Number of Data Entries - Marketing details
df.shape
df.head()

df.rename(columns={'Visits':'visits','Unique Visitors':'unique_visitors' ,'Leads':'leads','MQL':'mql','Pipeline Count':'pipeline_count','Opportunity Accounts':'opportunity_accounts','MC Subscriptions':'mc_subscriptions','MC Net Adds':'mc_net_adds'},inplace=True)

# Use Case 001 - Predictions for leads based on Visits and Unique Visitors
x_uc001 = df.drop(['leads','mql','pipeline_count','opportunity_accounts','mc_subscriptions','mc_net_adds'], axis=1)
y_uc001 = df['leads']
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
test_uc001 = [[19,10]]
model_uc001.predict(test_uc001)
ypred_uc001 = model_uc001.predict(xtest_uc001)
from sklearn import metrics
metrics.r2_score(ytest_uc001,ypred_uc001)   # This Model has performance of 99.82%


# Use Case 002 - Predictions for MQL based on Visits , Unique Visitors and leads 
x_uc002 = df.drop(['mql','pipeline_count','opportunity_accounts','mc_subscriptions','mc_net_adds'], axis=1)
y_uc002 = df['mql']
xtrain_uc002,xtest_uc002,ytrain_uc002,ytest_uc002 = train_test_split(x_uc002,y_uc002,test_size=0.25 , random_state=5 )

model_uc002 = LinearRegression()
model_uc002.fit(xtrain_uc002 , ytrain_uc002)

# Validate Use Case 002
test_uc002 = [[19,10,5]]
model_uc002.predict(test_uc002)
ypred_uc002 = model_uc002.predict(xtest_uc002)
from sklearn import metrics
metrics.r2_score(ytest_uc002,ypred_uc002)   # This Model has performance of 99.67%

# Use Case 003 - Predictions for Pipeline Count based on Visits , Unique Visitors , leads and MQL 
x_uc003 = df.drop(['pipeline_count','opportunity_accounts','mc_subscriptions','mc_net_adds'], axis=1)
y_uc003 = df['pipeline_count']
xtrain_uc003,xtest_uc003,ytrain_uc003,ytest_uc003 = train_test_split(x_uc003,y_uc003,test_size=0.25 , random_state=5 )

model_uc003 = LinearRegression()
model_uc003.fit(xtrain_uc003 , ytrain_uc003)

# Validate Use Case 003
test_uc003 = [[19,10,5,4]]
model_uc003.predict(test_uc003)
ypred_uc003 = model_uc003.predict(xtest_uc003)
from sklearn import metrics
metrics.r2_score(ytest_uc003,ypred_uc003)   # This Model has performance of 99.36%

# Use Case 004 - Predictions for  Opportunity Account based on Visits , Unique Visitors , leads , MQL and Pipeline Count
x_uc004 = df.drop(['opportunity_accounts','mc_subscriptions','mc_net_adds'], axis=1)
y_uc004 = df['opportunity_accounts']
xtrain_uc004,xtest_uc004,ytrain_uc004,ytest_uc004 = train_test_split(x_uc004,y_uc004,test_size=0.25 , random_state=5 )

model_uc004 = LinearRegression()
model_uc004.fit(xtrain_uc004 , ytrain_uc004)

# Validate Use Case 004
test_uc004 = [[19,10,5,4,3]]
model_uc004.predict(test_uc004)
ypred_uc004 = model_uc004.predict(xtest_uc004)
from sklearn import metrics
metrics.r2_score(ytest_uc004,ypred_uc004)   # This Model has performance of 99.17%

# Use Case 005 - Predictions for MC Subscriptions  based on Visits , Unique Visitors , leads , MQL , Pipeline Count and Opportunity Account
x_uc005 = df.drop(['mc_subscriptions','mc_net_adds'], axis=1)
y_uc005 = df['mc_subscriptions']
xtrain_uc005,xtest_uc005,ytrain_uc005,ytest_uc005 = train_test_split(x_uc005,y_uc005,test_size=0.30 , random_state=5 )

model_uc005 = LinearRegression()
model_uc005.fit(xtrain_uc005 , ytrain_uc005)

# Validate Use Case 005
test_uc005 = [[19,10,5,4,3,3]]
model_uc005.predict(test_uc005)
ypred_uc005 = model_uc005.predict(xtest_uc005)
from sklearn import metrics
metrics.r2_score(ytest_uc005,ypred_uc005)   
# Train/Test 75/25 - performance of 91.72% 
# Train/Test 80/20 - performance of 91.72%
# Train/Test 70/30 - performance of 91.70%


# Use Case 006 - Predictions for MC Net Addition based on Visits , Unique Visitors , leads , MQL , Pipeline Count , Opportunity Account and MC Subscriptions  
x_uc006 = df.drop(['mc_net_adds'], axis=1)
y_uc006 = df['mc_net_adds']
xtrain_uc006,xtest_uc006,ytrain_uc006,ytest_uc006 = train_test_split(x_uc006,y_uc006,test_size=0.30 , random_state=5 )

model_uc006 = LinearRegression()
model_uc006.fit(xtrain_uc006 , ytrain_uc006)

# Validate Use Case 006
test_uc006 = [[19,10,5,4,3,3,1]]
model_uc006.predict(test_uc006)
ypred_uc006 = model_uc006.predict(xtest_uc006)
from sklearn import metrics
metrics.r2_score(ytest_uc006,ypred_uc006)  
# Train/Test 75/25 - performance of 85.00%
# Train/Test 80/20 - performance of 84.13%
# Train/Test 70/30 - performance of 84.05%
