from utils.init_distancias import init_distancias
from utils.relax import relax

def bellman_ford(grafo, origem):
    (distancias, predecessores) = init_distancias(grafo, origem)
    
    for i in range(len(grafo)-1):
        for vertice in grafo:
            for adjacente, peso in grafo[vertice]:
                relax(distancias, predecessores, vertice, adjacente, peso)
    
    for vertice in grafo:
        for adjacente, peso in grafo[vertice]:
            if distancias[vertice] + peso < distancias[adjacente]:
                return False
    
    return True