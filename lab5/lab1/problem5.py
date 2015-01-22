##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.5                                  #
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

df = pd.read_csv("cleaned_data_population.csv")

#adding new data
sLength = len(df['gdp'])
df['new_data'] = pd.Series(np.random.randn(sLength), index=df.index)

#conver to log
df['policy_index'] = np.log1p(df['policy_index'])
df['persons_prosecuted'] = np.log1p(df['persons_prosecuted'])
df['child_victims'] = np.log1p(df['child_victims'])
df['gdp'] = np.log1p(df['gdp'])
df['females_education'] = np.log1p(df['females_education'])
df['life_expectancy'] = np.log1p(df['life_expectancy'])
df['unemployment'] = np.log1p(df['unemployment'])

y = df[['Adult_victims']]
x=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims"]]
X = sm.add_constant(x)
x2=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims","unemployment"]]
X2 = sm.add_constant(x2)

#figure prep
plt.figure()
plt.scatter(x.gdp,y, s=10, alpha=0.3)
plt.scatter(x.policy_index,y, s=10, alpha=0.3)
plt.scatter(x.life_expectancy,y, s=10, alpha=0.3)
plt.scatter(x.persons_prosecuted,y, s=10, alpha=0.3)
plt.scatter(x.child_victims,y, s=10, alpha=0.3)
plt.scatter(x.females_education,y, s=10, alpha=0.3)
plt.scatter(x2.unemployment,y, s=10, alpha=0.3)
plt.ylim([-5,30])
plt.xlabel('all predictors')
plt.ylabel('Adult victim')
x=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims"]]
y = df[['Adult_victims']]
X = sm.add_constant(x)

# 3-rd order polynomial
poly_3 = smf.ols(formula='Adult_victims~ 1 + persons_prosecuted + child_victims+ gdp+ policy_index+ females_education + life_expectancy+I(persons_prosecuted ** 2.0) + I(child_victims ** 2.0)+ I(gdp ** 2.0) + I(policy_index ** 2.0)+I(females_education ** 2.0) + I(life_expectancy ** 2.0)+I(persons_prosecuted ** 3.0) + I(child_victims ** 3.0)+ I(gdp ** 3.0) + I(policy_index ** 3.0)+I(females_education ** 3.0) + I(life_expectancy ** 3.0)', data=df).fit()
print poly_3.summary()
plt.plot(x, poly_3.predict(X), 'g+', label='Before adding data $R^2$=%.2f' % poly_3.rsquared, 
         alpha=0.9)

# 3-rd order polynomial with new data
newpoly_3 = smf.ols(formula='Adult_victims~ 1 + persons_prosecuted + child_victims+ gdp+ policy_index+ females_education + life_expectancy+unemployment+I(persons_prosecuted ** 2.0) + I(child_victims ** 2.0)+ I(gdp ** 2.0) + I(policy_index ** 2.0)+I(females_education ** 2.0) + I(life_expectancy ** 2.0)+I(unemployment ** 2.0)+I(persons_prosecuted ** 3.0) + I(child_victims ** 3.0)+ I(gdp ** 3.0) + I(policy_index ** 3.0)+I(females_education ** 3.0) + I(life_expectancy ** 3.0)+I(unemployment ** 3.0)', data=df).fit()
print newpoly_3.summary()
plt.plot(x, newpoly_3.predict(X2), 'ro', label='New data added $R^2$=%.2f' % newpoly_3.rsquared, 
         alpha=0.9)

#plt.legend()
plt.savefig('figure_5.png')
plt.show()


