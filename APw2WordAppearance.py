myDict = dict()
answer = list()
wordCount = 0

while True:
    input_line = input()

    if input_line == '':
        break
    else:
        words = input_line.split()
        for word in words:
            count = myDict.get(word, -1)
            if count == -1:
                myDict[word] = wordCount
                wordCount += 1
                answer.append(str(count))
            else:
                myDict[word] = wordCount
                wordCount += 1
                answer.append(str(count))

print(*answer, sep=' ')
