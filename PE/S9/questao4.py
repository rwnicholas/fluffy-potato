#!/usr/bin/python3

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

data = pd.read_csv("data/dataset2.csv")

x = data[['j', 'bj']]
y = data['sbj']

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

plt.scatter(x['bj'], model.predict(x))
plt.show()
