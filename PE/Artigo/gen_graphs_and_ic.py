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
# dataMean = data.groupby(['algoritmo', 'nvertices', 'densidade']).mean().drop(columns="ensaio")

# for y_,head in zip(dataMean['tempo'], dataMean['tempo'].axes[0]):
#     plt.boxplot([y_])
#     plt.title("Algoritmo: " + str(head[0]) + " | Nº Vertices: " + str(head[1]) + " | Densidade: " + str(head[2]))
#     plt.show()

dataBox = data.groupby(['algoritmo', 'nvertices', 'densidade'])

for group in dataBox.groups:
    plt.boxplot(dataBox.get_group(group)['tempo'])
    plt.title("Algoritmo: " + str(group[0]) + " | Nº Vertices: " + str(group[1]) + " | Densidade: " + str(group[2]))
    plt.savefig("boxplot-tempo/" + str(group[0]) + "_" + str(group[1]) + "_" + str(group[2]) + "_tempo"+ ".png")
    plt.close()

for group in dataBox.groups:
    plt.boxplot(dataBox.get_group(group)['memoria'])
    plt.title("Algoritmo: " + str(group[0]) + " | Nº Vertices: " + str(group[1]) + " | Densidade: " + str(group[2]))
    plt.savefig("boxplot-memoria/" + str(group[0]) + "_" + str(group[1]) + "_" + str(group[2]) + "_memoria"+ ".png")
    plt.close()