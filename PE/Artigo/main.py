import gen_graph_per_density as gpd
import time
import networkx as nx
import matplotlib.pyplot as plt

start_time = time.time()
graph = gpd.DenseXGraph(1, 10**2, 1, 100)
print("--- %s seconds ---" % (time.time() - start_time))
graph.export("teste.gexf")

n_var = [250, 500, 1000, 10000]
probab = [0.3, 0.6, 0.9, 1]

for p in probab:
    for n in n_var:
        tmp_graph = gpd.DenseXGraph(p, n)
        tmp_graph.export("graphs/graph_p_" + p + "_n_" + n + ".gexf")