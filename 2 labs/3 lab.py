import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
P0= [[0, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 0, 1],
 [1, 1, 0, 1, 0, 1],
 [0, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 0, 1],
 [1, 1, 1, 1, 1, 0]]

G = nx.DiGraph(np.matrix(P0))
nx.draw(G, with_labels=True, node_size=300, arrows=True)
plt.show()