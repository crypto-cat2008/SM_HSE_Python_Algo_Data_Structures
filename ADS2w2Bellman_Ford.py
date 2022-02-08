def BellmanFord(weight_matrix, v_from):
    n, graph = len(weight_matrix), weight_matrix
    dist = [float("inf") for i in range(n)]

    dist[v_from] = 0

    for e in range(1, n):
        for u in range(n):
            for v in range(n):
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    return dist


weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), float('inf')],
                 [2, float('inf'), float('inf')]]
v_from = 0
# check that your code works correctly on provided example
answer = BellmanFord(weight_matrix, v_from)
# print(answer)
assert answer == [0, 5, 2], 'Wrong answer'

weight_matrix = [[float('inf'), -1, 4, float('inf'), float('inf')],
                 [float('inf'), float('inf'), 3, 2, 2],
                 [float('inf'), float('inf'), float('inf'), 6, float('inf')],
                 [float('inf'), 1, 5, float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), -3, float('inf')]
                 ]
v_from = 0
# check that your code works correctly on provided example
answer = BellmanFord(weight_matrix, v_from)
# print(answer)
assert answer == [0, -1, 2, -2, 1], 'Wrong answer'

weight_matrix = [[float('inf'), 1, float('inf'), float('inf')],
                 [2, float('inf'), float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), 2],
                 [float('inf'), float('inf'), -2, float('inf')]
                 ]
v_from = 3
# check that your code works correctly on provided example
answer = BellmanFord(weight_matrix, v_from)
# print(answer)
assert answer == [float('inf'), float('inf'), -2, 0], 'Wrong answer'

v_from = 2
weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), -10],
                 [2, -10, float('inf')]]
answer = BellmanFord(weight_matrix, v_from)
# print(answer)

'''
------------------------------------------------------------------------------------------------------------
'''


def hasNegativeCycle(weight_matrix):
    n = len(weight_matrix)
    has_negative_cycle = False

    for source in range(n):

        dist = [float('inf') for i in range(n)]
        dist[source] = 0

        for e in range(1, n):
            for u in range(n):
                for v in range(n):
                    dist[v] = min(dist[v], dist[u] + weight_matrix[u][v])

        for u in range(n):
            for v in range(n):
                if dist[v] != float('inf') and dist[u] + weight_matrix[u][v] < dist[v]:
                    return True

    return has_negative_cycle


weight_matrix = []
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert not answer, 'Wrong answer'

weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), -10],
                 [2, -10, float('inf')]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'

weight_matrix = [[float('inf'), -1, 4, float('inf'), float('inf')],
                 [float('inf'), float('inf'), 3, 2, 2],
                 [float('inf'), float('inf'), float('inf'), 6, float('inf')],
                 [float('inf'), 1, 5, float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), -3, float('inf')]]
# check that your code works correctly on provided example
assert not hasNegativeCycle(weight_matrix), 'Wrong answer'

weight_matrix = [[float('inf'), -1],
                 [-2, float('inf')]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'


weight_matrix = [[float('inf'), 1],
                 [2, float('inf')]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert not answer, 'Wrong answer'


weight_matrix = [[float('inf'), -1, float('inf'), float('inf'), float('inf')],
                 [-2, float('inf'), float('inf'), float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), 1, float('inf')],
                 [float('inf'), float('inf'), float('inf'), float('inf'), 2],
                 [float('inf'), float('inf'), 10, float('inf'), float('inf')],
                 ]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'


weight_matrix = [[-1]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'


'''
------------------------------------------------------------------------------------------------------------
'''


def bellmanFord(edges, source, N):
    # `cost` stores the shortest path information
    cost = [float('inf')] * N

    # Initially, all vertices except the source vertex weight infinity
    cost[source] = 0

    # Relaxation step (run `V-1` times)
    for _ in range(N - 1):
        # consider all edges from `u` to `v` having weight `w`
        for (u, v, w) in edges:
            # if the cost to destination `u` can be
            # shortened by taking edge `u —> v`
            if cost[u] != float('inf') and cost[u] + w < cost[v]:
                # update cost to the new lower value
                cost[v] = cost[u] + w

    # Run relaxation step once more for N'th time to
    # check for negative-weight cycles
    for (u, v, w) in edges:
        # if the cost to destination `u` can be
        # shortened by taking edge `u —> v`
        if cost[u] != float('inf') and cost[u] + w < cost[v]:
            return True

    return False

def hasNegativeCycle(weight_matrix):
    N = len(weight_matrix)
    edges = []

    for v in range(N):
        for u in range(N):
            if weight_matrix[v][u] and weight_matrix[v][u] != float('inf'):
                edges.append((v, u, weight_matrix[v][u]))

    for i in range(N):
        if bellmanFord(edges, i, N):
            return True

    return False

weight_matrix = []
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert not answer, 'Wrong answer'

weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), -10],
                 [2, -10, float('inf')]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'

weight_matrix = [[float('inf'), -1, 4, float('inf'), float('inf')],
                 [float('inf'), float('inf'), 3, 2, 2],
                 [float('inf'), float('inf'), float('inf'), 6, float('inf')],
                 [float('inf'), 1, 5, float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), -3, float('inf')]]
# check that your code works correctly on provided example
assert not hasNegativeCycle(weight_matrix), 'Wrong answer'

weight_matrix = [[float('inf'), -1],
                 [-2, float('inf')]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'


weight_matrix = [[float('inf'), 1],
                 [2, float('inf')]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert not answer, 'Wrong answer'


weight_matrix = [[float('inf'), -1, float('inf'), float('inf'), float('inf')],
                 [-2, float('inf'), float('inf'), float('inf'), float('inf')],
                 [float('inf'), float('inf'), float('inf'), 1, float('inf')],
                 [float('inf'), float('inf'), float('inf'), float('inf'), 2],
                 [float('inf'), float('inf'), 10, float('inf'), float('inf')],
                 ]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'


weight_matrix = [[-1]]
# check that your code works correctly on provided example
answer = hasNegativeCycle(weight_matrix)
assert answer, 'Wrong answer'

