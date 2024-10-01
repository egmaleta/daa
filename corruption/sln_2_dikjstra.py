import heapq

from .grafo import Grafo


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

def reconstruir_camino(inicio, destino, caminos):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = caminos[actual]
    camino.reverse()
    return camino if camino[0] == inicio else None


def solver(grafo):
    long_de_caminos = {vertice: {} for vertice in grafo.grafo}
    for v in grafo.grafo.keys():
        distancias,caminos = dijkstra(grafo,v)

        for w in grafo.grafo.keys():
            if v != w:
                camino_de_v_a_w = reconstruir_camino(v,w,caminos)
                if camino_de_v_a_w != None:
                    long_de_caminos[v][w] = len(camino_de_v_a_w)  -1

    return long_de_caminos    


# testing

grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 4)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('B', 'D', 5)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista("D", "C", 10)
grafo.agregar_arista("D", "A", 3)

# distancias, caminos = dijkstra(grafo,'B')
# print("Distancias:", distancias)
# print("Caminos:", caminos)

# camino = reconstruir_camino('B', 'C', caminos)
# print("Camino de A a D:", camino)

result = solver(grafo)
print(result)
