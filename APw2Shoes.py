custShoeSize = int(input())
inputSizes = input().split()
sizesInStore = [int(i) for i in inputSizes if int(i) >= custShoeSize]
smallestSize = True
count = 0

sizesInStore.sort()

for shoe in sizesInStore:
    if smallestSize:
        custShoeSize = shoe
        smallestSize = False
        count = 1
    else:
        if shoe - custShoeSize >= 3:
            custShoeSize = shoe
            count += 1

print(count)
