from shared import FLOAT_INF

from .grafo import Grafo


def min_cost_path_len(Graph, start, end):
    visited = set()
    min_cost = [FLOAT_INF]
    path_len = [FLOAT_INF]

    def backtrack(v, current_cost, pl):
        if v == end:
            if current_cost < min_cost[0]:
                min_cost[0] = current_cost
                path_len[0] = pl
            return 
        
        visited.add(v)

        for neighbor, cost in Graph.grafo[v].items():
            if neighbor not in visited:
                backtrack(neighbor, current_cost + cost, pl + 1)

        visited.remove(v)

    backtrack(start, 0, 0)
    return path_len[0]


def sln(graph: Grafo):
    vertices = sorted(graph.grafo.keys())

    lenghts = []
    for v in vertices:
        for w in vertices:
            if v == w:
                continue

            l = min_cost_path_len(graph, v, w)
            if l != FLOAT_INF:
                lenghts.append((v, w, l))
    
    return lenghts
