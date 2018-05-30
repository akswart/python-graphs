
import sys
import numpy as np
import matplotlib.pyplot as plt
from networkx import nx

n = 10  # 10 nodes
p = .2  # 20 edges
p2 = 2*np.log(n)/n

G = nx.gnp_random_graph(n, p2)

# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print('%s %d %f' % (v, nx.degree(G, v), nx.clustering(G, v)))

# print the adjacency list to terminal
try:
    nx.write_adjlist(G, sys.stdout)
except TypeError:  # Python 3.x
    nx.write_adjlist(G, sys.stdout.buffer)

nx.draw(G)
plt.show()