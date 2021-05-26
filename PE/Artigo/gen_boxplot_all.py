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

dataVertices = data.drop(columns="densidade").groupby(['algoritmo', 'nvertices'])
dataDensidade = data.drop(columns="nvertices").groupby(['algoritmo', 'densidade'])


for groupKruskal, groupPrim in zip(itertools.islice(dataVertices.groups, len(dataVertices.groups)//2), itertools.islice(dataVertices.groups, len(dataVertices.groups)//2, len(dataVertices.groups))):
    plt.boxplot([dataVertices.get_group(groupKruskal)['tempo'], dataVertices.get_group(groupPrim)['tempo']])
    plt.xticks([1,2], ['Kruskal', 'Prim'])
    plt.title("Algoritmo: " + str(groupKruskal[0]) + " | Nº Vertices: " + str(groupKruskal[1]) + "\n"
    "Algoritmo: " + str(groupPrim[0]) + " | Nº Vertices: " + str(groupPrim[1]))
    plt.ylabel("Segundos")
    plt.savefig("boxplot-tempo/" + "tempo"+ "_" + str(groupKruskal[0]) + "_vertices_" + str(groupKruskal[1]) + ".png")
    plt.close()

for groupKruskal, groupPrim in zip(itertools.islice(dataVertices.groups, len(dataVertices.groups)//2), itertools.islice(dataVertices.groups, len(dataVertices.groups)//2, len(dataVertices.groups))):
    plt.boxplot([dataVertices.get_group(groupKruskal)['memoria'], dataVertices.get_group(groupPrim)['memoria']])
    plt.xticks([1,2], ['Kruskal', 'Prim'])
    plt.title("Algoritmo: " + str(groupKruskal[0]) + " | Nº Vertices: " + str(groupKruskal[1]) + "\n"
    "Algoritmo: " + str(groupPrim[0]) + " | Nº Vertices: " + str(groupPrim[1]))
    plt.ylabel("Megabytes")
    plt.savefig("boxplot-memoria/" + "memoria"+ "_" + str(groupKruskal[0]) + "_vertices_" + str(groupKruskal[1]) + ".png")
    plt.close()

for groupKruskal, groupPrim in zip(itertools.islice(dataDensidade.groups, len(dataDensidade.groups)//2), itertools.islice(dataDensidade.groups, len(dataDensidade.groups)//2, len(dataDensidade.groups))):
    plt.boxplot([dataDensidade.get_group(groupKruskal)['tempo'], dataDensidade.get_group(groupPrim)['tempo']])
    plt.xticks([1,2], ['Kruskal', 'Prim'])
    plt.title("Algoritmo: " + str(groupKruskal[0]) + " | Densidade: " + str(groupKruskal[1]) + "\n"
    "Algoritmo: " + str(groupPrim[0]) + " | Densidade: " + str(groupPrim[1]))
    plt.ylabel("Segundos")
    plt.savefig("boxplot-tempo/" + "tempo"+ "_" + str(groupKruskal[0]) + "_densidade_" + str(groupKruskal[1]) + ".png")
    plt.close()

for groupKruskal, groupPrim in zip(itertools.islice(dataDensidade.groups, len(dataDensidade.groups)//2), itertools.islice(dataDensidade.groups, len(dataDensidade.groups)//2, len(dataDensidade.groups))):
    plt.boxplot([dataDensidade.get_group(groupKruskal)['memoria'], dataDensidade.get_group(groupPrim)['memoria']])
    plt.xticks([1,2], ['Kruskal', 'Prim'])
    plt.title("Algoritmo: " + str(groupKruskal[0]) + " | Densidade: " + str(groupKruskal[1]) + "\n"
    "Algoritmo: " + str(groupPrim[0]) + " | Densidade: " + str(groupPrim[1]))
    plt.ylabel("Megabytes")
    plt.savefig("boxplot-memoria/" + "memoria"+ "_" + str(groupKruskal[0]) + "_densidade_" + str(groupKruskal[1]) + ".png")
    plt.close()