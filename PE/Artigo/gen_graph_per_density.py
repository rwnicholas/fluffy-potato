import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class DenseXGraph:
    G = None

    def __init__(self, p, n, low_interv = 10, high_interv = 1000):
        '''
            p: Representa a densidade do gráfico em porcentagem
            
            n: É o número de vértices

            low_interv: Valor mínimo do intervalo do peso das arestas

            high_interv: Valor máximo do intervalo do peso das arestas
        '''
        
        m = (n*(n-1)*p)/2
        
        self.G = nx.generators.random_graphs.dense_gnm_random_graph(n, np.rint(m))
        while not nx.is_connected(self.G):
            self.G = nx.generators.random_graphs.dense_gnm_random_graph(n, np.rint(m))
        
        for (u, v) in self.G.edges():
            self.G.edges[u,v]['weight'] = np.random.randint(low_interv, high_interv)

    def plot(self, figsize=(10, 15), label = True):
        plt.figure(figsize=figsize)
        
        pos=nx.spring_layout(self.G)
        nx.draw_networkx(self.G,pos)

        if label == True:
            labels = nx.get_edge_attributes(self.G,'weight')
            nx.draw_networkx_edge_labels(self.G,pos,edge_labels=labels)
        
        plt.show()
