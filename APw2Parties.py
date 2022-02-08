partiesDict = dict()
partiesList = list()
answer = list()
votesFlag = False
totalVotes = 0

input_line = input()

while True:
    input_line = input()
    if input_line == '':
        break

    if input_line == 'VOTES:':
        votesFlag = True
        continue

    if votesFlag:
        partiesDict[input_line] += 1
    else:
        partiesDict[input_line] = 0
        partiesList.append(input_line)

for party in partiesDict:
    totalVotes += partiesDict[party]

for party in partiesList:
    percentToPass = int(partiesDict[party]*100/totalVotes)
    if percentToPass >= 7:
        print(party)
