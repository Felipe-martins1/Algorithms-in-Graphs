from lista_adjacencia import ListaAdjacencia



with open('graph.txt') as f:
    lines = f.readlines()
    directed = lines[0].strip() == 'directed'
    graph = ListaAdjacencia(directed)
    for line in lines[1:]:
        vertex1, vertex2 = line.strip().split(' ')
        graph.adiciona_vertice(vertex1)
        graph.adiciona_vertice(vertex2)
        graph.adiciona_aresta(vertex1, vertex2)
    graph.print_graph()
    

    
       