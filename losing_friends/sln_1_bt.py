from shared.graph import Graph


class _SlnFound(Exception):
    pass


def bt(g: Graph, v_start: int, w_start: int, friendship_count: int):
    if friendship_count == 0:
        return
    
    edges_list = [g.vecinity(v) for v in g.vertices()]
    if all(len(edges) == 3 for edges in edges_list):
        raise _SlnFound()
    if all(len(edges) == 0 for edges in edges_list):
        raise _SlnFound()
    
    for v, w, data in g.traverse(v_start, w_start):
        g.remove_edge(v, w)
        bt(g, v, w + 1, friendship_count - 1)
        g.add_edge(v, w, data)


def sln(k: int, friendships: list[tuple[int, int]]):
    g = Graph(k)
    for v, w in friendships:
        g.add_edge(v, w, True)
    
    try:
        bt(g, 0, 1, g.edge_count())
    except _SlnFound:
        return True

    return False
