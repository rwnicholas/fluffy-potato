#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

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

for groupKruskal, groupPrim in zip(itertools.islice(dataBox.groups, len(dataBox.groups)//2), itertools.islice(dataBox.groups, len(dataBox.groups)//2, len(dataBox.groups))):
    plt.boxplot([dataBox.get_group(groupKruskal)['tempo'], dataBox.get_group(groupPrim)['tempo']])
    plt.xticks([1,2], ['Kruskal', 'Prim'])
    plt.title("Algoritmo: " + str(groupKruskal[0]) + " | Nº Vertices: " + str(groupKruskal[1]) + " | Densidade: " + str(groupKruskal[2]) + "\n"
    "Algoritmo: " + str(groupPrim[0]) + " | Nº Vertices: " + str(groupPrim[1]) + " | Densidade: " + str(groupPrim[2])
    )
    plt.savefig("boxplot-tempo/" + "tempo"+ "_" + str(groupKruskal[1]) + "_" + str(groupKruskal[2]) + ".png")
    plt.close()

for groupKruskal, groupPrim in zip(itertools.islice(dataBox.groups, len(dataBox.groups)//2), itertools.islice(dataBox.groups, len(dataBox.groups)//2, len(dataBox.groups))):
    plt.boxplot([dataBox.get_group(groupKruskal)['memoria'], dataBox.get_group(groupPrim)['memoria']])
    plt.xticks([1,2], ['Kruskal', 'Prim'])
    plt.title("Algoritmo: " + str(groupKruskal[0]) + " | Nº Vertices: " + str(groupKruskal[1]) + " | Densidade: " + str(groupKruskal[2]) + "\n"
    "Algoritmo: " + str(groupPrim[0]) + " | Nº Vertices: " + str(groupPrim[1]) + " | Densidade: " + str(groupPrim[2])
    )
    plt.savefig("boxplot-memoria/" + "memoria"+ "_" + str(groupKruskal[1]) + "_" + str(groupKruskal[2]) + ".png")
    plt.close()
