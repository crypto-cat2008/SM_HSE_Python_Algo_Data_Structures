class Queue:
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x):
        while len(self.popStack) > 0:
            self.pushStack.append(self.popStack.pop())
        self.pushStack.append(x)

    def pop(self):
        while len(self.pushStack) > 0:
            self.popStack.append(self.pushStack.pop())
        if len(self.popStack) == 0:
            raise IndexError('pop from an empty queue')
        else:
            return self.popStack.pop()
