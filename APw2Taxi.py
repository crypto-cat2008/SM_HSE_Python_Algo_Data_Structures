distances = [int(x) for x in input().split()]
fares = [int(x) for x in input().split()]
total = 0

distances.sort(reverse=True)
fares.sort()

for distance, fare in zip(distances, fares):
    total += distance * fare

print(total)
