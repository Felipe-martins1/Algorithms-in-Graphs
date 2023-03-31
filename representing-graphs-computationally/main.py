#ALUNOS:

#Felipe Domiciano Martins RA: 123959
#Gabriel Sossai Soares RA: 125475

from lista_adjacencia import ListaAdjacencia
from prim import prim
from kruskal import kruskal
from dijkstra import dijkstra
from floyd_warshal import floyd_warshall
from bellman_ford import bellman_ford

from utils.print_matrix_floyd_warshall import print_matrix_floyd_warshall

from utils.adiciona_pesos import adiciona_pesos

with open('grafo_com_pesos.txt') as f:
    lines = f.readlines()
    directed = lines[0].strip() == 'directed'
    graph = ListaAdjacencia(directed)
    pesos = {}

    for line in lines[1:]:
        vertex1, vertex2, peso = line.strip().split(' ')
        graph.adiciona_vertice(vertex1)
        graph.adiciona_vertice(vertex2)
        graph.adiciona_aresta(vertex1, vertex2)
        pesos[(vertex1, vertex2)] = int(peso)
        if(not directed):
            pesos[(vertex2, vertex1)] = int(peso)
    grafo_com_pesos = adiciona_pesos(graph, pesos);
    
    print('\n---------PRIM--------\n');
    aresta_minima = prim(grafo_com_pesos, 'a');
    print(aresta_minima);
    
    print('\n---------KRUSKAL--------\n');
    aresta_minima = kruskal(grafo_com_pesos);
    print(aresta_minima);

    print('\n---------DIJKSTRA--------\n');
    caminho_minimo = dijkstra(grafo_com_pesos, 'a');
    print(caminho_minimo);

    print('\n---------BELLMAN FORD--------\n');
    caminho_minimo = bellman_ford(grafo_com_pesos, 'a');
    print(caminho_minimo);

    print('\n---------FLOYD WARSHALL--------\n');
    caminho_minimo = floyd_warshall(grafo_com_pesos);
    print_matrix_floyd_warshall(grafo_com_pesos, caminho_minimo);

    print('\n')
    
    

    

    
       