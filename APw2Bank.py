bankDict = dict()
command = []
answer = []

while True:
    input_line = input()

    if input_line == '':
        break
    else:
        command = input_line.split()
        if command[0] == 'DEPOSIT':
            if command[1] not in bankDict:
                bankDict[command[1]] = int(command[2])
            else:
                bankDict[command[1]] += int(command[2])
            pass
        if command[0] == 'WITHDRAW':
            if command[1] not in bankDict:
                bankDict[command[1]] = 0
            bankDict[command[1]] -= int(command[2])
        if command[0] == 'TRANSFER':
            if command[1] not in bankDict:
                bankDict[command[1]] = 0
            if command[2] not in bankDict:
                bankDict[command[2]] = 0
            bankDict[command[1]] -= int(command[3])
            bankDict[command[2]] += int(command[3])
        if command[0] == 'BALANCE':
            answer.append(bankDict.get(command[1], 'ERROR'))
        if command[0] == 'INCOME':
            percentToAdd = int(command[1])
            for account in bankDict:
                accountBalance = bankDict[account]
                if accountBalance >= 0:
                    bankDict[account] += int(accountBalance*percentToAdd/100)

print(*answer, sep='\n')
