firstLine = True
maxGuessNum = 0
answers = []
guessSet = set()

while True:
    input_line = input()
    if firstLine:
        maxGuessNum = int(input_line.strip())
        possibleSet = {int(x) for x in range(1, maxGuessNum + 1)}
        firstLine = False
    else:
        if input_line.strip().upper() == "HELP":
            break
        else:
            guessSet = {int(x) for x in input_line.split()}
            difSet = possibleSet - guessSet
            interSet = possibleSet & guessSet
            if len(difSet) < len(interSet):
                answers.append("YES")
                possibleSet &= guessSet
                guessSet.clear()
            else:
                answers.append("NO")
                possibleSet -= guessSet
                guessSet.clear()

print(*answers, sep='\n')
print(*sorted(possibleSet), sep=' ')
