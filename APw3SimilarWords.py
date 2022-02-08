words = input().split()
scores = map(float, input().split())
myArray = filter(
    lambda x: x[0] > 0.5,
    sorted(
        zip(scores, words),
        key=lambda x: (-x[0], x[1])
        )
    )
print(*map(lambda x: x[1], myArray), sep='\n')
