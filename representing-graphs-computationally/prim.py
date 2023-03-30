import heapq

def prim(graph, start: str):
    vertices_visitados = []
    arestas_arvore_g_minima = {}
    arestas = [(0, start)]

    heapq.heapify(arestas)

    while arestas:
        peso, vertice = heapq.heappop(arestas)

        if vertice in vertices_visitados:
            continue
        
        vertices_visitados.append(vertice)

        if(vertice != start):
            arestas_arvore_g_minima[vertice] = peso

        for adjacente, peso in graph[vertice]:
            if adjacente not in vertices_visitados:
                heapq.heappush(arestas, (peso, adjacente))

    return arestas_arvore_g_minima

