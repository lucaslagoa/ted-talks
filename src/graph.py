from igraph import *

grafo = Graph()
grafo = grafo.Read_Ncol("saida.txt", names = True, directed = True, weights = False)

plot(grafo)