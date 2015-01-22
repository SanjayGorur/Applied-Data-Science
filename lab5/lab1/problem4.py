##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 1                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.4                                  #
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

df = pd.read_csv("cleaned_data_log.csv")
x=  df[["gdp","policy_index","females_education","life_expectancy","persons_prosecuted","child_victims"]]
y = df[['Adult_victims']]
X = sm.add_constant(x)


#figure prep
plt.figure()
plt.scatter(x.gdp,y, s=10, alpha=0.3)
plt.scatter(x.policy_index,y, s=10, alpha=0.3)
plt.scatter(x.life_expectancy,y, s=10, alpha=0.3)
plt.scatter(x.persons_prosecuted,y, s=10, alpha=0.3)
plt.scatter(x.child_victims,y, s=10, alpha=0.3)
plt.scatter(x.females_education,y, s=10, alpha=0.3)
plt.ylim([-5,30])
plt.xlabel('all predictors')
plt.ylabel('Adult victim')

#OLS
linear = sm.OLS(y, X).fit()
print linear.summary()
plt.plot(x, linear.predict(X), 'g+')

# 2-nd order polynomial
poly_2 = smf.ols(formula='Adult_victims~ 1 + persons_prosecuted + child_victims+ gdp+ policy_index+ females_education + life_expectancy+I(persons_prosecuted ** 2.0) + I(child_victims ** 2.0)+ I(gdp ** 2.0) + I(policy_index ** 2.0)+I(females_education ** 2.0) + I(life_expectancy ** 2.0)', data=df).fit()
#print poly_2.summary()
plt.plot(x, poly_2.predict(X), 'ro', label='Poly n=2 $R^2$=%.2f' % poly_2.rsquared, 
         alpha=0.9)

# 3-rd order polynomial
poly_3 = smf.ols(formula='Adult_victims~ 1 + persons_prosecuted + child_victims+ gdp+ policy_index+ females_education + life_expectancy+I(persons_prosecuted ** 2.0) + I(child_victims ** 2.0)+ I(gdp ** 2.0) + I(policy_index ** 2.0)+I(females_education ** 2.0) + I(life_expectancy ** 2.0)+I(persons_prosecuted ** 3.0) + I(child_victims ** 3.0)+ I(gdp ** 3.0) + I(policy_index ** 3.0)+I(females_education ** 3.0) + I(life_expectancy ** 3.0)', data=df).fit()
print poly_3.summary()
plt.plot(x, poly_3.predict(X), 'go', label='Poly n=3 $R^2$=%.2f' % poly_3.rsquared, 
         alpha=0.9)

plt.savefig('figure_4.png')
#plt.show()


