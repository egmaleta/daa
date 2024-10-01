from shared.graph import DirectedGraph
from shared.testing import test

from .test_gen import TEST_GEN


def sln(n: int, streets: list[tuple[int, int, int]]):
    g = DirectedGraph(n)
    for v, w, weight in streets:
        g.add_edge(v, w, weight)
    
    vertices = g.V()

    dists = [
        [0 if x == y else None for x in vertices]
        for y in vertices
    ]
    prevs = [
        [x if x == y else None for x in vertices]
        for y in vertices
    ]
    for v, w, weight in g.traverse():
        dists[v][w] = weight
        prevs[v][w] = v
    
    for k in vertices:
        for i in vertices:
            for j in vertices:
                i2k = dists[i][k]
                if i2k is None:
                    continue

                k2j = dists[k][j]
                if k2j is None:
                    continue

                i2k2j = i2k + k2j
                i2j = dists[i][j]
                if i2j is None or i2j > i2k2j:
                    dists[i][j] = i2k2j
                    prevs[i][j] = prevs[k][j]
    
    def path_length(v: int, w: int):
        if prevs[v][w] is None:
            return None
        
        p = [w]
        while v != w:
            w = prevs[v][w]
            assert w is not None
            p.append(w)
        
        return len(p) - 1
    
    street_lengths = set()
    for v, ws in enumerate(dists):
        for w, dist in enumerate(ws):
            if w == v:
                continue

            if dist is not None:
                l = path_length(v, w)
                assert l is not None
                street_lengths.add((v, w, l))
    
    return street_lengths


test(sln, TEST_GEN)
