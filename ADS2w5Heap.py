class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, elem):
        self._heap.append(elem)
        self._sift_up(len(self._heap) - 1)

    def _sift_up(self, index):
        parent = (index - 1) // 2

        if index > 0 and self._heap[index] > self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]  # swap
            self._sift_up(parent)


heap = MaxHeap()
heap.push(1)
heap.push(2)
heap.push(3)

# check that your code works correctly on provided example
assert heap._heap in [[3, 2, 1], [3, 1, 2]], 'Wrong answer'

'''
========================================================
'''


class MinHeap:
    def __init__(self):
        self._heap = []

    def pop(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        elem = self._heap.pop()
        self._sift_down(0)

    def _sift_down(self, index):

        l_child = index * 2 + 1
        r_child = index * 2 + 2

        if l_child < len(self._heap) and self._heap[l_child] < self._heap[index]:
            self._heap[index], self._heap[l_child] = self._heap[l_child], self._heap[index]  # swap
            self._sift_down(l_child)

        if r_child < len(self._heap) and self._heap[r_child] < self._heap[index]:
            self._heap[index], self._heap[r_child] = self._heap[r_child], self._heap[index]  # swap
            self._sift_down(r_child)

heap = MinHeap()
heap._heap = [1, 2, 3]
heap.pop()

# check that your code works correctly on provided example
assert heap._heap == [2, 3], 'Wrong answer'

'''
========================================================
'''

def swap_elem(arr, i, n):
    smallest = i
    l, r = i * 2 + 1, i * 2 + 2
    for child in (l, r):
        if child < n and arr[smallest] > arr[child]:
            smallest = child
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swap_elem(arr, smallest, n)

def heapify(array):
    n = len(array)

    start = n // 2 - 1
    for i in range(start, -1, -1):
        swap_elem(array, i, n)
    return

arr = [3, 2, 1]
heapify(arr)
# check that your code works correctly on provided example
assert arr in  [[1, 2, 3], [1, 3, 2]], 'Wrong answer'

'''
========================================================
'''

def swap_elem_max(arr, i, n):
    largest = i
    l, r = i * 2 + 1, i * 2 + 2
    for child in (l, r):
        if child < n and arr[largest] < arr[child]:
            largest = child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swap_elem_max(arr, largest, n)

def heapify_max(array):
    n = len(array)

    start = n // 2 - 1
    for i in range(start, -1, -1):
        swap_elem_max(array, i, n)
    return


def heapsort(array):
    n = len(array)

    heapify_max(array)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        swap_elem_max(array, 0, i)

    return array

arr = [3, 2, 1, 4]
# check that your code works correctly on provided example
assert heapsort(arr) ==  [1, 2, 3, 4], 'Wrong answer'