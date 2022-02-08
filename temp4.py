import math


def coins(n):
    # tbl[i] is going to contain the minimal number of coins to pay n cents
    tbl = [math.inf] * (n + 1)
    # tbl[0] = 0 as it should
    tbl[0] = 0
    for i in range(1, n + 1):
        # we always can take a one-cent coin and pay the remaining i - 1 cents
        tbl[i] = tbl[i - 1] + 1
        if i >= 3:
            # what if we can take 3-cent coin?
            tbl[i] = min(tbl[i], coins(n-i))
        if i >= 7:
            tbl[i] = min(tbl[i], coins(n-i))
        if i >= 8:
            tbl[i] = min(tbl[i], coins(n-i))

    return tbl[n]

# should print 3
print(coins(13))