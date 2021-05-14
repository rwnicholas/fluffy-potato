import gen_graph_per_density as gpd
import time
import networkx as nx
import matplotlib.pyplot as plt

n_var = [250, 500, 1000, 10000]
probab = [0.3, 0.6, 0.9, 1]

for i in range(1,11):
    for p in probab:
        for n in n_var:
            tmp_graph = gpd.DenseXGraph(p, n)
            tmp_graph.export("graphs/graph_i_" + str(i) + "_p_" + str(p) + "_n_" + str(n) + ".yaml")