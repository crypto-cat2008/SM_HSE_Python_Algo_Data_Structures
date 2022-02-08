from heapq import heappop, heappush


def dijkstra(adj_matrix, v_from, v_to):
    n, graph = len(adj_matrix), adj_matrix

    dist = [float("inf") for i in range(n)]
    heap = []
    used = [False for i in range(n)]

    # check for negative weights
    for i in range(n):
        for j in range(n):
            if graph[i][j] < 0:
                return -1

    # check for missing source and destination
    if v_from < 0 or v_from >= n:
        return -1

    if v_to < 0 or v_to >= n:
        return -1

    heappush(heap, (0, v_from))
    dist[v_from] = 0

    while len(heap) > 0:
        d, v = heappop(heap)
        used[v] = True

        if dist[v] < d:
            continue

        for u in range(len(graph[v])):
            if not used[u] and d + graph[v][u] < dist[u]:
                dist[u] = d + graph[v][u]
                heappush(heap, (dist[u], u))

    # print(dist)

    if dist[v_to] == float('inf'):
        return -1
    else:
        return dist[v_to]


adj_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), float('inf')],
                 [2, float('inf'), float('inf')]]
v_from, v_to = 0, 2
# check that your code works correctly on provided example
assert dijkstra(adj_matrix, v_from, v_to) == 2, 'Wrong answer'

adj_matrix = [[float('inf'), -5, 2],
                 [5, float('inf'), float('inf')],
                 [2, float('inf'), float('inf')]]
v_from, v_to = 0, 2
# check that your code works correctly on provided example
assert dijkstra(adj_matrix, v_from, v_to) == -1, 'Wrong answer'

weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), float('inf')],
                 [2, float('inf'), float('inf')]]
v_from, v_to = 1, 2
# check that your code works correctly on provided example
answer = dijkstra(weight_matrix, v_from, v_to)
assert answer == 7, 'Wrong answer'

weight_matrix = [[float('inf'), 1, 4, float('inf'), float('inf')],
                 [float('inf'), float('inf'), 3, 2, 2],
                 [float('inf'), float('inf'), float('inf'), 6, float('inf')],
                 [float('inf'), 1, 5, float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), 3, float('inf')]
                 ]
v_from, v_to = 1, 2
# check that your code works correctly on provided example
answer = dijkstra(weight_matrix, v_from, v_to)
# print(answer)
assert answer == 3, 'Wrong answer'

weight_matrix = [[float('inf'), 1, float('inf'), float('inf')],
                 [2, float('inf'), float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), 2],
                 [float('inf'), float('inf'), 8, float('inf')]
                 ]
v_from, v_to = 3, 2
# check that your code works correctly on provided example
answer = dijkstra(weight_matrix, v_from, v_to)
# print(answer)
assert answer == 8, 'Wrong answer'

v_from, v_to = 0, 3
# check that your code works correctly on provided example
answer = dijkstra(weight_matrix, v_from, v_to)
# print(answer)
assert answer == -1, 'Wrong answer'

v_from, v_to = 2, 0
weight_matrix = [[float('inf'), 5, 2],
                 [50, float('inf'), 10],
                 [20, 10, float('inf')]]
answer = dijkstra(weight_matrix, v_from, v_to)
# print(answer)
assert answer == 20, 'Wrong answer'

'''
------------------------------------------------------------------------------------------------------------
'''
from heapq import heappop, heappush


def print_path(parent, j, path):

    if parent[j] == -1:
        return

    print_path(parent, parent[j], path)
    path.append(j)


def dijkstraPath(adj_matrix, v_from, v_to):
    n, graph = len(adj_matrix), adj_matrix
    path = []

    dist = [float("inf") for i in range(n)]
    heap = []
    used = [False for i in range(n)]
    parent = [-1 for i in range(n)]

    # check for negative weights
    for i in range(n):
        for j in range(n):
            if graph[i][j] < 0:
                return -1

    # check for missing source and destination
    if v_from < 0 or v_from >= n:
        return -1

    if v_to < 0 or v_to >= n:
        return -1

    if v_from == v_to:
        if adj_matrix[v_from][v_to] != float('inf'):
            return [v_from]

    heappush(heap, (0, v_from))
    dist[v_from] = 0

    while len(heap) > 0:
        d, v = heappop(heap)
        used[v] = True

        if dist[v] < d:
            continue

        for u in range(len(graph[v])):
            if not used[u] and d + graph[v][u] < dist[u]:
                dist[u] = d + graph[v][u]
                parent[u] = v
                heappush(heap, (dist[u], u))

    # print('parent', parent)

    print_path(parent, v_to, path)

    if len(path) > 0:
        path = [v_from] + path
        # print('path', path)
        # print('dist', dist)
        return path
    else:
        return -1


adj_matrix = [[float('inf'), 5, 2],
              [5, float('inf'), float('inf')],
              [2, float('inf'), float('inf')]]
v_from, v_to = 0, 2
# check that your code works correctly on provided example
assert dijkstraPath(adj_matrix, v_from, v_to) == [0, 2], 'Wrong answer'

weight_matrix = [[float('inf'), 1, 4, float('inf'), float('inf')],
                 [float('inf'), float('inf'), 3, float('inf'), 20],
                 [float('inf'), float('inf'), float('inf'), 6, float('inf')],
                 [float('inf'), 1, 5, 1, float('inf')],
                 [float('inf'), float('inf'), float('inf'), 3, float('inf')]
                 ]
v_from, v_to = 1, 3
# check that your code works correctly on provided example
answer = dijkstraPath(weight_matrix, v_from, v_to)
assert answer == [1, 2, 3], 'Wrong answer'

v_from, v_to = 3, 0
# check that your code works correctly on provided example
answer = dijkstraPath(weight_matrix, v_from, v_to)
assert answer == -1, 'Wrong answer'

v_from, v_to = 3, 3
# check that your code works correctly on provided example
answer = dijkstraPath(weight_matrix, v_from, v_to)
assert answer == [3, 3], 'Wrong answer'