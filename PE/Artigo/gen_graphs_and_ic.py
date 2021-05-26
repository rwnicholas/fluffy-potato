#!/usr/bin/python3
import pandas as pd
import numpy as np

# 'tempo' in seconds
# 'memoria' in megabytes

data = pd.read_csv("data/result.csv", dtype={
    'ensaio': np.float64, 'densidade': np.float64,
    'tempo': np.float64
})

print(data.head())
# data.loc[data['algoritmo'] == "kruskal"].plot(x='ensaio', y='tempo')
# print(data.loc[data['algoritmo'] == "kruskal"])