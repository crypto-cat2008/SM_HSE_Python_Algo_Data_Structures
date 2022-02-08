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


text = 'abracadabra'
# check that your code works correctly on provided example
assert prefixFunction(text) == [0, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4], 'Wrong answer'


def KMP(text, pattern):
    indices = []

    s = pattern + "#" + text  # "#"should not be in the text
    n = len(pattern)  # n is what we are looking for in prefix array

    prefix = prefixFunction(s)

    for i in range(n + 1, len(prefix)):
        if prefix[i] == n:
            indices.append(i - (n + 1) - n + 1)  # start of found pattern - this can be replaces with (i -2 * n)

    return indices


text = 'abracadabra'
pattern = 'ab'
# check that your code works correctly on provided example
assert KMP(text, pattern) == [0, 7], 'Wrong answer'

# original_string = 'abcde'
# shifted_string = 'deabc'
# print('kpm', KMP(shifted_string + shifted_string, original_string))


def zFunction(text):
    n = len(text)
    z = [0 for i in range(n)]

    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)

        while i + z[i] < n and text[z[i] + i] == text[z[i]]:
            z[i] += 1

        new_r = i + z[i] - 1
        if new_r > r:
            l, r = i, new_r

    return z

text = 'abracadabra'
# check that your code works correctly on provided example
assert zFunction(text) == [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1], 'Wrong answer'


def zAlgorithm(text, pattern):
    n, m = len(text), len(pattern)
    special_symbol = "#"
    indices = []

    s = pattern + special_symbol + text

    z = zFunction(s)

    for i in range(m + 1, len(s)):
        if z[i] == m:
            indices.append(i - m - 1)

    return indices


text = 'abracadabra'
pattern = 'ab'
# check that your code works correctly on provided example
assert zAlgorithm(text, pattern) == [0, 7], 'Wrong answer'



def order(c):
    return ord(c) - ord('a') + 1


def RabinKarp(text, pattern):
    n, m = len(text), len(pattern)
    p, q = 31, 10 ** 9 + 7
    indices = []

    if m == 0 or n < m:
        return indices

    p_pow = 1
    for i in range(m - 1):
        p_pow = (p_pow * p) % q

    pattern_hash = 0
    window_hash = 0

    for i in range(m):
        pattern_hash = (pattern_hash * p + order(pattern[i])) % q
        window_hash = (window_hash * p + order(text[i])) % q

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            match = True

            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break

            if match:
                indices.append(i)

        if i < n - m:
            window_hash = (window_hash - order(text[i]) * p_pow) % q
            window_hash = (window_hash * p + order(text[i + m])) % q
            window_hash = (window_hash + q) % q

    return indices


text = 'abracadabra'
pattern = 'ab'
# check that your code works correctly on provided example
answer = RabinKarp(text, pattern)
# print(answer)
assert answer == [0, 7], 'Wrong answer'

text = 'abracadabra'
pattern = ''
# check that your code works correctly on provided example
answer = RabinKarp(text, pattern)
# print(answer)
assert answer == [], 'Wrong answer'

text = 'zabracadabra'
pattern = 'abracadabra'
# check that your code works correctly on provided example
answer = RabinKarp(text, pattern)
# print(answer)
assert answer == [1], 'Wrong answer'

text = 'abr'
pattern = 'aabracadabra'
# check that your code works correctly on provided example
answer = RabinKarp(text, pattern)
# print(answer)
assert answer == [], 'Wrong answer'


def minCyclicShift(original_string, shifted_string):
    min_shift = -1

    if len(original_string) != len(shifted_string):
        return -1
    if original_string == shifted_string:
        return 0

    text = shifted_string + shifted_string

    result = KMP(text, original_string)

    if len(result) != 0:
        min_shift = result[0]

    return min_shift


original_string = 'abcde'
shifted_string = 'deabc'
# check that your code works correctly on provided example
assert minCyclicShift(original_string, shifted_string) == 2, 'Wrong answer'

original_string = 'abcde'
shifted_string = 'bcdea'
# check that your code works correctly on provided example
answer = minCyclicShift(original_string, shifted_string)
# print(answer)
assert answer == 4, 'Wrong answer'

original_string = 'abcde'
shifted_string = 'abcde'
# check that your code works correctly on provided example
answer = minCyclicShift(original_string, shifted_string)
# print(answer)
assert answer == 0, 'Wrong answer'

original_string = ''
shifted_string = ''
# check that your code works correctly on provided example
answer = minCyclicShift(original_string, shifted_string)
# print(answer)
assert answer == 0, 'Wrong answer'

def check_positions(positions, len):

    result = [False for i, j in enumerate(positions)]

    for i, p in enumerate(positions):
        if p[0] + len == p[1]:
            result[i] = True

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

            checks = check_positions(positions, pattern_len)
            # print(checks)
            if False not in checks:
                return pattern_len

    return len(cyclic_string)


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

cyclic_string = 'bbbbbbbbbbbbbbbbbb'
# check that your code works correctly on provided example
answer = shortestCycle(cyclic_string)
assert answer == 1, 'Wrong answer'

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
    assert shortestCycle(cyclic_string) == ans