import numpy as np

import statsmodels.api as sm

import statsmodels.formula.api as smf

import pandas as pd
import plotnine as p9

data = pd.read_csv("beauty.csv")
print(data)
results = smf.ols('courseevaluation~btystdave+age+beautyflowerdiv+beautyfupperdiv+beautymlowerdiv', data=data).fit()
wyn = results.params
print(results.summary())
fig3 = (p9.ggplot(p9.aes(x='btystdave',y='age', color='courseevaluation'), data=data)
        + p9.geom_point())

print(fig3)
data['courseevaluation_predict'] = results.predict()


data['residuals'] = data['courseevaluation'] - data['courseevaluation_predict']

fig3_res = (p9.ggplot(p9.aes(x='btystdave',y='age', color='residuals'), data=data)
            + p9.geom_point())
print(fig3_res)

