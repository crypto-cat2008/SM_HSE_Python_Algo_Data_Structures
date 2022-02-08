input_line = input().strip()
numOfStudents = int(input_line)
students = [[] for j in range(numOfStudents)]

for i in range(0, numOfStudents):
    numOfLanguages = int(input().strip())

    for j in range(0, numOfLanguages):
        input_line = input().strip()
        students[i].append(input_line)

firstItem = True
for item in students:
    if firstItem:
        firstItem = False
        answer1 = set(item)
    else:
        answer1 &= set(item)

print(len(answer1), *sorted(answer1), sep='\n')
