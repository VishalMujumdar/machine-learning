# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:57:29 2020

@author: vismujum
"""
#import numpy as np

import pandas as pd
import statsmodels.formula.api as sm

#pip install pandas
#pip install numpy

def mkt_details():
    # Read CSV File to capture Marketing Details
    df = pd.read_csv('C:\codeRepository\machine-learning\Marketing_Details.csv')
    
    # Replace all rows that has missing values
    df.dropna(inplace = True)
    
    # Information on attributes
    df.info()

    # Number of Data Entries - Marketing details
    df.shape
    df.head()

    df.rename(columns={'Visits':'visits','Unique Visitors':'unique_visitors' ,'Leads':'leads','MQL':'mql','Pipeline Count':'pipeline_count','Opportunity Accounts':'opportunity_accounts','MC Subscriptions':'mc_subscriptions','MC Net Adds':'mc_net_adds'},inplace=True)

    # Lets identify Less impactful variables when we are identifying total subscription (mc_subscriptions) are received based for a given campaign 
    # Visits and Unique visitirs are independent variable and rest all are dependent variables.

    # visits, unique_visitors,leads',mql , pipeline_count,opportunity_accounts,mc_subscriptions, mc_net_adds'
    # Impactful variables to determin MC Net Additions 
    model = sm.ols(formula='mc_net_adds~visits+unique_visitors+leads+mql+pipeline_count+opportunity_accounts+mc_subscriptions' , data=df)
    fitted = model.fit()
    fitted.summary()

    model = sm.ols(formula='mc_subscriptions~visits+unique_visitors+leads+mql+pipeline_count+opportunity_accounts' , data=df)
    fitted = model.fit()
    fitted.summary()


# Impactful variables to determin MC Subscriptions 

# Impactful variables to determin Opportunity Accounts

# Impactful variables to determin Pipeline Count


# Impactful variables to determin MQL

# Impactful variables to determin Leads

if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    mkt_details()

