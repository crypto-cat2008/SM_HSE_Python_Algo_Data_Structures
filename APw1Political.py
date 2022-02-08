input_line = input().split()
numOfDays = int(input_line[0])
numOfParties = int(input_line[1])
strikes = [[] for numOfDays in range(numOfParties)]
a = [i for i in range(1, numOfDays + 1)]
weekends = []
correctDays = []
correctDaysSet = {}

for n in range(0, numOfDays, 7):
    weekends.append(a[n:n+5])

for i in weekends:
    correctDays += i

correctDaysSet = set(correctDays)

for i in range(0, numOfParties):
    input_line = input().split()
    dayOne = int(input_line[0])
    interval = int(input_line[1])

    strikeDay = dayOne
    strikes[i].append(strikeDay)
    moreDays = True

    while moreDays:
        strikeDay = strikeDay + interval
        if strikeDay <= numOfDays:
            strikes[i].append(strikeDay)
        else:
            moreDays = False

firstItem = True
for item in strikes:
    if firstItem:
        firstItem = False
        answer1 = set(item)
    else:
        answer1 |= set(item)

answer = answer1 & correctDaysSet

print(len(answer))
