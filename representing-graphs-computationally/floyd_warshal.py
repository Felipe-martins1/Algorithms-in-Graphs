from math import inf

def create_vertex_map(adj_list):
    vertex_map = {}
    i = 0
    for vertex in adj_list:
        if vertex not in vertex_map:
            vertex_map[vertex] = i
            i += 1
        for neighbor, weight in adj_list[vertex]:
            if neighbor not in vertex_map:
                vertex_map[neighbor] = i
                i += 1
    return vertex_map

def floyd_warshall(graph):
    vertex_map = create_vertex_map(graph)
    n = len(vertex_map)
    
    dist = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for vertex in graph:
        i = vertex_map[vertex]
        for neighbor, weight in graph[vertex]:
            j = vertex_map[neighbor]
            dist[i][j] = weight
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
   