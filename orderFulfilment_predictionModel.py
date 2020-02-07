# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:31:32 2020

@author: vismujum
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 



def orderDetails_pTest():
    # Read CSV File to capture Marketing Details
    df = pd.read_csv('C:\codeRepository\machine-learning\OrderFulfilment_Details.csv')
    
    # Replace all rows that has missing values
    df.dropna(inplace = True)
    
    # Information on attributes
    df.info()

    # Number of Data Entries - Marketing details
    df.shape
    df.head()

    df.rename(columns={'Total Accounts':'total_acc','Touched Accounts':'touched_acc','Engaged Accounts':'engaged_acc','Hi-Valued Accounts':'hiValued_acc','Won Accounts':'won_acc','Orders':'orders','Cart Additions':'cart_additions','Purchase':'purchase'},inplace=True)
    
   #total_acc , touched_acc , engaged_acc , hiValued_acc , won_acc , orders , cart_additions , purchase 
   
   # Use Case 001 - Predictions for Engaged Accounts based on Total Account and Touched Account
    x_uc001 = df.drop(['engaged_acc', 'hiValued_acc', 'won_acc', 'orders', 'cart_additions', 'purchase'], axis=1)
    y_uc001 = df['engaged_acc']
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
    test_uc001 = [[111,37]]
    model_uc001.predict(test_uc001)
    ypred_uc001 = model_uc001.predict(xtest_uc001)
    from sklearn import metrics
    metrics.r2_score(ytest_uc001,ypred_uc001)   # This Model has performance of 99.82%
    
    # Use Case 002 - Predictions for Hi Valued Account based on Total Account , Touched Account and Engaged Account
    x_uc002 = df.drop(['hiValued_acc', 'won_acc', 'orders', 'cart_additions', 'purchase'], axis=1)
    y_uc002 = df['hiValued_acc']
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
    test_uc002 = [[111,37,18]]
    model_uc002.predict(test_uc002)
    ypred_uc002 = model_uc002.predict(xtest_uc002)
    from sklearn import metrics
    metrics.r2_score(ytest_uc002,ypred_uc002)   # This Model has performance of 99.43%
    
     # Use Case 003 - Predictions for Won Accounts based on Hi Valued Account , Total Account , Touched Account and Engaged Account
    x_uc003 = df.drop([ 'won_acc', 'orders', 'cart_additions', 'purchase'], axis=1)
    y_uc003 = df['won_acc']
    xtrain_uc003,xtest_uc003,ytrain_uc003,ytest_uc003 = train_test_split(x_uc003,y_uc003,test_size=0.30 , random_state=5 )

    print('X-Shape Size: ',x_uc003.shape)
    print('Y-Shape Size :',y_uc003.shape)
    print('X-Train Size: ',xtrain_uc003.shape)
    print('Y-Train Size :',ytrain_uc003.shape)
    print('X-Test Size: ',xtest_uc003.shape)
    print('Y-Test Size :',ytest_uc003.shape)

    model_uc003 = LinearRegression()
    model_uc003.fit(xtrain_uc003 , ytrain_uc003)

    # Validate Use Case 003
    test_uc003 = [[111,37,18,9]]
    model_uc003.predict(test_uc003)
    ypred_uc003 = model_uc003.predict(xtest_uc003)
    from sklearn import metrics
    metrics.r2_score(ytest_uc003,ypred_uc003)   # This Model has performance of 94.80%
    
    # Use Case 004 - Predictions for Qualified Orders based on Won Accounts , Hi Valued Account , Total Account , Touched Account and Engaged Account
    x_uc004 = df.drop([ 'orders', 'cart_additions', 'purchase'], axis=1)
    y_uc004 = df['orders']
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
    test_uc004 = [[111,37,18,9,5]]
    model_uc004.predict(test_uc004)
    ypred_uc004 = model_uc004.predict(xtest_uc004)
    from sklearn import metrics
    metrics.r2_score(ytest_uc004,ypred_uc004)   # This Model has performance of 98.63%

    # Use Case 005 - Predictions for Cart Additions based on Qualified Orders ,Won Accounts , Hi Valued Account , Total Account , Touched Account and Engaged Account
    x_uc005 = df.drop([ 'cart_additions', 'purchase'], axis=1)
    y_uc005 = df['cart_additions']
    xtrain_uc005,xtest_uc005,ytrain_uc005,ytest_uc005 = train_test_split(x_uc005,y_uc005,test_size=0.25 , random_state=5 )

    print('X-Shape Size: ',x_uc005.shape)
    print('Y-Shape Size :',y_uc005.shape)
    print('X-Train Size: ',xtrain_uc005.shape)
    print('Y-Train Size :',ytrain_uc005.shape)
    print('X-Test Size: ',xtest_uc005.shape)
    print('Y-Test Size :',ytest_uc005.shape)

    model_uc005 = LinearRegression()
    model_uc005.fit(xtrain_uc005 , ytrain_uc005)

    # Validate Use Case 005
    test_uc005 = [[111,37,18,9,5,9]]
    model_uc005.predict(test_uc005)
    ypred_uc005 = model_uc005.predict(xtest_uc005)
    from sklearn import metrics
    metrics.r2_score(ytest_uc005,ypred_uc005)   # This Model has performance of 99.82%

 # Use Case 006 - Predictions for Order Provisioned based on Cart Additions , Qualified Orders ,Won Accounts , Hi Valued Account , Total Account , Touched Account and Engaged Account
    x_uc006 = df.drop([ 'purchase'], axis=1)
    y_uc006 = df['purchase']
    xtrain_uc006,xtest_uc006,ytrain_uc006,ytest_uc006 = train_test_split(x_uc006,y_uc006,test_size=0.25 , random_state=5 )

    print('X-Shape Size: ',x_uc006.shape)
    print('Y-Shape Size :',y_uc006.shape)
    print('X-Train Size: ',xtrain_uc006.shape)
    print('Y-Train Size :',ytrain_uc006.shape)
    print('X-Test Size: ',xtest_uc006.shape)
    print('Y-Test Size :',ytest_uc006.shape)

    model_uc006 = LinearRegression()
    model_uc006.fit(xtrain_uc006 , ytrain_uc006)

    # Validate Use Case 004
    test_uc006 = [[111,37,18,9,5,9,23]]
    model_uc006.predict(test_uc006)
    ypred_uc006 = model_uc006.predict(xtest_uc006)
    from sklearn import metrics
    metrics.r2_score(ytest_uc006,ypred_uc006)   # This Model has performance of 99.82%