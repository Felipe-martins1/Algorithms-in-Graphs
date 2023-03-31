from utils.union_set import UnionSet;

def sort_arestas_by_peso(graph):
    arestas = []
    for vertice in graph:
        for adjacente, peso in graph[vertice]:
            arestas.append((peso, vertice, adjacente))
    arestas.sort()
    return arestas

def kruskal(graph):
    arvore_g_minima = []
    union_set = UnionSet()

    for vertice in graph:
        union_set.makeSet(vertice)

    arestas = sort_arestas_by_peso(graph)

    for peso, vertice, adjacente in arestas:
        if union_set.findSet(vertice) != union_set.findSet(adjacente):
            arvore_g_minima.append((vertice, adjacente, peso))
            union_set.union(vertice, adjacente)

    return arvore_g_minima