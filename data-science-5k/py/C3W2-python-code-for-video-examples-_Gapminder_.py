# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:46:09 2015

@author: jrose01
"""
import numpy as numpyp
import pandas as pandas
import statsmodels.api
import statsmodels.formula.api as smf

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#call in data set
data = pandas.read_csv('gapminder.csv')

# convert variables to numeric format using convert_objects function
data['internetuserate'] = pandas.to_numeric(data['internetuserate'], errors='coerce')
data['urbanrate'] = pandas.to_numeric(data['urbanrate'], errors='coerce')

############################################################################################
# BASIC LINEAR REGRESSION
############################################################################################
scat1 = seaborn.regplot(x="urbanrate", y="internetuserate", scatter=True, data=data)
plt.xlabel('Urbanization Rate')
plt.ylabel('Internet Use Rate')
plt.title ('Scatterplot for the Association Between Urban Rate and Internet Use Rate')
print(scat1)

print ("OLS regression model for the association between urban rate and internet use rate")
reg1 = smf.ols('internetuserate ~ urbanrate', data=data).fit()
print (reg1.summary())



