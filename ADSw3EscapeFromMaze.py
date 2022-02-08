import math
import copy

def fastest_escape_length(maze, i=0, j=0, l=1):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall

    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return l

    maze[i][j] = 1

    min_length = math.inf

    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:

        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:

            a_length = fastest_escape_length(maze, a, b, l + 1)

            if a_length < min_length:
                min_length = a_length

    maze[i][j] = 0
    return min_length

def fastest_escapes(maze, i=0, j=0, path=[]):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall

    global min_paths
    if len(path) == 0:
        min_paths = []

    path.append((i, j))

    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:

        min_length = math.inf

        if len(min_paths) > 0:
            min_length = len(min_paths[0])
            if min_length > len(path):
                min_paths = []

        if min_length >= len(path):
            min_paths.append(copy.deepcopy(path))

        path.remove((i, j))
        return min_paths

    maze[i][j] = 1

    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            fastest_escapes(maze, a, b, path)

    maze[i][j] = 0

    path.remove((i, j))

    return min_paths


def weighted_escape_length(maze, w, i=0, j=0, l=1):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall

    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return l

    maze[i][j] = maze[i][j] + 2

    min_length = math.inf
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] < 2:
            if maze[a][b] == 1:
                cost = w
            else:
                cost = 1
            a_length = weighted_escape_length(maze, w, a, b, l + cost)
            if a_length < min_length:
                min_length = a_length

    maze[i][j] = maze[i][j] - 2

    return min_length

def w_len(maze, w, path):
    l = 0
    for p in path:
        (i, j) = p
        if maze[i][j] == 2 or maze[i][j] == 0:
            l = l+1
        elif maze[i][j] == 3 or maze[i][j] == 1:
            l = l+w

    return l

def weighted_escapes(maze, w, i=0, j=0, path=[]):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall

    global min_paths
    if len(path) == 0:
        min_paths = []

    path.append((i, j))

    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:

        min_length = math.inf

        path_len = w_len(maze, w, path)
        if len(min_paths) > 0:
            min_length = w_len(maze, w, min_paths[0])
            if min_length > path_len:
                min_paths = []

        if min_length >= path_len:
            min_paths.append(copy.deepcopy(path))

        path.remove((i, j))
        return min_paths

    maze[i][j] = maze[i][j]+2

    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] < 2:
            weighted_escapes(maze, w, a, b, path)

    maze[i][j] = maze[i][j]-2

    path.remove((i, j))

    return min_paths


# some test code
if __name__ == "__main__":
    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # should print 5
    print(fastest_escape_length(test_a))
    # should print 2
    print(weighted_escape_length(test_a, 0))
    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # should print inf
    print(fastest_escape_length(test_b))
    # should print 5
    print(weighted_escape_length(test_b, 1))
    # should print 6
    print(weighted_escape_length(test_b, 2))

    # should print [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    print(fastest_escapes(test_a))
    # should print []
    print(fastest_escapes(test_b))
    # should print [5, 5, 5, 5, 5, 5]
    print(list(map(len, fastest_escapes([[0 for _ in range(3)] for _ in range(3)]))))

    # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
    print(weighted_escapes(test_b, 0))
    # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # the order of the paths within the list might be different
    print(weighted_escapes(test_b, 2))