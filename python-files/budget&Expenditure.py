# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:18:50 2020

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


def expDetails_pTest():
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
    
    import locale
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
    
    
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
    
    df['spend']=df['spend'].astype(str)
    df['spend']=df['spend'].str.replace(',','').str.strip()
    df['spend']=df['spend'].str.strip()
    
    df['budget']=df['budget'].astype(str)
    df['budget']=df['budget'].str.replace(',','').str.strip()
    df['budget']=df['budget'].str.strip()
   
    
    
    
    df['pipeline']=df['pipeline'].astype(float)
    df['spend']=df['spend'].astype(float)
    df['budget']=df['budget'].astype(float)
    
    		
    # Lets identify Less impactful variables when we are identifying Billing , Billing Targets , Spend and Pipeline costfor a given campaign 
    # Budget are independent variable and rest all are dependent variables.

    # mc_billings , billings_target , pipeline , spend , budget
    # Impactful variables to determin Pipeline Cost 
    model_pipeline = sm.ols(formula='pipeline~mc_billings+billings_target+spend+budget', data=df)
    fitted_pipeline = model_pipeline.fit()
    fitted_pipeline.summary()
    
      # Impactful variables to determin mc_billings
    model_mc_billings = sm.ols(formula='mc_billings~pipeline+billings_target+spend+budget' , data=df)
    fitted_mc_billings = model_mc_billings.fit()
    fitted_mc_billings.summary()

     # Impactful variables to determin billings_target
    model_billings_target = sm.ols(formula='billings_target~pipeline+mc_billings+spend+budget' , data=df)
    fitted_billings_target = model_billings_target.fit()
    fitted_billings_target.summary()
    
    # Impactful variables to determin Spend
    model_spend = sm.ols(formula='spend~billings_target+pipeline+mc_billings+budget' , data=df)
    fitted_spend = model_spend.fit()
    fitted_spend.summary()
    
    
    df1 = df
    vif_cal(df1 , "mc_billings")
    vif_cal(df1 , "billings_target")
    vif_cal(df1 , "pipeline")
    vif_cal(df1 , "spend")
    vif_cal(df1 , "budget")
    
    