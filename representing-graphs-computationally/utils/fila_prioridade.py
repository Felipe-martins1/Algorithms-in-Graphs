class FilaPrioridade:
    def __init__(self):
        self.fila = []

    def __len__(self):
        return len(self.fila)

    def __str__(self):
        return str(self.fila)

    def inserir(self, item):
        self.fila.append(item)

    def remover(self):
        if len(self.fila) == 0:
            return None
        else:
            minimo = self.fila[0]
            (custoMin, verticeMin) = minimo
            for i in range(1, len(self.fila)):
                (custo, vertice) = self.fila[i]
                if custo < custoMin:
                    minimo = self.fila[i]
            self.fila.remove(minimo)
            return minimo