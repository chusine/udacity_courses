import math

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Make an empty graph
a_ring = {}

n = 5

# Add in the edges
for i in range(n):
    make_link(a_ring, i, (i+1) % n)

# How many nodes?
print(len(a_ring))

# How many edges?
print(sum([len(a_ring[node]) for node in a_ring.keys()]) / 2)

print(a_ring)

# 5 Quiz: Grid Network. How many edges are in a graph with 256 nodes?
G = {}

n = 256
side = int(math.sqrt(n))

# Add in the edges
for i in range(side):
    for j in range(side):
        if i < side - 1: make_link(G, (i, j), (i + 1, j))
        if j < side - 1: make_link(G, (i, j), (i, j + 1))

# How many nodes?
print(len(G))

# How many edges?
print(sum([len(G[node]) for node in G.keys()]) / 2)
