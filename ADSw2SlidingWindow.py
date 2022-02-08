import collections


def sliding_window_min(a, k):
    result = []
    que = collections.deque()

    for (i, val) in enumerate(a):

        while len(que) > 0 and val < que[-1]:
            que.pop()
        que.append(val)
        print('q1', que)

        j = i + 1 - k
        if j >= 0:
            result.append(que[0])
            if a[j] == que[0]:
                que.popleft()
        print('q2', que)

    return result

# some test code
if __name__ == "__main__":
    test_a, test_k = [1, 3, 4, 5, 2, 7], 3
    # should print [1, 3, 2, 2]
    # print(sliding_window_min(test_a, test_k))

    test_a, test_k = [5, 4, 10, 1], 2
    # should print [4, 4, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [10, 20, 6, 10, 8], 5
    # should print [6]
    print(sliding_window_min(test_a, test_k))
