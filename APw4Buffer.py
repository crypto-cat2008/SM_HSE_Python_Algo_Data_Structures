class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.sizeLeft = maxsize
        self.buffer = list()

    def add(self, *a):
        for i, y in enumerate(a):
            self.buffer.append(y)
            self.sizeLeft -= 1
            if self.sizeLeft == 0:
                print(sum(self.buffer))
                self.buffer = []
                self.sizeLeft = self.maxsize

    def get_current_part(self):
        return(self.buffer)
