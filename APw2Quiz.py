def calculate_comparison_value(number):
    numLenght = len(number)
    value = 0
    numberReverse = number[::-1]
    for i in range(0, int(numLenght/2)):
        value += int(number[i]) - int(numberReverse[i])

    return value


count = int(input())
numbers = list()

for i in range(0, count):
    number = input()
    numbers.append((number, calculate_comparison_value(number)))

numbers.sort(key=lambda x: (x[1], abs(int(x[0]))))
for item in numbers:
    print(item[0], sep='\n')
