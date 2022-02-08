import math
import copy
global min_paths


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
