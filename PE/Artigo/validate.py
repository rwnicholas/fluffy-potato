#!/usr/bin/python3
import pandas as pd
from pandas.plotting import lag_plot
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 'tempo' in seconds
# 'memoria' in megabytes

data = pd.read_csv("data/result.csv", dtype={
    'nvertices': np.float64, 'densidade': np.float64,
    'tempo': np.float64, 'memoria': np.float64
})

dataBox = data.groupby(['algoritmo','densidade','nvertices']).mean().drop(columns='ensaio')

# dataBox.get_group('kruskal').plot.scatter(x='tempo', y='densidade')
# # dataBox.plot.scatter(x='tempo', y='ensaio')

model = ols('memoria ~ nvertices + densidade + algoritmo', data=data).fit()
print(model.summary())
fig = plt.figure(figsize=(12,8))

obj = 'algoritmo[T.prim]'

fig = sm.graphics.plot_regress_exog(model, obj,fig=fig)
plt.savefig(obj+'_memoria.png')
plt.close()
