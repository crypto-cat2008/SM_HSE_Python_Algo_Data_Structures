def get_neighbours(v, graph):
    neighbours = []
    for i in range(len(graph)):
        if graph[v][i] == 1:
            neighbours.append(i)

    return neighbours


def hasLoops(adj_matrix):
    n = len(adj_matrix)
    has_loops = False

    for i in range(n):
        for j in range(len(adj_matrix)):
            if i == j and adj_matrix[i][i] == 1:
                has_loops = True

    return has_loops


adj_matrix = [[0, 1], [0, 1]]
# check that your code works correctly on provided example
assert hasLoops(adj_matrix), 'Wrong answer'


def isUndirected(adj_matrix):
    n = len(adj_matrix)
    is_undirected = True

    for i in range(n):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                if adj_matrix[j][i] != 1:
                    is_undirected = False
            if i == j and adj_matrix[i][i] == 1:
                is_undirected = False

    return is_undirected


adj_matrix = [[0, 1], [1, 0]]
# check that your code works correctly on provided example
assert isUndirected(adj_matrix), 'Wrong answer'



def countEdges(adj_matrix):
    n = len(adj_matrix)
    edges_count = 0

    for i in range(n):
        neighbour_list = get_neighbours(i, adj_matrix)
        edges_count += len(neighbour_list)

    return edges_count/2


adj_matrix = [[0, 1], [1, 0]]
# check that your code works correctly on provided example
assert countEdges(adj_matrix) == 1, 'Wrong answer'



def edgesCount(adj_list):
    n = len(adj_list)
    edges_count = 0

    for v in range(n):
        edges_count += len(adj_list[v])

    return edges_count/2

adj_list = [[1, 2], [0], [0]]
# check that your code works correctly on provided example
assert edgesCount(adj_list) == 2, 'Wrong answer'


def reverseGraph(adj_list):
    n = len(adj_list)
    reversed_graph = [[] for i in range(n)]

    for v_from in range(n):
        for v_to in adj_list[v_from]:
            reversed_graph[v_to].append(v_from)

    return reversed_graph

adj_list = [[1, 2], [], []]
# check that your code works correctly on provided example
assert reverseGraph(adj_list) == [[], [0], [0]], 'Wrong answer'


def isTransitive(adj_list):
    n = len(adj_list)
    is_transitive = True

    for v_1 in range(n):
        for v_2 in adj_list[v_1]:
            for v_3 in adj_list[v_2]:

                if v_3 not in adj_list[v_1]:
                    is_transitive = False

    return is_transitive

adj_list = [[1, 2], [2], []]
# check that your code works correctly on provided example
assert isTransitive(adj_list), 'Wrong answer'


def vertexDegree(vertex_count, edge_list):
    n = vertex_count
    degrees = [0 for i in range(n)]

    for edge in edge_list:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    return degrees

vertex_count = 3
edge_list = [[0, 1], [0, 2]]
# check that your code works correctly on provided example
assert vertexDegree(vertex_count, edge_list) == [2, 1, 1], 'Wrong answer'


def hasDuplicates(vertex_count, edge_list):
    n = vertex_count
    has_duplicates = False

    for edge in edge_list:
        v1 = edge[0]
        v2 = edge[1]
        if [v2, v1] in edge_list:
            has_duplicates = True
        if edge_list.count(edge) > 1:
            has_duplicates = True

    return has_duplicates

vertex_count = 2
edge_list = [[0, 1], [1, 0]]
# check that your code works correctly on provided example
assert hasDuplicates(vertex_count, edge_list), 'Wrong answer'

def get_neighbours_edge_list(v, edges):
    neighbours = []
    for edge in edges:
        if edge[0] == v:
            neighbours.append(edge[1])

    return neighbours

def isComplete(vertex_count, edge_list):
    n = vertex_count
    is_complete = True

    edge_count = len(edge_list)
    if edge_count != (vertex_count*(vertex_count-1))/2:
        print('edge_count')
        is_complete = False

    for edge in edge_list:
        v = edge[0]
        n = len(get_neighbours_edge_list(v, edge_list))
        if n < vertex_count - 1:
            print('1', n)
            is_complete = False

    return is_complete

vertex_count = 2
edge_list = [[0, 1]]
# check that your code works correctly on provided example
assert isComplete(vertex_count, edge_list), 'Wrong answer'

