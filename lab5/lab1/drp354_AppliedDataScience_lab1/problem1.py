##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1                                  #
##############################################

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from scipy.stats.stats import pearsonr

df = pd.read_csv("trafficking_data.csv")
df = df.replace(np.nan,0)
df.rename(columns={'persons prosecuted': 'persons_prosecuted', 
                   'policy index': 'policy_index',
                   'child victims':'child_victims',
                   'Adult victims':'Adult_victims',
                   'life expectancy':'life_expectancy',
                   'females in primary education':'females_education'}, inplace=True)
ind_vars = df[["gdp","policy_index","life_expectancy","females_education"]]


results_victims = sm.OLS(df["Adult_victims"],ind_vars).fit()
results_prosecuted = sm.OLS(df["persons_prosecuted"], ind_vars).fit()

print results_victims.summary()
print "Parameters:", results_victims.params
print results_prosecuted.summary()
print "Parameters:", results_prosecuted.params

print "\n\nR^2 of results_victims", results_victims.rsquared
print "R^2 of results_prosecuted", results_prosecuted.rsquared

print 'person prosecuted VS adult victim:'
print pearsonr(df["persons_prosecuted"],df["Adult_victims"])
print '\nchild victim VS adult victim:'
print pearsonr(df["child_victims"],df["Adult_victims"])
print '\ngdp VS adult victim:'
print pearsonr(df["gdp"],df["Adult_victims"])
print '\nlife expectancy VS adult victim:'
print pearsonr(df["life_expectancy"],df["Adult_victims"])
print '\nFemale primary education VS adult victim:'
print pearsonr(df["females_education"],df["Adult_victims"])
print '\npolicy index VS adult victim:'
print pearsonr(df["policy_index"],df["Adult_victims"])
