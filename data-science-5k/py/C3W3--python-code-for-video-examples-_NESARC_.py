# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:54:18 2015

@author: jrose01
"""

import numpy
import pandas
import statsmodels.api as sm
import seaborn
import statsmodels.formula.api as smf 

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

data = pandas.read_csv('nesarc_pds.csv', low_memory=False)

##############################################################################
# DATA MANAGEMENT
##############################################################################

#setting variables you will be working with to numeric
data['IDNUM'] =pandas.to_numeric(data['IDNUM'], errors='coerce')
data['TAB12MDX'] = pandas.to_numeric(data['TAB12MDX'], errors='coerce')
data['MAJORDEPLIFE'] = pandas.to_numeric(data['MAJORDEPLIFE'], errors='coerce')
data['NDSymptoms'] = pandas.to_numeric(data['NDSymptoms'], errors='coerce')
data['SOCPDLIFE'] = pandas.to_numeric(data['SOCPDLIFE'], errors='coerce')
data['S3AQ3C1'] = pandas.to_numeric(data['S3AQ3C1'], errors='coerce')
data['AGE'] =pandas.to_numeric(data['AGE'], errors='coerce')
data['SEX'] = pandas.to_numeric(data['SEX'], errors='coerce')

data['S3AQ3B1'] = pandas.to_numeric(data['S3AQ3B1'], errors='coerce')
data['CHECK321'] =pandas.to_numeric( data['CHECK321'], errors='coerce')
data['S3AQ8B11'] = pandas.to_numeric(data['S3AQ8B11'], errors='coerce')
data['S3AQ8B12'] = pandas.to_numeric(data['S3AQ8B12'], errors='coerce')
data['S3AQ8B13'] = pandas.to_numeric(data['S3AQ8B13'], errors='coerce')
data['S3AQ8B7A'] = pandas.to_numeric(data['S3AQ8B7A'], errors='coerce')
data['S3AQ8B7B'] = pandas.to_numeric(data['S3AQ8B7B'], errors='coerce')
data['S3AQ8B7C'] = pandas.to_numeric(data['S3AQ8B7C'], errors='coerce')
data['S3AQ8B7D'] = pandas.to_numeric(data['S3AQ8B7D'], errors='coerce')
data['S3AQ8B7E'] = pandas.to_numeric(data['S3AQ8B7E'], errors='coerce')
data['S3AQ8B7F'] = pandas.to_numeric(data['S3AQ8B7F'], errors='coerce')
data['S3AQ8B7G'] = pandas.to_numeric(data['S3AQ8B7G'], errors='coerce')
data['S3AQ8B7H'] = pandas.to_numeric(data['S3AQ8B7H'], errors='coerce')
data['S3AQ8B7J'] = pandas.to_numeric(data['S3AQ8B7J'], errors='coerce')

data['S6Q1'] = pandas.to_numeric(data['S6Q1'], errors='coerce')
data['S6Q2'] = pandas.to_numeric(data['S6Q2'], errors='coerce')
data['S6Q3'] = pandas.to_numeric(data['S6Q3'], errors='coerce')
data['S6Q7'] = pandas.to_numeric(data['S6Q7'], errors='coerce')
data['S6Q61'] = pandas.to_numeric(data['S6Q61'], errors='coerce')
data['S6Q62'] = pandas.to_numeric(data['S6Q62'], errors='coerce')
data['S6Q63'] = pandas.to_numeric(data['S6Q63'], errors='coerce')
data['S6Q64'] = pandas.to_numeric(data['S6Q64'], errors='coerce')
data['S6Q65'] = pandas.to_numeric(data['S6Q65'], errors='coerce')
data['S6Q66'] = pandas.to_numeric(data['S6Q66'], errors='coerce')
data['S6Q67'] = pandas.to_numeric(data['S6Q67'], errors='coerce')
data['S6Q68'] = pandas.to_numeric(data['S6Q68'], errors='coerce')
data['S6Q69'] = pandas.to_numeric(data['S6Q69'], errors='coerce')
data['S6Q610'] = pandas.to_numeric(data['S6Q610'], errors='coerce')
data['S6Q611'] = pandas.to_numeric(data['S6Q611'], errors='coerce')
data['S6Q612'] = pandas.to_numeric(data['S6Q612'], errors='coerce')
data['S6Q613'] = pandas.to_numeric(data['S6Q613'], errors='coerce')

data['S3AQ3C1']=data['S3AQ3C1'].replace(99, numpy.nan)

# run this subset code to do the NDsymptoms regression (age 18-25, smoked in past month)
# pandas gives observations missing on all symptoms (N=3) a value of zero, but should be nan
# have to delete them 
sub1=data[(data['AGE']<=25) & (data['CHECK321']==1) & (data['S3AQ3B1']==1) & 
(data['IDNUM']!=20346) & (data['IDNUM']!=36471) & (data['IDNUM']!=28724)]

# run this code to do all other regression analyses
sub1=data[(data['AGE']<=25) & (data['CHECK321']==1) & (data['S3AQ3B1']==1)]

# Current Tolerance criteria #1 DSM-IV
def crit1 (row):
   if row['S3AQ8B11']==1 or row['S3AQ8B12'] == 1 :
      return 1
   elif row['S3AQ8B11']==2 and row['S3AQ8B12']==2 :
      return 0
sub1['crit1'] = sub1.apply (lambda row: crit1 (row),axis=1)
chk2 = sub1['crit1'].value_counts(sort=False, dropna=False)
print (chk2)
chk3 = sub1['S3AQ8B11'].value_counts(sort=False, dropna=False)
print chk3
chk4 = sub1['S3AQ8B12'].value_counts(sort=False, dropna=False)
print chk4
print pandas.crosstab(sub1['S3AQ8B11'], sub1['S3AQ8B12'])

c1 = sub1['S3AQ8B7J'].value_counts(sort=False, dropna=False)
print (c1)

#Current 8 WITHDRAWAL SUB-SYMPTOMS IN DSM-IV (recode 1,2 to 0,1 for summing)
# after recoding 9s to missing
recode1 = {1: 1, 2: 0}
sub1['S3AQ8B7A']=sub1['S3AQ8B7A'].replace(9, numpy.nan)
sub1['S3AQ8B7A']= sub1['S3AQ8B7A'].map(recode1)
sub1['S3AQ8B7B']=sub1['S3AQ8B7B'].replace(9, numpy.nan)
sub1['S3AQ8B7B']= sub1['S3AQ8B7B'].map(recode1)
sub1['S3AQ8B7C']=sub1['S3AQ8B7C'].replace(9, numpy.nan)
sub1['S3AQ8B7C']= sub1['S3AQ8B7C'].map(recode1)
sub1['S3AQ8B7D']=sub1['S3AQ8B7D'].replace(9, numpy.nan)
sub1['S3AQ8B7D']= sub1['S3AQ8B7D'].map(recode1)
sub1['S3AQ8B7E']=sub1['S3AQ8B7E'].replace(9, numpy.nan)
sub1['S3AQ8B7E']= sub1['S3AQ8B7E'].map(recode1)
sub1['S3AQ8B7F']=sub1['S3AQ8B7F'].replace(9, numpy.nan)
sub1['S3AQ8B7F']= sub1['S3AQ8B7F'].map(recode1)
sub1['S3AQ8B7G']=sub1['S3AQ8B7G'].replace(9, numpy.nan)
sub1['S3AQ8B7G']= sub1['S3AQ8B7G'].map(recode1)
sub1['S3AQ8B7H']=sub1['S3AQ8B7H'].replace(9, numpy.nan)
sub1['S3AQ8B7H']= sub1['S3AQ8B7H'].map(recode1)

# check recode
chk1c = sub1['S3AQ8B7J'].value_counts(sort=False, dropna=False)
print (chk1c)

# sum symptoms
sub1['CWITHDR_COUNT'] = numpy.nansum([sub1['S3AQ8B7A'], sub1['S3AQ8B7B'], sub1['S3AQ8B7C'], 
              sub1['S3AQ8B7D'], sub1['S3AQ8B7E'], sub1['S3AQ8B7F'],
              sub1['S3AQ8B7G'], sub1['S3AQ8B7H']], axis=0)

# check to make sure sum code worked
chksum=sub1[['IDNUM','S3AQ8B7A', 'S3AQ8B7B', 'S3AQ8B7C', 'S3AQ8B7D', 
           'S3AQ8B7E', 'S3AQ8B7F', 'S3AQ8B7G', 'S3AQ8B7H', 'CWITHDR_COUNT']]
chksum.head(n=50)

chk1d = sub1['CWITHDR_COUNT'].value_counts(sort=False, dropna=False)
print (chk1d)

# withdrawal (yes/no)
def crit2 (row):
   if row['CWITHDR_COUNT']>=4 or row['S3AQ8B7J']==1:
      return 1
   elif row['CWITHDR_COUNT']<4 and row['S3AQ8B7J']!=1:
      return 0
sub1['crit2'] = sub1.apply (lambda row: crit2 (row),axis=1)
print (pandas.crosstab(sub1['CWITHDR_COUNT'], sub1['crit2']))


#Current Larger amount or longer period criteria #3 DSM-IV
sub1['S3AQ8B13']=sub1['S3AQ8B13'].replace(9, numpy.nan)
sub1['S3AQ8B13']= sub1['S3AQ8B13'].map(recode1)
  
chk1d = sub1['S3AQ8B13'].value_counts(sort=False, dropna=False)
print (chk1d)


#Current Cut down criteria #4 DSM-IV
sub1['S3AQ8B6'] = pandas.to_numeric(sub1['S3AQ8B6'], errors='coerce')
sub1['S3AQ8B1'] = pandas.to_numeric(sub1['S3AQ8B1'], errors='coerce')
def crit4 (row):
   if row['S3AQ8B6']==1 or row['S3AQ8B1'] == 1 :
      return 1
   elif row['S3AQ8B6']==2 and row['S3AQ8B1']==2 :
      return 0
sub1['crit4'] = sub1.apply (lambda row: crit4 (row),axis=1)
chk1e = sub1['crit4'].value_counts(sort=False, dropna=False)
print (chk1e)


#Current Substance aCtivities criteria #5 DSM-IV
sub1['S3AQ8B5'] = pandas.to_numeric(sub1['S3AQ8B5'], errors='coerce')
sub1['S3AQ8B5']=sub1['S3AQ8B5'].replace(9, numpy.nan)
sub1['S3AQ8B5']= sub1['S3AQ8B5'].map(recode1)

chk1f = sub1['S3AQ8B5'].value_counts(sort=False, dropna=False)
print (chk1f)

#Current Reduce aCtivities criteria #6 DSM-IV
sub1['S3AQ8B2'] = pandas.to_numeric(sub1['S3AQ8B2'], errors='coerce')
sub1['S3AQ8B3'] = pandas.to_numeric(sub1['S3AQ8B3'], errors='coerce')
def crit6 (row):
   if row['S3AQ8B2']==1 or row['S3AQ8B3'] == 1 :
      return 1
   elif row['S3AQ8B2']==2 and row['S3AQ8B3']==2 :
      return 0
sub1['crit6'] = sub1.apply (lambda row: crit6 (row),axis=1)
chk1g = sub1['crit6'].value_counts(sort=False, dropna=False)
print (chk1g)

#Current use continued despite knowledge of physical or psychological problem criteria #7 DSM-IV
sub1['S3AQ8B4'] = pandas.to_numeric(sub1['S3AQ8B4'], errors='coerce')
sub1['S3AQ8B14'] = pandas.to_numeric(sub1['S3AQ8B14'], errors='coerce')
def crit7 (row):
   if row['S3AQ8B4']==1 or row['S3AQ8B14'] == 1 :
      return 1
   elif row['S3AQ8B4']==2 and row['S3AQ8B14']==2 :
      return 0
sub1['crit7'] = sub1.apply (lambda row: crit7 (row),axis=1)
chk1h = sub1['crit7'].value_counts(sort=False, dropna=False)
print (chk1h)

# sum all symptoms (np.nansum allows rows with some missing values to count all valid values)
# instead of recoding the sum to nan
sub1['NDSymptoms'] = numpy.nansum([sub1['crit1'], sub1['crit2'], sub1['S3AQ8B13'], 
              sub1['crit4'], sub1['S3AQ8B5'], sub1['crit6'],
              sub1['crit7']], axis=0 )
chk2 = sub1['NDSymptoms'].value_counts(sort=False, dropna=False)
print (chk2)


c1 = sub1["MAJORDEPLIFE"].value_counts(sort=False, dropna=False)
print(c1)
c2 = sub1["AGE"].value_counts(sort=False, dropna=False)
print(c2)
# binary nictoine dependence
def NICOTINEDEP (x):
   if x['TAB12MDX']==1:
      return 1
   else: 
      return 0
sub1['NICOTINEDEP'] = sub1.apply (lambda x: NICOTINEDEP (x), axis=1)
print (pandas.crosstab(sub1['TAB12MDX'], sub1['NICOTINEDEP']))

# rename variables
sub1.rename(columns={'S3AQ3C1': 'numbercigsmoked'}, inplace=True)

c6 = sub1["numbercigsmoked"].value_counts(sort=False, dropna=False)
print(c6)

def PANIC (x1):
    if ((x1['S6Q1']==1 and x1['S6Q2']==1) or (x1['S6Q2']==1 and x1['S6Q3']==1) or 
    (x1['S6Q3']==1 and x1['S6Q61']==1) or (x1['S6Q61']==1 and x1['S6Q62']==1) or 
    (x1['S6Q62']==1 and x1['S6Q63']==1) or (x1['S6Q63']==1 and x1['S6Q64']==1) or 
    (x1['S6Q64']==1 and x1['S6Q65']==1) or (x1['S6Q65']==1 and x1['S6Q66']==1) or 
    (x1['S6Q66']==1 and x1['S6Q67']==1) or (x1['S6Q67']==1 and x1['S6Q68']==1) or 
    (x1['S6Q68']==1 and x1['S6Q69']==1) or (x1['S6Q69']==1 and x1['S6Q610']==1) or 
    (x1['S6Q610']==1 and x1['S6Q611']==1) or (x1['S6Q611']==1 and x1['S6Q612']==1) or 
    (x1['S6Q612']==1 and x1['S6Q613']==1) or (x1['S6Q613']==1 and x1['S6Q7']==1) or 
    x1['S6Q7']==1):
        return 1
    else:
        return 0
sub1['PANIC'] = sub1.apply (lambda x1: PANIC (x1), axis=1)
c7 = sub1["PANIC"].value_counts(sort=False, dropna=False)
print(c7)

# 4 category ethnicity variable
sub1['ETHRACE2A'] = pandas.to_numeric(sub1['ETHRACE2A'], errors='coerce')
recode2 = {1: 1, 2: 2, 3: 3, 4: 3, 5: 0}
sub1['ETHRACE2A'] = sub1['ETHRACE2A'].replace(9, numpy.nan)
sub1['ETHRACE'] = sub1['ETHRACE2A'].map(recode2)

c8 = sub1["ETHRACE2A"].value_counts(sort=False, dropna=False)
print(c8)

c9 = sub1["ETHRACE"].value_counts(sort=False, dropna=False)
print(c9)

##############################################################################
# END DATA MANAGEMENT
##############################################################################

##############################################################################
# MULTIPLE REGRESSION & CONFIDENCE INTERVALS
##############################################################################

# adding number of cigarettes smoked as an explanatory variable 
# center quantitative IVs for regression analysis
sub1['numbercigsmoked_c'] = (sub1['numbercigsmoked'] - sub1['numbercigsmoked'].mean())
print (sub1['numbercigsmoked_c'].mean()) 

sub3 = sub1[['NDSymptoms', 'numbercigsmoked', 'MAJORDEPLIFE']].dropna()

# multiple regression with depression and centered number of cigarettes smoked
reg2 = smf.ols('NDSymptoms ~ MAJORDEPLIFE + numbercigsmoked_c', data=sub1).fit()
print (reg2.summary())

# linear regression analysis with dysphoria 
reg3 = smf.ols('NDSymptoms ~ DYSLIFE', data=sub1).fit()
print (reg3.summary())

# multiple regression analysis with dysphoria & depression
reg4 = smf.ols('NDSymptoms ~ DYSLIFE + MAJORDEPLIFE', data=sub1).fit()
print (reg4.summary())

# multiple regression analysis with dysphoria & depression + other covariates
# centering age variable
sub1['age_c']=(sub1['AGE'] - sub1['AGE'].mean())
print (sub1['age_c'].mean()) 

reg5 = smf.ols('NDSymptoms ~ DYSLIFE + MAJORDEPLIFE + numbercigsmoked_c + age_c + SEX', data=sub1).fit()
print (reg5.summary())


