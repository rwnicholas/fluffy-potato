#!/usr/bin/python3
from numpy.core.defchararray import title
import pandas as pd
from pandas.plotting import lag_plot
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

# 'tempo' in seconds
# 'memoria' in megabytes

data = pd.read_csv("data/result.csv", dtype={
    'nvertices': np.float64, 'densidade': np.float64,
    'tempo': np.float64, 'memoria': np.float64
})

dataBox = data.groupby(['algoritmo','densidade','nvertices']).mean().drop(columns='ensaio')

# dataBox.get_group('kruskal').plot.scatter(x='tempo', y='densidade')
# # dataBox.plot.scatter(x='tempo', y='ensaio')
data = data.drop(columns='ensaio')

lnmodel = LinearRegression()
vizualizer = ResidualsPlot(lnmodel, qqplot=True, hist=False, train_color='r', title="Residuais x Tempo")
vizualizer.fit(data[['nvertices','densidade']], data['tempo'])
vizualizer.show(outpath='residuais_tempo.png')

