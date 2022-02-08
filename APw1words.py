wordDict = {}
answer = []

while True:
    input_line = input().strip()

    if input_line == '':
        break
    else:
        words = input_line.split()
        for word in words:
            if word in wordDict:
                count = wordDict[word] + 1
                wordDict[word] = count
                answer.append(count)
            else:
                wordDict[word] = 0
                answer.append(0)

print(*answer, sep=' ')
