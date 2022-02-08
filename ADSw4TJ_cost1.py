import math
import random


def tj_cost(L, W):
    n = len(W)
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0

    for i in range(1, n + 1):
        length = -1
        for j in range(i - 1, -1, -1):
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            elif i == len(W):
                P = 0
            else:
                P = (L - length) ** 3

            if tbl[j] + P < tbl[i]:
                tbl[i] = tbl[j] + P

    return tbl[n]
