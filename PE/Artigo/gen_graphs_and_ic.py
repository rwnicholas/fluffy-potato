#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 'tempo' in seconds
# 'memoria' in megabytes

data = pd.read_csv("data/result.csv", dtype={
    'ensaio': np.float64, 'densidade': np.float64,
    'tempo': np.float64, 'memoria': np.float64
})

# print(data.head())
dataMean = data.groupby(['nvertices', 'densidade', 'algoritmo']).mean().drop(columns="ensaio")

# dataMean.loc[dataMean['algoritmo'] == "kruskal"].plot.scatter(x='densidade', y='tempo')
# plt.savefig('teste.png')