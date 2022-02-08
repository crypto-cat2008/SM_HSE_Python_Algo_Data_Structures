class Deque:

    def __init__(self):
        self.max_len = 60000 + 1  # change size to 60,000
        self.queue = [0] * self.max_len
        self.tmp_queue = []
        self.head = 0
        self.tail = 0

    def push_front(self, key):

        size = self.size()

        if self.empty():
            self.queue[self.tail] = key
            self.tail = (self.tail + 1) % self.max_len
        else:
            for i in range(size):
                self.tmp_queue.append(self.queue[i])
                self.tail = (self.tail - 1) % self.max_len

            self.queue[self.tail] = key
            self.tail = (self.tail + 1) % self.max_len

            for i in range(size):
                self.queue[self.tail] = self.tmp_queue[i]
                self.tail = (self.tail + 1) % self.max_len

        self.tmp_queue = []
        # print('push_front', key, self.queue)
        return "ok"

    def push_back(self, key):
        self.queue[self.tail] = key
        self.tail = (self.tail + 1) % self.max_len
        # print('push_back', key, self.queue)
        return "ok"

    def pop_front(self):
        size = self.size()

        if self.empty():
            return 'error'
        else:
            res = self.queue[self.head]
            for i in range(1, size):
                self.queue[i-1] = self.queue[i]
            self.tail = self.tail - 1

        # print('pop_front', res, self.queue)
        return res

    def pop_back(self):
        if self.empty():
            return 'error'
        else:
            res = self.queue[self.tail - 1]
            self.tail = (self.tail - 1) % self.max_len
            return res

    def front(self):
        if self.empty():
            return 'error'
        else:
            return self.queue[self.head]

    def back(self):
        if self.empty():
            return 'error'
        else:
            return self.queue[self.tail - 1]

    def clear(self):
        self.head = 0
        self.tail = 0
        return "ok"

    def size(self):
        return self.tail - self.head

    def empty(self):
        return self.head == self.tail


def process_deque(commands):
    q = Deque()
    results = []
    param = 0
    result = None

    for i in commands:
        if ' ' in i:
            cmd, param = i.split()
        else:
            cmd = i
        if cmd == "push_front":
            result = q.push_front(int(param))
        elif cmd == "push_back":
            result = q.push_back(int(param))
        elif cmd == "front":
            result = q.front()
        elif cmd == "back":
            result = q.back()
        elif cmd == "clear":
            result = q.clear()
        elif cmd == "pop_front":
            result = q.pop_front()
        elif cmd == "pop_back":
            result = q.pop_back()
        elif cmd == "size":
            result = q.size()
        else:
            print("invalid command", cmd)
        # print('cmd', cmd, 'result', result)
        results.append(result)
    return results
