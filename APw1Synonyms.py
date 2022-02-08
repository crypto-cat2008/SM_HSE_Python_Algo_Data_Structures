n = int(input())
wordDict = {}

for n in range(1, n + 1):
    input_line = input().split()
    wordDict[input_line[0]] = input_line[1]
    wordDict[input_line[1]] = input_line[0]

input_line = input().strip()

print(wordDict[input_line])
