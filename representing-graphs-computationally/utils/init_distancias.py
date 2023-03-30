def init_distancias(graph, origem):
    distancias = {}
    predecessores = {}
    for vertice in graph:
        distancias[vertice] = float('inf')
        predecessores[vertice] = None
    distancias[origem] = 0
    return (distancias, predecessores)