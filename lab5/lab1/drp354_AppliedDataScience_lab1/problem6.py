##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.6                                  #
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

y = df[['Adult_victims']]
x=  df[["gdp","policy_index","females_education","life_expectancy"]]
X = sm.add_constant(x)

# Model preparation
model = smf.ols(formula='Adult_victims~ 1 + gdp+ policy_index+ females_education + life_expectancy+ I(gdp ** 2.0) + I(policy_index ** 2.0)+I(females_education ** 2.0) + I(life_expectancy ** 2.0)+ I(gdp ** 3.0) + I(policy_index ** 3.0)+I(females_education ** 3.0) + I(life_expectancy ** 3.0)', data=df).fit()
print model.summary()

#new dataset
df_new = pd.read_csv("new.csv")
df_new = df_new.replace(np.nan,0)
df_new.rename(columns={'persons prosecuted': 'persons_prosecuted', 
                   'policy index': 'policy_index',
                   'child victims':'child_victims',
                   'Adult victims':'Adult_victims',
                   'life expectancy':'life_expectancy',
                   '% females in primary education':'females_education'}, inplace=True)

x_new= df_new[["gdp","policy_index","females_education","life_expectancy"]]
y_new = df_new[['Adult_victims']]
X_new = sm.add_constant(x_new)

#figure prep
plt.figure()
plt.xlabel('all predictors')
plt.ylabel('Adult_victim')

# 3-rd order polynomial with new data
plt.plot(X_new, model.predict(X_new), 'ro', label='Poly n=3 $R^2$=%.2f' % model.rsquared, 
         alpha=0.9)

#saving new predicted values to csv
df_new['Adult_victims']=model.predict(X_new)
df_new['Adult_victims'] = df_new['Adult_victims'].astype(int)
df_new.to_csv('predicted.csv')

plt.savefig('figure_6.png')
#plt.show()


