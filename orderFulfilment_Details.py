# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:56:15 2020

@author: vismujum
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

def vif_cal(input_data, dependent_col):
    x_vars=input_data.drop([dependent_col], axis=1)
    xvar_names=x_vars.columns
    for i in range(0,xvar_names.shape[0]):
        y1=x_vars[xvar_names[i]]
        x1=x_vars[xvar_names.drop(xvar_names[i])]
        rsq=sm.ols(formula="y1~x1", data=x_vars).fit().rsquared
        vif=round(1/(1-rsq),2)
        print (xvar_names[i], " VIF = " , vif)
        

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
    
   
    
    		
    # Lets identify Less impactful variables - total_acc , touched_acc, engaged_acc,hiValued_acc , won_acc','
    # orders, cart_additions , purchase'
    
    
    # Impactful variables to determin purchase
    # Inputs used are - total_acc , touched_acc, engaged_acc,hiValued_acc , won_acc',' orders inquired, cart_additions
    model_purchase = sm.ols(formula='purchase~total_acc+touched_acc+engaged_acc+hiValued_acc+won_acc+orders+cart_additions', data=df)
    fitted_purchase = model_purchase.fit()
    fitted_purchase.summary()
    
    # Impactful variables to determin cart_additions
    # Inputs used are - total_acc , touched_acc, engaged_acc,hiValued_acc , won_acc , orders Inquired
    model_cart_additions = sm.ols(formula='cart_additions~total_acc+touched_acc+engaged_acc+hiValued_acc+won_acc+orders' , data=df)
    fitted_cart_additions = model_cart_additions.fit()
    fitted_cart_additions.summary()

    # Impactful variables to determin Orders Inquired
    # Inputs used are - total_acc , touched_acc, engaged_acc,hiValued_acc , won_acc
    model_orders = sm.ols(formula='orders~total_acc+touched_acc+engaged_acc+hiValued_acc+won_acc' , data=df)
    fitted_orders = model_orders.fit()
    fitted_orders.summary()
    
    # Impactful variables to determin Won Accounts
    # Inputs used are - total_acc , touched_acc, engaged_acc,hiValued_acc
    model_won_acc = sm.ols(formula='won_acc~total_acc+touched_acc+engaged_acc+hiValued_acc' , data=df)
    fitted_won_acc = model_won_acc.fit()
    fitted_won_acc.summary()
    
    # Impactful variables to determin Hi Valued Account
    # Inputs used are - total_acc , touched_acc  , engaged accounts
    model_hiValued_acc = sm.ols(formula='hiValued_acc~total_acc+touched_acc+engaged_acc' , data=df)
    fitted_hiValued_acc = model_hiValued_acc.fit()
    fitted_hiValued_acc.summary()
    
     # Impactful variables to determin engaged accounts
    # Inputs used are - total_acc , touched_acc  , 
    model_engaged_acc = sm.ols(formula='engaged_acc~total_acc+touched_acc' , data=df)
    fitted_engaged_acc = model_engaged_acc.fit()
    fitted_engaged_acc.summary()
    
    
    
    df1 = df
    vif_cal(df1 , "purchase")
    vif_cal(df1 , "cart_additions")
    vif_cal(df1 , "orders")
    vif_cal(df1 , "won_acc")
    vif_cal(df1 , "hiValued_acc")
    vif_cal(df1 , "engaged_acc")
    vif_cal(df1 , "touched_acc")
    
   