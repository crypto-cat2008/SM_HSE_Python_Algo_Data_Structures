def partition(array, pivot_index):
    l = 0
    r = len(array) - 1
    array[r], array[pivot_index] = array[pivot_index], array[r]
    i, pivot = l - 1, array[r]

    for j in range(l, r):
        if array[j] <= pivot:  # increasing order
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i + 1]

    # print(array)

    return array


arr = [3, 2, 1, 4]
pivot_index = 0
# check that your code works correctly on provided example
assert partition(arr, pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'

arr = [2, 1, 6, 4, 7, 3, 5, 8, 10, 9]
pivot_index = 2
assert partition(arr, pivot_index) == [2, 1, 4, 3, 5, 6, 7, 8, 10, 9], 'Wrong answer'

'''
--------------------------------------------------
'''


def partition_ext(arr, l, r):
    i, pivot = l - 1, arr[r]

    for j in range(l, r):
        if arr[j] <= pivot:  # increasing order
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1


def quicksort_ext(arr, l, r):
    if l >= r:
        return

    p = partition_ext(arr, l, r)
    quicksort_ext(arr, l, p - 1)
    quicksort_ext(arr, p + 1, r)


def quicksort(array):
    n = len(array)

    quicksort_ext(array, 0, n-1)
    # print(array)

    return array


arr = [3, 2, 1, 4]
# check that your code works correctly on provided example
assert quicksort(arr) == [1, 2, 3, 4], 'Wrong answer'
