
import statsmodels.formula.api as smf

import pandas as pd
import plotnine as p9

data = pd.read_csv("excercise1.csv")
shortData = data.head(40)
print(data)
results = smf.ols('y~x2+x1', data=shortData).fit()
wyn = results.params
print(results.summary())
fig3 = (p9.ggplot(p9.aes(x='x1', y='x2', color='y'), data=shortData)
        + p9.geom_point())

print(fig3)
shortData['y_predict'] = results.predict()

fig3_res = (p9.ggplot(p9.aes(x='x1', y='x2', color='y_predict'), data=shortData)
            + p9.geom_point())
print(fig3_res)

shortData['residuals'] = shortData['y'] - shortData['y_predict']

fig3_res = (p9.ggplot(p9.aes(x='x1', y='x2', color='residuals'), data=shortData)
            + p9.geom_point())
print(fig3_res)

pred = data.tail(20)
pred['y'] = results.predict(pred)
fig4 = (p9.ggplot(p9.aes(x='x1', y='x2', color='y'), data=pred)
            + p9.geom_point())
print(fig4)
