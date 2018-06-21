from igraph import *

grafo = Graph()
grafo = grafo.Read_Ncol("saida.txt", names = True, directed = True, weights = False)

#plot(grafo, bbox = (0,0,2500,2500))
graph1 = grafo.community_infomap()
plot(graph1, bbox = (0,0,700,700), mark_groups = True)