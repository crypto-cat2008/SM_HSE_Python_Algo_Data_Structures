import math
import random
import time


def find_median(a, a0, a_len, b, b0, b_len):

    if a_len < b_len:
        min_index = 0
        max_index = a_len

        while min_index <= max_index:

            i = (min_index + max_index) // 2
            j = ((a_len + b_len) // 2) - i

            max_left_a = -math.inf if i == 0 else a[i - 1 + a0]
            min_right_a = math.inf if i == a_len else a[i + a0]

            max_left_b = -math.inf if j == 0 else b[j - 1 + b0]
            min_right_b = math.inf if j == b_len else b[j + b0]

            if i < a_len and j > 0 and max_left_b > min_right_a:
                min_index = i + 1

            elif i > 0 and j < b_len and min_right_b < max_left_a:
                max_index = i - 1

            else:
                if i == 0:
                    return max_left_b, i, j

                if j == 0:
                    return max_left_a, i, j
                else:
                    return max(max_left_a, max_left_b), i, j
    else:
        min_index = 0
        max_index = b_len

        while min_index <= max_index:

            i = (min_index + max_index) // 2
            j = ((a_len + b_len) // 2) - i

            max_left_b = -math.inf if i == 0 else b[i - 1 + b0]
            min_right_b = math.inf if i == b_len else b[i + b0]

            max_left_a = -math.inf if j == 0 else a[j - 1 + a0]
            min_right_a = math.inf if j == a_len else a[j + a0]

            if i < b_len and j > 0 and max_left_a > min_right_b:
                min_index = i + 1

            elif i > 0 and j < a_len and min_right_a < max_left_b:
                max_index = i - 1

            else:
                if i == 0:
                    return max_left_a, j, i

                if j == 0:
                    return max_left_b, j, i
                else:
                    return max(max_left_a, max_left_b), j, i


def find_percentile(a, b, p):

    k_float = p / 100 * (len(a) + len(b))  # ordinal rank

    if k_float.is_integer():
        k = int(k_float)
    else:
        k = math.floor(k_float) + 1

    a_len = len(a)
    b_len = len(b)
    a0 = 0
    b0 = 0

    while True:

        # end of recursion - one element left
        if a_len == 1 and b_len == 0:
            return a[0 + a0]
        if a_len == 0 and b_len == 1:
            return b[0 + b0]

        # otherwise keep splitting
        (value, i, j) = find_median(a, a0, a_len, b, b0, b_len)

        if i + j == k:
            return value
        elif i + j < k:  # k is in left part
            a0 += i
            b0 += j
            a_len -= i
            b_len -= j
            count_discarded = i + j
            k -= count_discarded
        else:           # k is in right part
            a_len = i
            b_len = j


def test_percentile(test_arr1, test_arr2, test_p, answer):
    random.seed(int(time.time()))
    percentile_result = find_percentile(test_arr1, test_arr2, test_p)
    error_str = 'Test failed!\nInput: {0}, {1}, {2}\nOutput: {3}\nCorrect output: {4}'
    assert percentile_result == answer, error_str.format(test_arr1, test_arr2, test_p, percentile_result, answer)


def run_unit_test():
    test_percentile([15, 15, 15], [12, 12, 12, 12], 50, 12)
    test_percentile([101, 118, 138, 175], [7, 11, 21, 45, 65], 91, 175)
    test_percentile([1], [], 50, 1)
    test_percentile([], [1], 50, 1)
    test_percentile([1], [0], 50, 0)
    test_percentile([1], [2, 3], 50, 2)
    test_percentile([2, 3], [1], 50, 2)
    test_percentile([], [1, 2, 3], 50, 2)
    test_percentile([1, 2, 7, 8, 10], [6, 12], 50, 7)
    test_percentile([15, 20, 35, 40, 50], [], 30, 20)
    test_percentile([15, 20], [25, 40, 50], 40, 20)
    test_percentile([55], [25, 40, 50], 20, 25)
    test_percentile([15], [25, 40, 50], 5, 15)
    test_percentile([15, 20], [25, 40, 50], 70, 40)
    test_percentile([15, 20, 55], [12, 25, 40, 50], 100, 55)
    test_percentile([15, 20, 55], [12, 25, 40, 50], 1, 12)
    print("Unit tests passed!")


def get_random_test(test_size1, test_size2, max_int1):
    a = []
    b = []

    if test_size1 == 0 and test_size2 == 0:  # don't need to test 0,0
        return [1], [1], 1
    else:
        for i in range(test_size1):
            a.append(random.randint(0, max_int1))
        for i in range(test_size2):
            b.append(random.randint(0, max_int1))
        return sorted(a), sorted(b), random.randint(1, 100)


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        index = partition(arr, l, r)
        if index - l == k - 1:
            return arr[index]

        if index - l > k - 1:
            return kthSmallest(arr, l, index - 1, k)

        return kthSmallest(arr, index + 1, r,
                           k - index + l - 1)
    print("Index out of bound")


def run_stress_test(max_test_size=20, max_attempts=10, max_right_border=10):
    # random.seed(100)
    random.seed(int(time.time()))

    for test_size1 in range(0, max_test_size):
        for test_size2 in range(max_test_size, -1, -1):
            print('test_size = ', test_size1, test_size2)
            for right_border in range(0, max_right_border):
                for attempt in range(max_attempts):
                    a, b, p = get_random_test(test_size1, test_size2, 200)
                    k_float = p / 100 * (len(a) + len(b))  # ordinal rank
                    if k_float.is_integer():
                        k = int(k_float)
                    else:
                        k = math.floor(k_float) + 1
                    test_percentile(a, b, p, kthSmallest(a+b, 0, len(a+b)-1, k))

    print('Stress test passed!')

# Array a len: 1000000 Array b len: 1000000 Max int in both arrays: 42
# find_percentile runs in  0.000995 seconds


def run_max_test():
    # random.seed(100)
    random.seed(int(time.time()))
    a, b, p = get_random_test(1000, 1000, 100000000)
    k_float = p / 100 * (len(a) + len(b))  # ordinal rank
    if k_float.is_integer():
        k = int(k_float)
    else:
        k = math.floor(k_float) + 1
    test_percentile(a, b, p, kthSmallest(a + b, 0, len(a + b) - 1, k))
    print('Max test passed!')

    # measure time
    a, b, p = get_random_test(1000000, 1000000, 100000000)
    print('Array a len:', len(a), 'Array b len:', len(b), 'Max int in both arrays:', p)
    start = time.time()
    answer = find_percentile(a, b, p)
    end = time.time()
    difference = end - start
    print("find_percentile runs % f seconds" % difference)



def main():
    run_unit_test()
    run_stress_test()
    run_max_test()


# some test code
if __name__ == "__main__":
    main()
