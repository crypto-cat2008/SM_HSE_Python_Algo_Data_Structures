import math


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