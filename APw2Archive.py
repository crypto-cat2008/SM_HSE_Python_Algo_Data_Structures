input_line = input()
diskSize, numOfUsers = input_line.split(maxsplit=1)
sizes = []
totalSize = 0
count = 0

for user in range(0, int(numOfUsers)):
    userFileSize = int(input())
    sizes.append(userFileSize)

sizes.sort()

for item in sizes:
    totalSize += item
    if totalSize <= int(diskSize):
        count += 1
    else:
        break

print(count)
