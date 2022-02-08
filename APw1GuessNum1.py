firstLine = True
maxGuessNum = 0
noSet = set()

while True:
    input_line = input()
    if firstLine:
        maxGuessNum = int(input_line.strip())
        yesSet = {int(x) for x in range(1, maxGuessNum + 1)}
        firstLine = False
    else:
        if input_line.strip().upper() == "HELP":
            break
        elif input_line.strip().upper() == "YES":
            yesSet &= inputSet
            inputSet.clear()
        elif input_line.strip().upper() == "NO":
            noSet |= inputSet
            inputSet.clear()
        else:
            inputSet = {int(x) for x in input_line.split()}

yesSet -= noSet
print(*sorted(yesSet), sep=' ')
