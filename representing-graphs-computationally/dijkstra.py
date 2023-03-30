from utils.fila_prioridade import FilaPrioridade
from utils.init_distancias import init_distancias
from utils.relax import relax

def dijkstra(grafo, origem):
    (distancias, predecessores) = init_distancias(grafo, origem)
    fila = FilaPrioridade()
    fila.inserir((0, origem))
    visitados = []

    while fila:
        
        distancia_atual, vertice_atual = fila.remover()
        
        if vertice_atual in visitados:
            continue
       
        visitados.append(vertice_atual)
       
        for adjacente, peso in grafo[vertice_atual]:
            relaxResult = relax(distancias, predecessores, vertice_atual, adjacente, peso)
            if relaxResult:
                fila.inserir((distancias[adjacente], adjacente))

    return distancias