import itertools as it
a = [1,2,3,4,5,11,12,13,14]

c = it.combinations(a, 3)
count = 0
for i in c:
    if i[2] > 10:
        if i[0] < 10 and i[1] < 10:
            print(i)
            count += 1
        elif i[0] > 10 and i[1] > 10:
            print(i)
            count += 1

print(count)