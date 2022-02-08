import json
numOfWords = int(input())
words = []
answer = dict()

for i in range(numOfWords):
    words.append(input())

outputFile = input()

for word in sorted(words):
    if word[0] not in answer:
        answer[word[0]] = {}
        value = answer[word[0]]
    else:
        value = answer[word[0]]

    if word[0:2] not in value:
        value[word[0:2]] = []
        value[word[0:2]].append(word)
    else:
        value[word[0:2]].append(word)

with open(outputFile, 'w') as f:
    json_str = json.dumps(answer)
    f.write(json_str)
