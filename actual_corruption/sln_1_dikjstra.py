from shared import FLOAT_INF as INF


def get_min(nodes):
    minimum = INF
    index = 0
    for i,node in enumerate(nodes):
        if node[1] < minimum:
            index = i
            minimum = node[1]

    return index


def dijkstra(graph, s):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    V = len(dist[0])
    nodes = [[i,INF,[None]] for i in range(V)]
    nodes[s][1]=0
    lista=[[s,0,[None]]]
    while len(lista)>0:
        #current = lista.pop(0)
        current = lista.pop(get_min(lista))
        for i in range(V):
            if i != current[0]:
                if dist[current[0]][i] < INF and nodes[i][1] >= nodes[current[0]][1] + dist[current[0]][i]:
                    if nodes[i][1] == nodes[current[0]][1] + dist[current[0]][i]:
                        nodes[i][1] = nodes[current[0]][1] + dist[current[0]][i]
                        nodes[i][2].append(current[0])
                    else:
                        nodes[i][2] = [current[0]]
                        nodes[i][1] = nodes[current[0]][1] + dist[current[0]][i]
                        lista.append(nodes[i])
    return nodes


def path_seeker(current, nodes, used_edges, left, right, sol):
    if nodes[current][2].__contains__(None):
        return
    else:
        for i in nodes[current][2]:
            if not used_edges[i][current]:
                #used_edges[current][i] = True 
                used_edges[i][current] = True
                sol[left][right] += 1
            path_seeker(i,nodes,used_edges, left, right, sol)


def sln(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    solution_matrix = [[0 for i in range(len(dist[0]))] for i in range (len(dist[0]))] #this is new 
    
    V = len(dist)
    for i in range(V):
        temp = dijkstra(dist,i)
        for j in range(V):
            used_edges = [[False for i in range(len(dist[0]))] for i in range (len(dist[0]))]
            path_seeker(j,temp,used_edges, i, j, solution_matrix)
    return solution_matrix


graph = [
    [0, 1, INF, INF,INF],
	[1, 0, 1, 1,INF],
	[INF, 1, 0, INF,1],
	[INF, 1, INF, 0,1],
    [INF,INF,1,1,0]
]
print(sln(graph))
