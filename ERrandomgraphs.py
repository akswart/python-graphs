import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


n = 10  # 10 nodes
p = .2 # prob of .1

G1 = nx.gnp_random_graph(n, p)



nx.draw(G1)
plt.show()