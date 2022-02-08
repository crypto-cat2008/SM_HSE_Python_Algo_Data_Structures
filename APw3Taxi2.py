distances = sorted(
            map(lambda x: (x[1], x[0]),
                enumerate(map(int, input().split()))
                ),
            )

fares = sorted(
            map(lambda x: (x[1], x[0]),
                enumerate(map(int, input().split()))
                ),
            reverse=True
            )

match = map(lambda x: (x[0][1], x[1][1]), zip(distances, fares))
print(*map(lambda x: x[1], sorted(match)))
