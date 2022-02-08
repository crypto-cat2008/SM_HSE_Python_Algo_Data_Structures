
firstRow = True
totalCount = 0
parsed_data = list()
maleCount = 0
femaleCount = 0
parchCount = 0
firstClassCount = 0
survCount = 0
firstClassAndSur = 0
totalAge = 0
ageCount = 0
ageList = []
ageDict = dict()
totalFare = 0
fareList = []
fareCountAboveAvg = 0

with open("titanic.csv") as f:
    data = f.readlines()
    for line in data:
        if firstRow:
            firstRow = False
        else:
            totalCount += 1
            a= line.rstrip()
            b = a.split(',')
            parsed_data.append(b)

for line in parsed_data:
    if line[5] == 'male':
        maleCount += 1
    elif line[5] == 'female':
        femaleCount += 1

    if int(line[8]) > 0:
        parchCount += 1

    if int(line[2]) == 1:
        firstClassCount += 1

    if int(line[1]) == 1:
        survCount += 1

    if int(line[2]) == 1 and int(line[1]) == 1:
        firstClassAndSur += 1

    try:
        totalAge += float(line[6])
        ageCount += 1
        ageList.append(float(line[6]))
        if float(line[6]) not in ageDict:
            ageDict[int(line[6])] = 1
        else:
            ageDict[int(line[6])] += 1
    except ValueError:
        pass

    totalFare += float(line[10])
    fareList.append(float(line[10]))

sortedAgeList = sorted(ageList)
avgFare = round(totalFare / totalCount, 2)

for i in fareList:
    if i > avgFare:
        fareCountAboveAvg += 1

#print('male count ', maleCount, 'female count', femaleCount, 'parch count', parchCount)
print('first class percent', round((firstClassCount*100)/totalCount,2))
#print('survivors percent', round((survCount*100)/totalCount,2))
#print('first class survivors percent', round((firstClassAndSur*100)/firstClassCount,2))
print('Avrg age', round(totalAge/ageCount, 2), ageCount)
#print(sortedAgeList[343],sortedAgeList[344],sortedAgeList[345])
#print(sorted(ageDict.items(), key=lambda x: -x[1]))
#print(fareList)
#print('fare count above avrg', fareCountAboveAvg)
print('first class count', firstClassCount)
print('survivor count', survCount)
print('first class surv', firstClassAndSur)