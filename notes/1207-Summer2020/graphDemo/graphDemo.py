import networkx as nx
from network2tikz import plot
from graphNxUtils import nxWeightedGraphFromFile 
from collections import deque 
  
#https://networkx.github.io/documentation/stable/tutorial.html
#https://pypi.org/project/network2tikz/

g = nxWeightedGraphFromFile("./testCases/input007.txt")

#print(g.edges.data())

#requires matlibplot: nx.draw(g)
style = {}
style['node_label'] = [str(x) for x in g.nodes]
style['edge_curved'] = 0
style['layout'] = 'fruchterman_reingold'
style['edge_label'] = [wt for (x,y,wt) in g.edges.data('weight')]
plot(g,'mygraph.tex',**style)

#now the real fun begins...

# Let's write a function that:
# given a graph G, two vertices, a, b returns
# a path from a to be if one exists
# let's adapt DFS to solve this problem

def findPath(g, a, b):
  """
  Finds a path in the graph g from the vertex a
  to the vertex b if one exists.  No conditions
  (shortest distance or weighted path) are placed
  on the resulting path.  Returns None if no such
  path exists
  """
  #maps verticies to strings for their status
  # including "unvisited", "visited", "processed"
  status = {x:"unvisited" for x in g.nodes}
  s = [] # my stack: append or pop
  s.append(a)
  status[a] = "visited"
  while len(s) > 0:
    curr = s[-1]
    # check if you've found b:
    if curr == b:
      return s
    # select the next vertex to visit...
    next = None
    #print("curr = " + str(curr))
    for y in g.neighbors(curr):
      if status[y] == "unvisited":
        next = y
        break
    if next is None:
      #done with curr, need to backtrack    
      s.pop()
      status[curr] = "processed"
    else:
      # go to the *next* vertex:
      status[next] = "visited"
      s.append(next)
  return None


def bfsTree(g, a):
  """
  returns a BFS tree resulting from one BFS 
  run starting at vertex a
  """
  t = nx.Graph()
  t.add_nodes_from(range(len(g.nodes)))
  q = deque() #popleft(), append()
  #maps verticies to strings for their status
  # including "unvisited", "visited", "processed"
  status = {x:"unvisited" for x in g.nodes}
  #start with a:
  status[a] = "visited"
  q.append(a)
  while len(q) > 0:
    curr = q.popleft()
    for y in g.neighbors(curr):
      if status[y] == "unvisited":
        status[y] = "visited"
        q.append(y)
        # add the edge from curr to y to the BFS tree
        t.add_edge(curr, y, weight=g[curr][y]['weight'])
    status[curr] = "processed"
  return t



t = bfsTree(g, 0)
plot(t,'mytree.tex',**style)



