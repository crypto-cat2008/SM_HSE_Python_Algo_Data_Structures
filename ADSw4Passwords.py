def voc_to_list(vocabulary):
    """
    produces a list lengths such that lengths[i] is the number of
    words in length i in vocabulary
    """
    max_len = max([len(w) for w in vocabulary])
    lengths = [0] * (max_len + 1)
    for w in vocabulary:
        lengths[len(w)] += 1
    return lengths


def passwords(L, vocabulary):
    lengths = voc_to_list(vocabulary)
    print(lengths)

    # k is max word length
    k = len(lengths)
    print('k=', k)

    # this table has entry for every target password length
    # it appears to contain the function return, i.e. the number
    # of passwords for a given target length

    tbl = [0] * (L + 1)

    for i in range(L + 1):
        if i < k:
            # single word, exact fit - simply the number of
            # words that have this length
            tbl[i] = lengths[i]
        for j in range(min(k, i)):
            # try to add
            if lengths[j] > 0:
                # we have word(s) with length j
                tbl[i] += tbl[i-j-1]

    # the last value is the number of passwords for target length L
    print('tbl full', tbl)
    return tbl[-1]


# should print 2
print(passwords(34, ["a", "aa"]))
print()
