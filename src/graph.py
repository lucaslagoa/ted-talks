from igraph import *

grafo = Graph()
grafo = grafo.Read_Ncol("saidaGraph.txt", names = True, directed = True, weights = False)
name = grafo.vs['name']
graph1 = grafo.community_infomap()
plot(graph1, bbox = (800,800),mark_groups = True,vertex_label = name)