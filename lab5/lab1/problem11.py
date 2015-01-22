##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.11                                 #
##############################################
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from scipy.stats.stats import pearsonr

df = pd.read_csv("cleaned_data_population.csv")

#y = df[['Adult_victims']]
#x=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims","internet_penet","connected_dev"]]

print 'Internet penetration VS adult victim:'
print pearsonr(df["internet_penet"],df["Adult_victims"])
print '\nConnected device VS adult victim:'
print pearsonr(df["connected_dev"],df["Adult_victims"])


y = df[['Adult_victims']]
x=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims"]]
x2=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims","internet_penet"]]
x3=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims","connected_dev"]]
X = sm.add_constant(x)
X2 = sm.add_constant(x2)
X3 = sm.add_constant(x3)

#OLS 1
linear = sm.OLS(y, X).fit()
print linear.summary()

#OLS 2
linear = sm.OLS(y, X2).fit()
print linear.summary()

#OLS 3
linear = sm.OLS(y, X3).fit()
print linear.summary()



