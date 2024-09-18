import heapq

class Grafo:
    def __init__(self) -> None:
        self.grafo = {}

    def agragar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.agragar_vertice(origen)
        if destino not in self.grafo:
            self.agragar_vertice(destino)

        self.grafo[origen][destino] = peso
        


def dijkstra(grafo, inicio):
    # Inicializar estructuras 
    distancias = {vertice: float('inf') for vertice in grafo.grafo}
    distancias[inicio] = 0
    prioridad = [(0,inicio)] # (distancia, vertice)
    caminos = {vertice: None for vertice in grafo.grafo}

    while prioridad:
        distancia_actual, vertice_actual = heapq.heappop(prioridad)

        if distancia_actual > distancias[vertice_actual]:
            continue 

        for vecino,peso in grafo.grafo[vertice_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino]= distancia
                caminos[vecino] = vertice_actual
                heapq.heappush(prioridad, (distancia, vecino))

    return distancias, caminos

def reconstruir_camino(self, inicio, destino, caminos):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = caminos[actual]
    camino.reverse()
    return camino if camino[0] == inicio else None






