from math import inf


def create_vertex_map(adj_list):
    vertice_map = {}
    i = 0
    for vertice in adj_list:
        if vertice not in vertice_map:
            vertice_map[vertice] = i
            i += 1
        for adjacente, _ in adj_list[vertice]:
            if adjacente not in vertice_map:
                vertice_map[adjacente] = i
                i += 1
    return vertice_map

def floyd_warshall(graph):
    vertice_map = create_vertex_map(graph)
    n = len(vertice_map)
    
    dist = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for vertice in graph:
        i = vertice_map[vertice]
        for adjacente, peso in graph[vertice]:
            j = vertice_map[adjacente]
            dist[i][j] = peso 
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
   