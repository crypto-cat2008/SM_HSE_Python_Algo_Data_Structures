words = dict()
line = list()
wordsList = list()

while True:
    input_line = input()
    if input_line == '':
        break
    else:
        line = input_line.split()
        for word in line:
            count = words.setdefault(word, 0)
            words[word] += 1

for key, value in words.items():
    wordsList.append((key, value))

wordsList.sort()
words = dict(wordsList)
print(*sorted(words, key=lambda x: words[x], reverse=True), sep='\n')
