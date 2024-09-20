from typing import Any

class Graph:
    def __init__(self, size: int):
        assert size >= 2
        self._mask: list[list[Any]] = [
            [None for _ in range(size)]
            for _ in range(size)
        ]
    
    def traverse(self, v_start = 0, w_start = 1):
        for v, mask in enumerate(self._mask[v_start:], start=v_start):
            if v > v_start:
                # continue traversing matrix normally
                w_start = v + 1
            
            for w, data in enumerate(mask[w_start:], start=w_start):
                yield v, w, data
    
    def _is_valid_vertex(self, v: int):
        return 0 <= v < len(self._mask)
    
    def _is_valid_edge(self, v: int, w: int):
        return v != w and self._is_valid_vertex(v) and self._is_valid_vertex(w)
    
    def add_edge(self, v: int, w: int, data):
        assert self._is_valid_edge(v, w)
        assert data is not None
        self._mask[v][w] = data
        self._mask[w][v] = data

    def remove_edge(self, v: int, w: int):
        assert self._is_valid_edge(v, w)
        self._mask[v][w] = None
        self._mask[w][v] = None
    
    def edge_count(self):
        count = 0
        for _, _, data in self.traverse():
            if data is not None:
                count += 1
        return count
    
    def vecinity(self, v: int):
        assert self._is_valid_vertex(v)
        return [w for w, data in enumerate(self._mask[v]) if data is not None]
    
    def vertices(self):
        return [v for v in range(len(self._mask))]


class DirectedGraph:
    def __init__(self, size: int):
        assert size >= 2
        self._mask: list[list[Any]] = [
            [None for _ in range(size)]
            for _ in range(size)
        ]
    
    def traverse(self, v_start = 0, w_start = 0):
        for v, mask in enumerate(self._mask[v_start:], start=v_start):
            if v > v_start:
                # continue traversing matrix normally
                w_start = 0
            
            for w, data in enumerate(mask[w_start:], start=w_start):
                if w == v:
                    continue
                yield v, w, data
    
    def _is_valid_vertex(self, v: int):
        return 0 <= v < len(self._mask)
    
    def _is_valid_edge(self, v: int, w: int):
        return v != w and self._is_valid_vertex(v) and self._is_valid_vertex(w)
    
    def add_edge(self, v: int, w: int, data):
        assert self._is_valid_edge(v, w)
        assert data is not None
        self._mask[v][w] = data

    def remove_edge(self, v: int, w: int):
        assert self._is_valid_edge(v, w)
        self._mask[v][w] = None
    
    def V(self):
        return [v for v in range(len(self._mask))]
