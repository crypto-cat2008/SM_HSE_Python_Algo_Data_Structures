upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
wordDict = dict()
errorCount = 0

n = int(input())

for i in range(1, n + 1):
    word = input().strip()
    wordDict[word] = word.lower()

phrase = input().split()

for word in phrase:
    stressCount = 0

    for letter in word:
        if letter in upperCaseLetters:
            stressCount += 1

    if stressCount == 0:
        errorCount += 1
        continue

    if word in wordDict:
        continue
    else:
        if stressCount > 1:
            errorCount += 1
        else:
            if word.lower() in wordDict.values():
                errorCount += 1

print(errorCount)
