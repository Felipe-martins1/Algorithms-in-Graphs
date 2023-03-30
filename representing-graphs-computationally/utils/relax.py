def relax(distancias, predecessores, vertice, adjacente, w):
    distancia_vizinho = distancias[vertice] + w
    if distancias[adjacente] > distancia_vizinho:
        distancias[adjacente] = distancia_vizinho
        predecessores[adjacente] = vertice
        return True
    return False