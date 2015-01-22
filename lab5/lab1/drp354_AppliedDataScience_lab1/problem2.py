##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2                                  #
##############################################
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.graphics as smgraphics
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import numpy as np
from scipy import stats

df = pd.read_csv("trafficking_data.csv")
df = df.replace(np.nan,0)
df.rename(columns={'persons prosecuted': 'persons_prosecuted', 
                   'policy index': 'policy_index',
                   'child victims':'child_victims',
                   'Adult victims':'Adult_victims',
                   'life expectancy':'life_expectancy',
                   'females in primary education':'females_education'}, inplace=True)

x=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims"]]
y = df[['Adult_victims']]
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

# Find outliers #
test = results.outlier_test()
outlier_id = []
for index, row in test.iterrows():
  if abs(row['student_resid'])>3: 
    outlier_id.append(index)

print "Outlier: ", outlier_id
print df.ix[outlier_id]

df_new = df.drop(df.index[outlier_id])
x2=  df_new[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims"]]
y2 = df_new[['Adult_victims']]
X2 = sm.add_constant(x2)
model = sm.OLS(y2, X2)
results_new = model.fit()
print(results_new.summary())

df_new.to_csv('cleaned_data.csv')

#plot
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig = sm.graphics.influence_plot(results, ax=ax, criterion="cooks")
fig = sm.graphics.influence_plot(results_new, ax=ax2, criterion="cooks")
plt.show()
