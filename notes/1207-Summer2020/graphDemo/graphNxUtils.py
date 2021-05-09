import sys
import networkx as nx

def nxGraphFromFile(fileName):
    """
    Parses a text file representation of a graph and
    produces a NetworkX (nx) graph instance of an
    undirected graph.  
    
    The format of the file is as follows:
     - first line: n, the number of vertices in G
     - each line after is an adjacency list - an initial 
       vertex followed by a space-delimited list of
       vertices it is incident on
    
    See https://networkx.github.io/documentation
    """
    g = nx.Graph()
    try:
        lines = open(fileName,'r').readlines()
    except FileNotFoundError:
        sys.stderr.write("File not found: " + fileName + "\n")
        return g
    n = int(lines[0].strip())
    g.add_nodes_from(range(n))
    for x in range(n):
        line = lines[x+1]
        tokens = line.strip().split(" ")
        for y in tokens[1:]:
            g.add_edge(x,int(y))
    return g.to_undirected()

def nxWeightedGraphFromFile(fileName):
    """
    Parses a text file representation of a graph and
    produces a NetworkX (nx) graph instance of an
    undirected graph with edge weights (stored as
    attributes on edges).  
    
    The format of the file is as follows:
     - first line: n, the number of vertices in G
     - each line after is a space-delimited triple
       representing an edge: two vertices followed 
       by the weight of the edge
    
    See https://networkx.github.io/documentation
    """
    g = nx.Graph()
    try:
        lines = open(fileName,'r').readlines()
    except FileNotFoundError:
        sys.stderr.write("File not found: " + fileName + "\n")
        return g
    n = int(lines[0].strip())
    g.add_nodes_from(range(n))
    for line in lines[1:]:
        tokens = line.strip().split(" ")
        if len(tokens) == 3:
          g.add_edge(int(tokens[0]),int(tokens[1]),weight=float(tokens[2]))
    return g.to_undirected()

