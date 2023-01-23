
class ListaAdjacencia:
    def __init__(self, directed: bool = False):
        self.graph = {}
        self.directed = directed


    #Complexidade adiciona_vertice t(n) = 2 ou 1 -> O(1)
    def adiciona_vertice(self, vertice):
        if vertice not in self.graph:
            self.graph[vertice] = []

    #Complexidade remove_vertice -> O(n)
    def remove_vertice(self, vertice):
        if(self.vertice_existe(vertice)):
            for v in self.graph:
                if vertice in self.graph[v]:
                    self.graph[v].remove(vertice)
            del self.graph[vertice]
        else:
            raise Exception('Vertice não encontrado')
    
    #Complexidade adiciona_aresta -> O(1)
    def adiciona_aresta(self, vertice1, vertice2):
        if(self.aresta_pertence_ao_grafo(vertice1, vertice2)):
            raise Exception('Aresta já existe')

        if(vertice1 == vertice2):
            raise Exception('Não é possível criar uma aresta com um mesmo vértice')

        if vertice1 in self.graph and vertice2 in self.graph:
            self.graph[vertice1].append(vertice2)
            if not self.directed:
                self.graph[vertice2].append(vertice1)
        else:
            raise Exception('Vertice não encontrado')

    #Complexidade remove_aresta -> O(1) 
    def remove_aresta(self, vertice1, vertice2):
        if(self.aresta_pertence_ao_grafo(vertice1, vertice2)):
            self.graph[vertice1].remove(vertice2)
            if not self.directed:
                self.graph[vertice2].remove(vertice1)
        else:
            raise Exception('Aresta não encontrada')  

    def lista_adjacencia(self):
        return self.graph

    def vertice_existe(self, vertice):
        return vertice in self.graph 

    def aresta_pertence_ao_grafo(self, vertice1, vertice2):
        return vertice2 in self.graph[vertice1]

    #Complexidade busca_vertices_adjacentes -> O(1) 
    def busca_vertices_adjacentes(self, vertice):
        return self.graph[vertice]

    #Complexidade busca_vertices_inscidentes -> O(n) 
    def busca_vertices_inscidentes(self, vertice):
        vertices = []
        for v in self.graph:
            if vertice in self.graph[v]:
                vertices.append(v)
        return vertices

    #Complexidade busca_aresta_complemento -> O(1) 
    def busca_aresta_complemento(self, complemento, vertice1, vertice2):
        pertence_grafo = self.aresta_pertence_ao_grafo(vertice1, vertice2)
        pertence_complemento = complemento.aresta_pertence_ao_grafo(vertice1, vertice2)

        if(not pertence_grafo and not pertence_complemento):
            return vertice1, vertice2
        
        pertence_grafo = self.aresta_pertence_ao_grafo(vertice2, vertice1)
        pertence_complemento = complemento.aresta_pertence_ao_grafo(vertice2, vertice1)

        if(not pertence_grafo and not pertence_complemento):
            return vertice2, vertice1
        
        return None, None
        
    #Complexidade grafo_complemento -> O(n^3) 
    def grafo_complemento(self):
        complemento = ListaAdjacencia(self.directed)
        for v in self.graph:
            complemento.adiciona_vertice(v)
        for vertice1 in self.graph:
            for vertice2 in self.graph:
                if(vertice1 != vertice2):
                    vertice_complemento1, vertice_complemento2 = self.busca_aresta_complemento(complemento, vertice1, vertice2)
                    while(vertice_complemento1 != None and vertice_complemento2 != None):
                        complemento.adiciona_aresta(vertice_complemento1, vertice_complemento2)
                        vertice_complemento1, vertice_complemento2 = self.busca_aresta_complemento(complemento, vertice1, vertice2)
        return complemento

    #Complexidade grafo_transposto -> O(n^2)
    def grafo_transposto(self):
        if(self.directed == False):
            raise Exception('Grafo não direcionado')

        transposto = ListaAdjacencia(self.directed)
        for v in self.graph:
            transposto.adiciona_vertice(v)
        for v in self.graph:
            for adjacente in self.graph[v]:
                transposto.adiciona_aresta(adjacente, v)
        return transposto

    #Complexidade matriz_adjacencia -> O(n^2)
    def matriz_adjacencia(self):
        matriz = []
        for vertice in self.graph:
            linha = []
            for vertice2 in self.graph:
                if(self.aresta_pertence_ao_grafo(vertice, vertice2)):
                    linha.append(1)
                else:
                    linha.append(0)
            matriz.append(linha)
        return matriz
    
    #Complexidade print_matriz_adjacencia -> O(n^2)
    def print_matriz_adjacencia(self, matriz: list):
        print('\n' + '-------------------------', end='\n\n', )
        print('Matriz de Adjacencia: ', end='\n\n')
        
        end_separator = ' | '
        start_separator = ' |'
        left_padding = ' ' * (len(end_separator) + 1)

        print(end=left_padding)
        for v in self.graph:
            print(start_separator, v, end=end_separator)
        print('\n')
        for index_linha, linha in enumerate(matriz):
            vertice = list(self.graph.keys())[index_linha]
            print(vertice, end=end_separator)
            for coluna in linha:
                print(start_separator, coluna, end=end_separator)
            print('\n')
        print('-------------------------', end='\n\n')

    #Complexidade print_graph -> O(n^2)
    def print_graph(self): 
        print('\n' + '-------------------------', end='\n\n', )
        print('Lista de Adjacencia: ', end='\n\n')
        for vertice in self.graph:
            print(vertice, '->', end=' ')
            for adjacente in self.graph[vertice]:
                isLast = adjacente == self.graph[vertice][-1]
                print(adjacente, end=' ' if isLast else ' -> ')
            print('\n')
        print('-------------------------', end='\n\n')
        
        
        
