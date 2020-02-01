# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:35:53 2019

@author: LeGrand
"""

###########################################################################
#                                                                         #
# a simple programme for creating my LinkedIn background image            #
# concept: visualise an exponential growth path with a stochastic element #
#                                                                         #
###########################################################################

# import of the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# initialise 1st dataframe: it will hold the data for plotting the graph 
data = pd.DataFrame(columns=['low','mid','high','rand'])
data.loc[0,['low','mid','high','rand']] = [1, 1, 1, 1]

# initialise 2nd dataframe: it will be used to generate different growth paths
value = pd.DataFrame(columns=['low','mid','high','rand'])
value.loc[0,['low','mid','high','rand']] = [1, 1, 1, 1]

# construct four different growth paths over 100 iterations
for i in np.arange(1,100):

    value['low'] = data.loc[i-1,'low'] * 1.012 # lower end growth paths
    value['mid'] = data.loc[i-1,'mid'] * 1.02 # mid-level growth paths   
    value['high'] = data.loc[i-1,'high'] * 1.025 # higher end grwoth paths
    value['rand'] = np.random.normal(value['mid'],i/95,1) # stochastic growth paths
    data = data.append(value).reset_index().drop('index', axis=1) # append iteration to data

# plotting 
plt.fill_between(np.arange(100),data['low'],data['high'],alpha=0.2) # area plot
plt.plot(data['mid'],color='black') # line plot mid-level growth paths
plt.plot(data['rand'],marker='o', color='grey',linewidth=1.0) #line plot stochastic growth paths
plt.axis('off') # de-activate axis from plot
plt.rcParams["figure.figsize"] = [9.0, 1.5] # define plot size
plt.savefig(r"C:\Users\Daniel\Python_scripts\theme.png", bbox_inches='tight',dpi=2000,transparent=True)
plt.close()