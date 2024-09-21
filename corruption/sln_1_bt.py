from sln_2_dikjstra import Grafo

def camino_minimo(Graph, start, end):
    visited = set()
    min_cost = [float('inf')]

    def backtrack(v, current_cost):
        if v == end:
            min_cost[0] = min(min_cost[0], current_cost)
            return 
        
        visited.add(v)

        for neighbor,cost in Graph.grafo[v].items():
            if neighbor not in visited:
                backtrack(neighbor, current_cost + cost)

        visited.remove(v)

    backtrack(start, 0)
    return min_cost[0] if min_cost[0] != float('inf') else None           