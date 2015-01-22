##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3                                  #
##############################################
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.graphics as smgraphics
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import numpy as np
from scipy import stats
import math

df = pd.read_csv("cleaned_data.csv")

results = smf.ols("Adult_victims~ persons_prosecuted + child_victims+ gdp+ policy_index+ females_education + life_expectancy ", data=df).fit()
results_log = smf.ols("Adult_victims ~ np.log1p(persons_prosecuted)+ np.log1p(child_victims)+ np.log1p(gdp)+ np.log1p(policy_index)+ np.log1p(females_education) + np.log1p(life_expectancy) ", data=df).fit()

print results.summary()
print results_log.summary()

df['policy_index'] = np.log1p(df['policy_index'])
df['persons_prosecuted'] = np.log1p(df['persons_prosecuted'])
df['child_victims'] = np.log1p(df['child_victims'])
df['gdp'] = np.log1p(df['gdp'])
df['females_education'] = np.log1p(df['females_education'])
df['life_expectancy'] = np.log1p(df['life_expectancy'])
df.to_csv('cleaned_data_log.csv')
