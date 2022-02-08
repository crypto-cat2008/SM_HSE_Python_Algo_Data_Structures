unique_elements_set = set()

while True:
    input_line = input()
    if input_line == '':
        break

    list_item = int(input_line)
    unique_elements_set.add(list_item)

print(len(unique_elements_set))

input_list = [int(x) for x in input().split()]
unique_elements_set = set(input_list)
print(len(unique_elements_set))

import sys


unique_elements_set = set()

for input_line in sys.stdin:
    input_line = input_line.rstrip('\n')

    if input_line == '':
        break

    list_item = int(input_line)
    unique_elements_set.add(list_item)

print(len(unique_elements_set))

import sys


lines = []
for input_line in sys.stdin:
    lines.append(input_line)

print(lines)

words = input().split()
unique_words_set = set(words)
print(len(unique_words_set))

print(*sorted(container), sep='\n')

container = {7, 1, 4, 3, 2}
print(*sorted(container), sep=' ')  # '1 2 3 4 7'



