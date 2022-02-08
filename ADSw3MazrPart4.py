import math
import copy
global min_paths

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
