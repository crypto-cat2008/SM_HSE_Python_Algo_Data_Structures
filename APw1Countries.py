n = int(input())
citiesDict = {}

for i in range(1, n + 1):
    input_line = input().split()
    for i, j in enumerate(input_line):
        if i > 0:
            citiesDict[j] = input_line[0]

n = int(input())
answer = []
for i in range(1, n + 1):
    input_line = input()
    answer.append(citiesDict[input_line])

print(*answer, sep='\n')
