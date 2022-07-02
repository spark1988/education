# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
# дополнительно возвращал список вершин, которые необходимо обойти.
# (для того, чтобы что?? поэтому тупао возвращаем вершины, по которыым обходили)


g = [
  #  0  1  2  3  4  4  6  7
    [0, 0, 1, 1, 9, 0, 0, 0,],  
    [0, 0, 9, 4, 0, 0, 5, 0,],  
    [0, 9, 0, 0, 3, 0, 6, 0,],  
    [0, 0, 0, 0, 0, 0, 0, 0,],  
    [0, 0, 0, 0, 0, 0, 1, 0,],  
    [0, 0, 0, 0, 0, 0, 5, 0,], 
    [0, 0, 7, 0, 8, 1, 0, 0,], 
    [0, 0, 0, 0, 0, 1, 2, 0,], 
]

g2 = [
    [0, 3, 1, 9],
    [0, 0, 1, 2],
    [0, 1, 0, 4],
    [0, 0, 0, 0],
]


def dkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length

    cost[start] = 0
    min_cost = 0
    way = []

    while min_cost < float('inf'):
        is_visited[start] = True
        way.append(start)

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                new_cost = vertex + cost[start]
                if cost[i] > new_cost:
                    cost[i] = new_cost


        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, way


print(dkstra(g, 0))