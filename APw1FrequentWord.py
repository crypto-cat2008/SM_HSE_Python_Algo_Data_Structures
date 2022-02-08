wordDict = dict()
maxCount = 0
answer = list()

while True:
    text_line = input()
    if text_line == '':
        break

    for word in text_line.split():
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

for value in wordDict.values():
    if value > maxCount:
        maxCount = value

for key, value in wordDict.items():
    if value == maxCount:
        answer.append(key)

print(min(answer), sep=' ')
