def floyd_warshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    V = len(dist[0])
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist [k][j]:
                    dist[i][j] = dist[i][k] + dist [k][j]
    return dist


def sln(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    V = len(dist[0])
    fw = floyd_warshall(dist)
    used_vertex = [[[] for i in range(V)] for i in range(V)]
    incoming_edges_to_j = [[0 for i in range(V)] for i in range(V)]
    edges_involved = [[0 for i in range(V)] for i in range(V)]
    
    for i in range(V):
        for j in range(V):
            if(i!=j):
                for k in range(V):
                    if fw[i][j] == fw[i][k] + fw[k][j] and k!=i:
                        used_vertex[i][j].append(k)
                    if fw[i][j] == fw[i][k] + dist[k][j] and k!=j:
                        incoming_edges_to_j[i][j] = incoming_edges_to_j[i][j] + 1
            
    for i in range(V):
        for j in range(V):
            for v in used_vertex[i][j]:
                edges_involved[i][j] = edges_involved[i][j] + incoming_edges_to_j[i][v]
                
    return edges_involved
