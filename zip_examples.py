def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
#
#
#
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

x2, y2 = zip(*zip(x, y)) # unzip the list
x == list(x2) and y == list(y2)