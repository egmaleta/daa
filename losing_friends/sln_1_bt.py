class Graph:
    def __init__(self, size: int):
        assert size >= 2
        self._mask = [
            [False for _ in range(size)]
            for _ in range(size)
        ]
    
    def _is_valid_vertex(self, v: int):
        return 0 <= v < len(self._mask)
    
    def _is_valid_edge(self, v: int, w: int):
        return v != w and self._is_valid_vertex(v) and self._is_valid_vertex(w)
    
    def add_edge(self, v: int, w: int):
        assert self._is_valid_edge(v, w)
        self._mask[v][w] = True
        self._mask[w][v] = True

    def remove_edge(self, v: int, w: int):
        assert self._is_valid_edge(v, w)
        self._mask[v][w] = False
        self._mask[w][v] = False
    
    def edges(self, v: int):
        assert self._is_valid_vertex(v)
        return [w for w, has_edge in enumerate(self._mask[v]) if has_edge]
    
    def edge_count(self):
        count = 0
        for v, mask in enumerate(self._mask):
            for has_edge in mask[v + 1:]:
                if has_edge:
                    count += 1
        return count
    
    def vertices(self):
        return [v for v in range(len(self._mask))]
    
    def traverse(self, v_start: int, w_start: int):
        for v, mask in enumerate(self._mask[v_start:], start=v_start):
            if v > v_start:
                # continue traversing matrix normally
                w_start = v + 1
            
            for w, has_edge in enumerate(mask[w_start:], start=w_start):
                yield v, w, has_edge


class _SlnFound(Exception):
    pass


def bt(g: Graph, v_start: int, w_start: int, friendship_count: int):
    if friendship_count == 0:
        return
    
    edges_list = [g.edges(v) for v in g.vertices()]
    if all(len(edges) == 3 for edges in edges_list):
        raise _SlnFound()
    if all(len(edges) == 0 for edges in edges_list):
        raise _SlnFound()
    
    for v, w, has_edge in g.traverse(v_start, w_start):
        if has_edge:
            g.remove_edge(v, w)
            bt(g, v, w + 1, friendship_count - 1)
            g.add_edge(v, w)


def sln(k: int, friendships: list[tuple[int, int]]):
    g = Graph(k)
    for v, w in friendships:
        g.add_edge(v, w)
    
    try:
        bt(g, 0, 1, g.edge_count())
    except _SlnFound:
        return True

    return False
