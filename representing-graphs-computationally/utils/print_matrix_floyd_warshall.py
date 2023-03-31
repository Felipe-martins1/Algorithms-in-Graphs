def print_matrix_floyd_warshall(graph, caminho_minimo):
    print("     ", end="")
    print(" ".join(f"{vertice:3}" for vertice in graph))
    print("")
    for i, row in enumerate(caminho_minimo):
        print(f"{list(graph.keys())[i]:3}", end="")
        print(" ".join(f"{x:3}" for x in row))