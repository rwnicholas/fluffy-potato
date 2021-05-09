import gen_graph_per_density as gpd
import time

start_time = time.time()
graph = gpd.DenseXGraph(0.3, 10**4, 1, 100)
print("--- %s seconds ---" % (time.time() - start_time))
graph.plot(label=False)