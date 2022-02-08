def largest_palindrome(s):

    if len(s) < 1:
        return ''
    elif len(s) == 1:
        return s

    results = []
    min_index = 0
    max_index = len(s) - 1

    middle_letter = s[0]
    results.append(middle_letter)
    biggest_size = 1
    found_one = False

    for i in range(len(s)):
        # check even
        left = i - 1
        right = i + 1

        while left >= min_index and right <= max_index:
            if s[left] == s[right]:
                # print('even', s[left], s[right], left, i, right)
                found_one = True
                left -= 1
                right += 1
            else:
                break

        if right - left > biggest_size and found_one:
            # print(right - left, s[left + 1: right], left, right)
            results.append(s[left + 1: right])
            biggest_size = right - left - 1
            found_one = False

        # check odd
        left = i
        right = i + 1
        while left >= min_index and right <= max_index:
            if s[left] == s[right]:
                # print('odd', s[left], s[right], left, i, right)
                left -= 1
                right += 1
                found_one = True
            else:
                break

        if right - left - 1 > biggest_size:
            results.append(s[left + 1: right])
            biggest_size = right - left - 1
            found_one = False

    # print(results)
    return results[-1]
