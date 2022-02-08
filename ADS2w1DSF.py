visited = []
graph = []

def dfs(v):

    visited[v] = True
    for u in range(len(graph[v])):
        if v != u and graph[v][u] != 0 and not visited[u]:
            dfs(u)


def sameComponent(adj_list, vertex):
    global visited
    global graph

    graph = adj_list
    n = len(adj_list)
    visited = []

    for i in range(n):
        visited.append(False)


    dfs(vertex)
    # print(visited)

    return visited.count(True)

adj_matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
vertex = 2
# check that your code works correctly on provided example
assert sameComponent(adj_matrix, vertex) == 3, 'Wrong answer'


adj_matrix = [[0, 1, 1, 0,0], [1, 0, 0, 0,0], [1, 0, 0, 0,0], [0, 0, 0, 0,1], [0, 0, 0, 1,0]]
vertex = 4
# check that your code works correctly on provided example
assert sameComponent(adj_matrix, vertex) == 2, 'Wrong answer'

'''
------------------------------------------------------------------
'''

def check_cycles(v, visisted, graph):
    cycles = False

    visisted[v] = True

    for u in graph[v]:
        if not visisted[u]:
            check_cycles(u, visisted, graph)
        else:
            if v != u:
                cycles = True

    return cycles

def isTree(adj_list):
    n = len(adj_list)
    visited = [False for i in range(n)]

    if check_cycles(0, visited, adj_list):
        is_tree = False
    elif False in visited:
        is_tree = False
    else:
        is_tree = True

    # print(is_tree, visited)

    return is_tree


adj_list = [[1, 2], [0], [0]]
# check that your code works correctly on provided example
assert isTree(adj_list), 'Wrong answer'

adj_list = [[1, 2], [0], [0], []]
# check that your code works correctly on provided example
assert not isTree(adj_list), 'Wrong answer'

adj_list = [[1, 2], [2], [1]]
# check that your code works correctly on provided example
assert not isTree(adj_list), 'Wrong answer'


'''
------------------------------------------------------------------
'''

def dfs_topological_sort(v, visited, graph, order):
    visited[v] = True

    for u in graph[v]:
        if not visited[u]:
            dfs_topological_sort(u, visited, graph, order)
    order.append(v)


def cyclic(g):
    path = set()

    def visit(vertex):
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)


def sortCourses(course_list, prerequisites_dict):

    if cyclic(prerequisites_dict):
        return -1

    n = len(course_list)
    course_order = []
    adj_list = [[] for i in range(len(course_list))]
    visited = [False for i in range(n)]

    for key in prerequisites_dict:
        for course in prerequisites_dict[key]:
            adj_list[course].append(key)

    # print('adj_list', adj_list)

    for v in range(n):
        if not visited[v]:
            dfs_topological_sort(v, visited, adj_list, course_order)

    course_order = course_order[::-1]
    # print(course_order)

    return course_order


course_list = [0, 1, 2]
prerequisites_dict = {2 : [1], 1: [0]}
# check that your code works correctly on provided example
assert sortCourses(course_list, prerequisites_dict) == [0, 1, 2], 'Wrong answer'


course_list = [0, 1, 2, 3, 4, 5]
prerequisites_dict = {0: [2], 2: [3], 1: [3, 0], 5: [3, 4]}
# check that your code works correc tly on provided example
assert sortCourses(course_list, prerequisites_dict) == [4,3,5,2,0,1], 'Wrong answer'

course_list = [0, 1, 2, 3, 4, 5]
prerequisites_dict = {0: [4, 5], 1: [4], 2: [5], 3 :[2], 4: [], 5: []}
# check that your code works correc tly on provided example
assert sortCourses(course_list, prerequisites_dict) == [5,4,2,3,1,0], 'Wrong answer'

course_list = [0, 1, 2]
prerequisites_dict = {0: [2], 1: [0], 2: [1]}
# check that your code works correct tly on provided example
assert sortCourses(course_list, prerequisites_dict) == -1, 'Wrong answer'


'''
------------------------------------------------------------------
'''


def dfs_rooks(v, visited, graph):

    visited[v] = True

    for u in range(len(graph[v])):
        if graph[v][u] != 0 and not visited[u]:
            dfs_rooks(u, visited, graph)

def get_neighbours(v, graph):
    neighbours = []
    for i in range(len(graph)):
        if graph[v][i] == 1:
            neighbours.append(i)

    return neighbours


def minRooksLeft(board_size, coordinates):
    # each entry in coordinates array looks like this: (x, y) - coordinates of the rook
    n = len(coordinates)
    rooks_left = 0
    connected_components = set()
    adj_matrix = [[0 for i in range(board_size)] for i in range(board_size)]
    visited = [False for i in range(board_size)]


    for c in coordinates:
        adj_matrix[c[0]][c[1]] = 1
        adj_matrix[c[1]][c[0]] = 1

    # print(adj_matrix)

    for v in range(len(adj_matrix)):
        # print(v, visited)
        if not visited[v]:
            connected_components.add(v)
            dfs_rooks(v, visited, adj_matrix)

    for node in connected_components:
        if len(get_neighbours(node, adj_matrix)) != 0:
            rooks_left += 1

    # print(connected_components, rooks_left)

    return rooks_left


board_size = 4
coordinates = [(0, 0), (0, 3), (3, 0)]
# check that your code works correctly on provided example
assert minRooksLeft(board_size, coordinates) == 1, 'Wrong answer'


board_size = 4
coordinates = [(0, 0), (0, 2), (1, 0), (1, 1), (2, 2)]
# check that your code works correctly on provided example
assert minRooksLeft(board_size, coordinates) == 1, 'Wrong answer'

board_size = 4
coordinates = [(0, 0)]
# check that your code works correctly on provided example
assert minRooksLeft(board_size, coordinates) == 1, 'Wrong answer'

board_size = 4
coordinates = [(0, 0), (0, 3), (3, 0), (1, 1)]
# check that your code works correctly on provided example
assert minRooksLeft(board_size, coordinates) == 2, 'Wrong answer'

board_size = 4
coordinates = [(0, 0), (1, 1), (2, 2), (3, 3)]
# check that your code works correctly on provided example
assert minRooksLeft(board_size, coordinates) == 4, 'Wrong answer'

board_size = 4
coordinates = [(0, 0), (1, 1), (2, 2), (3, 3), (1, 3)]
# check that your code works correctly on provided example
assert minRooksLeft(board_size, coordinates) == 3, 'Wrong answer'

