def modify_list(a):

    removeIndex = []

    for i in a:
        if i % 2 != 0:
            removeIndex.append(i)

    for i in removeIndex:
        a.remove(i)

    for i, j in enumerate(a):
        newValues = int(j/2)
        a.insert(i, newValues)
        a.remove(j)
