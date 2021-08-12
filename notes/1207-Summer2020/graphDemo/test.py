import networkx as nx
from graphNxUtils import nxWeightedGraphFromFile

g = nxWeightedGraphFromFile("./testCases/input007.txt")
nx.write_edgelist(g, "foo.txt")

h = nx.read_edgelist("foo.txt")

print(h)
