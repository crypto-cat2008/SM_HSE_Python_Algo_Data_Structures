import math

def num_boxes(n):
    # tbl stores minimal number of boxes required for each n
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    for j in range(1, n + 1):
        i = 1
        # this goes through all box sizes and identifies minimal config
        while i**3 <= j:
            # we have tbl[1..j-1]. How to use it?
            # assume we try adding just one box of each size
            k = int(j / i**3)
            j1 = j - k * (i**3)
            left = tbl[j1] + k
            tbl[j] = min(tbl[j], left)
            i += 1
    return tbl[-1]

# should print 3
print(num_boxes(10))

def num_boxes_2(n):
    # tbl stores minimal number of boxes required for each n
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    for j in range(1, n + 1):
        i = 1
        # this goes through all box sizes and identifies minimal config
        while i**3 <= j:
            # we have tbl[1..j-1]. How to use it?
            # assume we try adding as many boxes of each size as we can
            boxes = int(j / i**3)
            left = j - boxes * (i**3)
            # lookup remainder in the table
            boxes += tbl[left]
            # select the lowest number of boxes found
            tbl[j] = min(tbl[j], boxes)
            i += 1
    print('tbl', tbl)
    return tbl[-1]

# should print 3
print(num_boxes_2(269))

def num_boxes_3(n):
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    # table "last" appears to contain the number of largest boxes
    # indexed by n
    last = [0] * (n + 1)
    for j in range(1, n + 1):
        i = 1
        while i**3 <= j:
            boxes = int(j / i**3)
            left = j - boxes * (i**3)
            boxes += tbl[left]
            if tbl[j] > boxes:
                tbl[j] = boxes
                last[j] = i
            i += 1
    # now build the list of box counts by taking the largest box count,
    # subtracting their volume from n, then using the remainder as new n, etc.
    cubes = []
    current = n
    while current > 0:
        # this prepends to the list to maintain order from
        # smallest box to largest
        cubes.insert(0, last[current])
        current -= last[current]**3
    # sanity check - boxes should fit exactly
    if current != 0:
        print("error")
        exit(1)
    print('tbl', tbl[-1], tbl[-2])
    return (len(cubes), cubes)

# should print (3, [1, 1, 2])
# the order of boxes might be different
print(num_boxes_3(238))

