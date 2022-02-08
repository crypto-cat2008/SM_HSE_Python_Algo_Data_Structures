numOfWords = int(input())
words = list()

for i in range(0, numOfWords):
    word = input()
    words.append(word)

words.sort(key=lambda x: (len(x), ''.join(reversed(x))))
print(*words, sep='\n')
