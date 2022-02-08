def countingsort(array, lowerbound, upperbound):
    sorted_array = []
    count = [0 for _ in range(lowerbound, upperbound + 1)]

    for elem in array:
        count[elem - lowerbound] += 1

    for i, elem in enumerate(count):
        item = [(lowerbound + i) for _ in range(elem)]
        sorted_array.extend(item)

    # print(sorted_array)

    return sorted_array


arr = [3, 2, 1]
lowerbound = 1
upperbound = 3
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [1, 2, 3], 'Wrong answer'

arr = []
lowerbound = 0
upperbound = 10
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [], 'Wrong answer'

arr = [5, 2]
lowerbound = 2
upperbound = 5
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [2, 5], 'Wrong answer'

arr = [1, 2, 2, 1, 1, 1, 12]
lowerbound = 1
upperbound = 33
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [1, 1, 1, 1, 2, 2, 12], 'Wrong answer'


arr = [76, 43, 56, 12, 1, 4, 99]
lowerbound = 1
upperbound = 99
# check that your code works correctly on provided example
assert countingsort(arr, lowerbound, upperbound) == [1, 4, 12, 43, 56, 76, 99], 'Wrong answer'
'''
-------------------------------------------------------------------------
'''


def countingsort_expanded(array, char_count):
    sorted_array = []
    count = [[] for _ in range(100)]

    for elem in array:
        count[ord(elem[char_count]) - 32].append(elem)

    for elem in count:
        if len(elem) > 0:
            sorted_array.extend(elem)

    return sorted_array


def radixsort(names):
    n = len(names)
    names_padded = []

    if n == 0:
        return names

    # find max len
    max_len = len(max(names, key=len))

    # pad to max length
    for item in names:
        name_padded = item.rjust(max_len, ' ')
        names_padded.append(name_padded)

    for i in range(max_len - 1, -1, -1):
        names_padded = countingsort_expanded(names_padded, i)
        # print(i, names_padded)

    return names_padded


arr = ['Ivan', 'John', 'Anna']
# check that your code works correctly on provided example
assert radixsort(arr) == ['Anna', 'Ivan', 'John'], 'Wrong answer'
