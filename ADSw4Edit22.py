import math


def dump_edit_path(A, B, D):

    i = len(A)
    j = len(B)

    n = 0
    while i > 0 or j > 0:
        n += 1
        print(str(n) + ". at row", i + 1, "col", j + 1)

        current = D[i][j]
        upper_left = D[i - 1][j - 1]
        if upper_left == current:
            # equal
            print("equal", A[i - 1])
            i -= 1
            j -= 1
        else:
            if j == 0:
                # no cell to the left. move up
                print("delete1", A[i - 1])
                i -= 1
            elif j == 0:
                # no cell above, move left
                print("insert1", B[j - 1])
                j -= 1
            else:
                to_left = D[i][j - 1]
                to_up = D[i - 1][j]
                if upper_left < to_left and upper_left < to_up:
                    # substitution
                    print("subst", A[i - 1], "with", B[j - 1])
                    i -= 1
                    j -= 1
                elif to_left < to_up:
                    # move left
                    print("insert2", B[j - 1])
                    j -= 1
                else:
                    # move up
                    print("delete2", A[i - 1])
                    i -= 1


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

    print("      " + " ".join(B))
    print("   -" + "-" * (m + 1) * 2)
    for i in range(0, n + 1):
        s = ""
        for j in range(0, m + 1):
            s = s + ' ' + str(D[i][j])
        if i == 0:
            print('  |'+s)
        else:
            print(A[i-1]+' |'+s)

    # print("\n".join([str(l) for l in D]), '\n')
    # dump_edit_path(A, B, D)

    return D


def weighted_edistance2(A, B, wdel, wins, wsub):
    n = len(A)
    m = len(B)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    for i1, j1 in enumerate(D):
        if i1 == 0:
            for k1, m1 in enumerate(j1):
                D[i1][k1] = k1 * wins
        else:
            D[i1][0] = i1 * wdel

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]

            else:
                to_up = D[i - 1][j]
                to_left = D[i][j - 1]
                to_ul = D[i - 1][j - 1]

                # print("to_ul, to_left, to_up", to_ul, to_left, to_up)
                if to_ul < to_up and to_ul < to_left:
                    v = to_ul + wsub
                elif to_left < to_up:
                    v = to_left + wins
                else:
                    v = to_up + wdel

                D[i][j] = v

    """
    print("      " + " ".join(B))
    print("   -" + "-" * (m + 1) * 2)
    for i in range(0, n + 1):
        s = ""
        for j in range(0, m + 1):
            s = s + ' ' + str(D[i][j])
        if i == 0:
            print('  |'+s)
        else:
            print(A[i - 1]+' |'+s)


    #print("\n".join([str(l) for l in D]), '\n')
    #dump_edit_path(A, B, D)
    """

    return D


def weighted_edistance1(A, B, wdel, wins, wsub):

    D = edistance(A, B)
    # W = [wins, wsub, wdel]
    DW = [0, 0, 0]
    i = len(A)
    j = len(B)
    result = 0

    while i > 0 or j > 0:
        # print('i, j', i, j)

        if i == 1 and j == 1:
            break

        if j > 0:
            DW[0] = (D[i][j - 1]) * wins  # left
        else:
            DW[0] = math.inf  # left

        if i > 0 and j > 0:
            DW[1] = (D[i - 1][j - 1]) * wsub  # diagonal
        else:
            DW[1] = math.inf
        if i > 0:
            DW[2] = (D[i - 1][j]) * wdel  # up
        else:
            DW[2] = math.inf

        min_value = min(DW)

        for a, b in enumerate(DW):
            if b > min_value:
                DW[a] = math.inf

        # print(DW)

        # DW = [a * b for a, b in zip(DW, W)]

        min_index = DW.index(min(DW))
        # print('min_index', min_index)

        if min_index == 0:
            result += 1
            j -= 1
            if j < 0:
                break
            # print('left', result, i, j, '\n')

        elif min_index == 1:
            result += 1
            i -= 1
            j -= 1
            # print('diagonal', result, i, j, '\n')

        else:
            result += 1
            i -= 1
            # print('up', result, i, j, '\n')

    return result


def weighted_edistance(A, B, wdel, wins, wsub):
    i = len(A)
    j = len(B)

    # print("wdel, wins, wsub", wdel, wins, wsub)
    D = weighted_edistance2(A, B, wdel, wins, wsub)

    n = 0
    result = 0
    while i > 0 or j > 0:
        n += 1
        # print(str(n) + ". at row", i + 1, "col", j + 1)

        if i > 0 and j > 0 and D[i - 1][j - 1] == D[i][j]:
            # equal
            # print("equal", A[i - 1])
            i -= 1
            j -= 1
        else:
            if j == 0:
                # no cell to the left. move up
                # print("delete1", A[i - 1])
                i -= 1
                result += wdel
            elif i == 0:
                # no cell above, move left
                # print("insert1", B[j - 1])
                j -= 1
                result += wins
            else:
                to_left = D[i][j - 1] + wins
                to_up = D[i - 1][j] + wdel
                to_ul = D[i - 1][j - 1] + wsub
                # print("to_ul, to_left, to_up", to_ul, to_left, to_up)
                if to_ul < to_left and to_ul < to_up:
                    # substitution
                    # print("subst", A[i - 1], "with", B[j - 1])
                    i -= 1
                    j -= 1
                    result += wsub
                elif to_left < to_up:
                    # move left
                    # print("insert2", B[j - 1])
                    j -= 1
                    result += wins
                else:
                    # move up
                    # print("delete2", A[i - 1])
                    i -= 1
                    result += wdel

    return result
