from collections import deque


def distance(adj_list, v_from, v_to):
    n = len(adj_list)
    distance = -1

    if n == 0 or v_from >= n or v_to >= n or v_from < 0 or v_to < 0:
        return -1

    visited = [False for i in range(n)]
    Q = deque()

    Q.append((0, v_from))
    visited[v_from] = True

    while len(Q) > 0:
        d, v = Q.pop()
        # print("distance to", v, "from start", d)
        if v == v_to:
            distance = d
            return distance

        for u in adj_list[v]:
            if not visited[u]:
                Q.append((d + 1, u))
                visited[u] = True

    return distance


adj_list = []
v_from, v_to = 0, 2
# check that your code works correctly on provided example
assert distance(adj_list, v_from, v_to) == -1, 'Wrong answer'

adj_list = [[1], [0, 2], [1]]
v_from, v_to = 0, 2
# check that your code works correctly on provided example
assert distance(adj_list, v_from, v_to) == 2, 'Wrong answer'

adj_list = [[1], [0, 2], [1], [4], [3]]
v_from, v_to = 3, 4
# check that your code works correctly on provided example
assert distance(adj_list, v_from, v_to) == 1, 'Wrong answer'

adj_list = [[1], [0, 2], [1], [4], [3]]
v_from, v_to = 0, 4
# check that your code works correctly on provided example
assert distance(adj_list, v_from, v_to) == -1, 'Wrong answer'

adj_list = [[1], [0, 2], [1], [4], [3]]
v_from, v_to = 0, 0
# check that your code works correctly on provided example
assert distance(adj_list, v_from, v_to) == 0, 'Wrong answer'

adj_list = [[1], [2], [3], [4], []]
v_from, v_to = 0, 4
# check that your code works correctly on provided example
assert distance(adj_list, v_from, v_to) == 4, 'Wrong answer'

'''
------------------------------------------------------------------
'''

from collections import deque


def isBipartite(adj_list):

    un_used = 0
    blue = 1
    red = 2

    n = len(adj_list)
    is_bipartite = True
    color = [0 for i in range(n)]

    visited = [False for i in range(n)]

    for i in range(len(adj_list)):
        if color[i] == un_used:
            Q = deque()
            Q.append(i)
            color[i] = blue

            while len(Q) > 0:
                v = Q.pop()
                for u in adj_list[v]:
                    if color[v] == color[u]:
                        # print('1', color, False)
                        return False
                    if color[u] == un_used:
                        color[u] = (color[v] % 2) + 1
                        Q.append(u)

    # print('2', color, is_bipartite)
    return is_bipartite


adj_list = [[], [2], [1]]
# check that your code works correctly on provided example
assert isBipartite(adj_list), 'Wrong answer'

adj_list = [[1, 2], [2], [1]]
# check that your code works correctly on provided example
assert not isBipartite(adj_list), 'Wrong answer'

adj_list = [[1], [0], [3], [2]]
# check that your code works correctly on provided example
assert isBipartite(adj_list), 'Wrong answer'

adj_list = [[1], [2], [0]]
# check that your code works correctly on provided example
assert not isBipartite(adj_list), 'Wrong answer'

adj_list = [[1], [2], [3], [0]]
# check that your code works correctly on provided example
assert isBipartite(adj_list), 'Wrong answer'

adj_list = [[1], [2], [3], [0], [5], [6], [4]]
# check that your code works correctly on provided example
assert not isBipartite(adj_list), 'Wrong answer'

'''
------------------------------------------------------------------
'''


def maze2graph_save(maze):

    height = len(maze)
    if height == 0:
        return {}

    width = len(maze[0])
    if width == 0:
        return {}

    maze1 = []

    if height > 1:
        for row in maze:
            width = len(row[0])
            maze1.append(row[0])
    else:
        maze1 = maze

    graph = {(x, y): [] for y in range(width) for x in range(height) if maze1[x][y] != "#"}

    for key in graph:
        i = key[0]
        j = key[1]

        # check left
        if j - 1 >= 0:
            if maze1[i][j-1] == '.' or maze1[i][j-1].upper() == 'X':
                graph[key].append((i, j - 1))

        # check right
        if j + 1 <= width - 1:
            if maze1[i][j+1] == '.' or maze1[i][j+1].upper() == 'X':
                graph[key].append((i, j + 1))

        # check up
        if i - 1 >= 0:
            if maze1[i - 1][j] == '.' or maze1[i - 1][j].upper() == 'X':
                graph[key].append((i - 1, j))

        # check down
        if i + 1 <= height - 1:
            if maze1[i + 1][j] == '.' or maze1[i + 1][j].upper() == 'X':
                graph[key].append((i + 1, j))

    # print(graph)

    return graph


def maze2graph(maze):

    height = len(maze)
    if height == 0:
        return {}

    width = len(maze[0])
    if width == 0:
        return {}

    graph = {(x, y): [] for y in range(width) for x in range(height) if maze[x][y] != "#"}

    for key in graph:
        i = key[0]
        j = key[1]

        # check left
        if j - 1 >= 0:
            if maze[i][j-1] == '.' or maze[i][j-1].upper() == 'X':
                graph[key].append((i, j - 1))

        # check right
        if j + 1 <= width - 1:
            if maze[i][j+1] == '.' or maze[i][j+1].upper() == 'X':
                graph[key].append((i, j + 1))

        # check up
        if i - 1 >= 0:
            if maze[i - 1][j] == '.' or maze[i - 1][j].upper() == 'X':
                graph[key].append((i - 1, j))

        # check down
        if i + 1 <= height - 1:
            if maze[i + 1][j] == '.' or maze[i + 1][j].upper() == 'X':
                graph[key].append((i + 1, j))

    # print(graph)

    return graph


maze = ['.X..#.']
# check that your code works correctly on provided example
assert maze2graph(maze) == {(0, 0): [(0, 1)], (0, 1): [(0, 0), (0, 2)], (0, 2): [(0, 1), (0, 3)], (0, 3): [(0, 2)], (0, 5): []}, 'Wrong answer'


maze = [['....#.'], ['..x.#.']]
# check that your code works correctly on provided example
'''
assert maze2graph(maze) == {(0, 0): [(0, 1), (1, 0)], (1, 0): [(1, 1), (0, 0)], (0, 1): [(0, 0), (0, 2), (1, 1)],
                            (1, 1): [(1, 0), (1, 2), (0, 1)], (0, 2): [(0, 1), (0, 3), (1, 2)], (1, 2): [(1, 1), (1, 3), (0, 2)],
                            (0, 3): [(0, 2), (1, 3)], (1, 3): [(1, 2), (0, 3)], (0, 5): [(1, 5)], (1, 5): [(0, 5)]}, 'Wrong answer'
'''


maze = ['##.x.#']
# check that your code works correctly on provided example
assert maze2graph(maze) == {(0, 2): [(0, 3)], (0, 3): [(0, 2), (0, 4)], (0, 4): [(0, 3)]}, 'Wrong answer'

maze = []
# check that your code works correctly on provided example
assert maze2graph(maze) == {}, 'Wrong answer'

maze = ['']
# check that your code works correctly on provided example
assert maze2graph(maze) == {}, 'Wrong answer'


'''
------------------------------------------------------------------
'''
from collections import deque


def maze_distance(graph, start, goal):
    explored = []

    queue = [[start]]

    if start == goal:
        return []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    return(new_path)

            explored.append(node)

    return []


def path2exit(maze, x, y):
    height, width = len(maze), len(maze[0])
    path = []
    answer = []

    graph = maze2graph_save(maze)

    X_found = False
    X_x = 0
    X_y = 0

    # find X
    for row in maze:
        X_y = row[0].find('X')
        if X_y > 0:
            X_found = True
            break
        X_x += 1

    if X_found:
        X = (X_x, X_y)
        # print(X)
    else:
        return -1

    path = maze_distance(graph, (x, y), X)
    # print(path)

    if len(path) == 0:
        return -1
    else:
        for i, j in zip(path, path[1:]):
            if i[0] < j[0] and i[1] == j[1]:
                answer.append('D')
            elif i[0] > j[0] and i[1] == j[1]:
                answer.append('U')
            elif i[0] == j[0] and i[1] < j[1]:
                answer.append('R')
            elif i[0] == j[0] and i[1] > j[1]:
                answer.append('L')

    # print(''.join(answer))

    return ''.join(answer)



maze = [['.#.'], ['..X']]
x, y = 0, 0
# check that your code works correctly on provided example
assert path2exit(maze, x, y) == 'DRR', 'Wrong answer'


maze = [['...'], ['.#.'],['.#X'], ['...']]
x, y = 0, 0
# check that your code works correctly on provided example
assert path2exit(maze, x, y) == 'RRDD', 'Wrong answer'

maze = [['...'], ['.##'],['.#X'], ['.#.']]
x, y = 0, 0
# check that your code works correctly on provided example
assert path2exit(maze, x, y) == -1, 'Wrong answer'


