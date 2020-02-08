# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:57:29 2020

@author: vismujum
"""
#import numpy as np

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import tree

#pip install pandas
#pip install numpy
def vif_cal(input_data, dependent_col):
    x_vars=input_data.drop([dependent_col], axis=1)
    xvar_names=x_vars.columns
    for i in range(0,xvar_names.shape[0]):
        y1=x_vars[xvar_names[i]]
        x1=x_vars[xvar_names.drop(xvar_names[i])]
        rsq=sm.ols(formula="y1~x1", data=x_vars).fit().rsquared
        vif=round(1/(1-rsq),2)
        print (xvar_names[i], " VIF = " , vif)



def mktDetails_pTest():
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
    model_mcNetAdds = sm.ols(formula='mc_net_adds~visits+unique_visitors+leads+mql+pipeline_count+opportunity_accounts+mc_subscriptions' , data=df)
    fitted_mcNetAdds = model_mcNetAdds.fit()
    fitted_mcNetAdds.summary()
    
    model_mcNetAdds = sm.ols(formula='mc_net_adds~unique_visitors+leads+mql+pipeline_count+opportunity_accounts+mc_subscriptions' , data=df)
    fitted_mcNetAdds = model_mcNetAdds.fit()
    fitted_mcNetAdds.summary()

    # Apart from Visits attribute all other paraemters are required to predict no. of Net Addition in Subsctions


    # Impactful variables to determin MC Subscriptions 
    model_mcSubs = sm.ols(formula='mc_subscriptions~visits+unique_visitors+leads+mql+pipeline_count+opportunity_accounts' , data=df)
    fitted_mcSubs = model_mcSubs.fit()
    fitted_mcSubs.summary()
    # All paraemters are required to predict No of Subsctions achived by Given Campaign

      # Impactful variables to determin Pipeline Count
    model_pipeLine = sm.ols(formula='pipeline_count~visits+unique_visitors+leads+mql+opportunity_accounts' , data=df)
    fitted_pipeLine = model_pipeLine.fit()
    fitted_pipeLine.summary()
    # Visits , Leads and MQL play an important role in identifying Pipeline count for a marketing campaign
    
    # Impactful variables to determin Opportunity Accounts
    model_opporAcc = sm.ols(formula='opportunity_accounts~visits+unique_visitors+leads+mql' , data=df)
    fitted_opporAcc = model_opporAcc.fit()
    fitted_opporAcc.summary()
    # All parameters are required to predict Number of opportunity accounts that are acived from Marketing campaign
    
    # Impactful variables to determin MQL
    model_mql = sm.ols(formula='mql~visits+unique_visitors+leads' , data=df)
    fitted_mql = model_mql.fit()
    fitted_mql.summary()
    # All parameters are required to predict Number of opportunity accounts that are acived from Marketing campaign

    # Impactful variables to determin Leads
    model_leads = sm.ols(formula='mql~visits+unique_visitors' , data=df)
    fitted_leads = model_leads.fit()
    fitted_leads.summary()

def mktDetails_decisionTree():
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

    features = list(df.columns[0:6])
    x = df[features]
    y = df['mc_net_adds']
    clf = tree.DecisionTreeClassifier(max_depth=3)
    clf.fit(x,y)
    from IPython.display import Image
    from sklearn.externals.six import StringIO
    from sklearn import tree
    import pydotplus
    #import graphviz

    dot_data = StringIO()
    tree.export_graphviz(clf,out_file=dot_data,feature_names=features , filled=True,rounded=True, impurity=False)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

    Image(graph.create_png())

def mktDetails_VIFTest():
    df = pd.read_csv('C:\codeRepository\machine-learning\Marketing_Details.csv')
    # Replace all rows that has missing values
    df.dropna(inplace = True)
    # Information on attributes
    df.info()
    # Number of Data Entries - Marketing details
    df.shape
    df.head()
    df.rename(columns={'Visits':'visits','Unique Visitors':'unique_visitors' ,'Leads':'leads','MQL':'mql','Pipeline Count':'pipeline_count','Opportunity Accounts':'opportunity_accounts','MC Subscriptions':'mc_subscriptions','MC Net Adds':'mc_net_adds'},inplace=True)
    df1 = df.drop('visits')
    vif_cal(df1 , "mc_net_adds")


   
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    mktDetails_pTest()

