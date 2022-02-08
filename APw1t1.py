userInput = input().split()
numbers = set()
answerYes = 'YES'
answerNo = 'NO'
lenOfNumbers = 0

for i in userInput:
    numbers.add(i)
    newLenOfNumbers = len(numbers)
    if newLenOfNumbers > lenOfNumbers:
        print(answerNo)
        lenOfNumbers = newLenOfNumbers
    else:
        print(answerYes)
