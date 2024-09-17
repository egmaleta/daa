class Graph:
    def __init__(self, size: int):
        assert size >= 2
        self._mask = [
            [False for _ in range(size)]
            for _ in range(size)
        ]
    
    def _is_valid_edge(self, v: int, w: int):
        size = len(self._mask)
        return v != w and 0 <= v < size and 0 <= w < size
    
    def add_edge(self, v: int, w: int):
        assert self._is_valid_edge(v, w)
        self._mask[v][w] = True
        self._mask[w][v] = True

    def remove_edge(self, v: int, w: int):
        assert self._is_valid_edge(v, w)
        self._mask[v][w] = False
        self._mask[w][v] = False
    
    def edge_count(self):
        count = 0
        for v, mask in enumerate(self._mask):
            for has_edge in mask[v + 1:]:
                if has_edge:
                    count += 1
        return count


def sln(k: int, friendships: list[tuple[int, int]]):
    g = Graph(k)
    for v, w in friendships:
        g.add_edge(v, w)
    
    friendship_count = g.edge_count()
    possible = False

    def bt(g: Graph, v: int, w: int):
        raise NotImplementedError()

    bt(g, 0, 0)

    return possible
