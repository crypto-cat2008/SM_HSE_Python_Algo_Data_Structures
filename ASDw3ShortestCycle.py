def prefixFunction(text):
    n = len(text)
    prefix = [0 for i in range(n)]

    for i in range(1, n):

        x = prefix[i - 1]

        while x > 0 and text[i] != text[x]:
            x = prefix[x - 1]

        if text[i] == text[x]:
            prefix[i] = x + 1

    return prefix

def KMP(text, pattern):
    indices = []

    s = pattern + "#" + text  # "#"should not be in the text
    n = len(pattern)  # n is what we are looking for in prefix array

    prefix = prefixFunction(s)

    for i in range(n + 1, len(prefix)):
        if prefix[i] == n:
            indices.append(i - (n + 1) - n + 1)  # start of found pattern - this can be replaces with (i -2 * n)

    return indices

def check_positions(positions, pattern_len, s):

    result = [False for i, j in enumerate(positions)]

    for i, p in enumerate(positions):
        if p[0] + pattern_len == p[1]:
            result[i] = True

    if False in result:
        return False
    else:
        # print(positions, positions[-1], positions[-1][1], pattern_len, len(s))
        if positions[-1][1] + pattern_len == len(s):
            return True
        else:
            return False

    return result


def shortestCycle(cyclic_string):

    if len(cyclic_string) == 0:  # return 0 if string is empty
        return 0

    for i in range(len(cyclic_string)):  # for all substrings starting with 1 char

        pattern = cyclic_string[0:i + 1]
        pattern_len = len(pattern)
        result = KMP(cyclic_string, pattern)
        # print('kmp result', result)

        if len(result) > 1:     # if we found something, check if it can be repeated
            # print(result, cyclic_string[0:i + 1], i)
            positions = list(zip(result, result[1:]))

            if check_positions(positions, pattern_len, cyclic_string):
                return pattern_len

    return len(cyclic_string)


cyclic_string = 'ee5Gd1Z9c8IMOoitqnWnLsRbbxdgvFIRr8UJo0XPg9ra'
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 44, 'Wrong answer'

cyclic_string = 'ababab'
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 2, 'Wrong answer'

cyclic_string = 'abcd'
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 4, 'Wrong answer'

cyclic_string = 'abcdabcdabcdabcdabcdabcdabcdabcd'
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 4, 'Wrong answer'

cyclic_string = ''
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 0, 'Wrong answer'


cyclic_string = 'ababadbababa'
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 12, 'Wrong answer'



import random

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for i in range(1000):
    n = random.randint(1, len(s))
    repeat = random.randint(0, len(s))
    # randomly choice letter from s to build cyclic_string
    cyclic_string = ''.join([random.choice(s) for _ in range(n)]) * repeat
    ans = n if repeat != 0 else 0
    ans1 = shortestCycle(cyclic_string)
    if ans1 != ans:
        print(cyclic_string, ans1, ans)
