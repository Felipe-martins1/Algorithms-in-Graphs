from lista_adjacencia import ListaAdjacencia;

def adiciona_pesos(graph: ListaAdjacencia, pesos: dict):
    adjacency_list = {}
    for edge in graph.graph:
        adjacency_list[edge] = [(adjacente, pesos.get((edge, adjacente))) for (adjacente) in graph.graph[edge]]

    return adjacency_list