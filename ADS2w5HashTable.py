def isAnagram(string1, string2):

    hash_table = dict()

    for char in string1:
        if char in hash_table:
            hash_table[char] +=1
        else:
            hash_table[char] = 1

    for char in string2:
        if char in hash_table:
            hash_table[char] -= 1
        else:
            hash_table[char] = 1

    for val in hash_table.values():
        if val != 0:
            return False

    return True

string1 = 'baa'
string2 = 'aab'

# check that your code works correctly on provided example
assert isAnagram(string1, string2), 'Wrong answer'

string1 = ''
string2 = ''

# check that your code works correctly on provided example
assert isAnagram(string1, string2), 'Wrong answer'

string1 = 'baa'
string2 = 'aabc'

# check that your code works correctly on provided example
assert not isAnagram(string1, string2), 'Wrong answer'

string1 = 'baac'
string2 = ''

# check that your code works correctly on provided example
assert not isAnagram(string1, string2), 'Wrong answer'

'''
----------------------------------------------------------------
'''

def longestNonRepeating(text):
    n = len(text)
    longest = 0
    curr = 0
    hash_table = set()

    for i in range(n):
        while text[i] in hash_table:
            hash_table.remove(text[curr])
            curr += 1
        hash_table.add(text[i])
        longest = max(longest, i - curr + 1)
    return longest


text = 'baa'

# check that your code works correctly on provided example
assert longestNonRepeating(text) == 2, 'Wrong answer'

text = ''
# check that your code works correctly on provided example
assert longestNonRepeating(text) == 0, 'Wrong answer'

text = 'as  ddffvvgg'
# check that your code works correctly on provided example
assert longestNonRepeating(text) == 3, 'Wrong answer'

'''
----------------------------------------------------------------
'''


def arrayIntersection(array1, array2):
    intersection = []
    hash_table = dict()

    for elem in array1:
        if elem in hash_table:
            hash_table[elem] += 1
        else:
            hash_table[elem] = 1

    for elem in array2:
        if elem in hash_table:
            intersection.append(elem)

    # print(intersection)

    return intersection

array1 = [1, 2, 3]
array2 = [2, 4, 5]

# check that your code works correctly on provided example
assert arrayIntersection(array1, array2) == [2], 'Wrong answer'

array1 = []
array2 = [2, 4, 5]

# check that your code works correctly on provided example
assert arrayIntersection(array1, array2) == [], 'Wrong answer'

array1 = [2, 2, 2, 2, 2]
array2 = [2, 4, 5]

# check that your code works correctly on provided example
assert arrayIntersection(array1, array2) == [2], 'Wrong answer'

array1 = [2, 4, 2, 5, 2, 5]
array2 = [2, 4, 5, 5]

# check that your code works correctly on provided example
assert arrayIntersection(array1, array2) == [2, 4, 5, 5], 'Wrong answer'