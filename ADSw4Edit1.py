import math


def edistance(A, B):
    n = len(A)
    m = len(B)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    for i1, j1 in enumerate(D):
        if i1 == 0:
            for k1, m1 in enumerate(j1):
                D[i1][k1] = k1
        else:
            D[i1][0] = i1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:

                D[i][j] = D[i - 1][j - 1]
            if A[i - 1] != B[j - 1]:

                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])

    # print("\n".join([str(l) for l in D]))
    return D[-1][-1]
