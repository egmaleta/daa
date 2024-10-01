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
