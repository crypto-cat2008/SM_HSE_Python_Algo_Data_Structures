class Flash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.totalSizeWritten = 0

    def write(self, filesize):
        if filesize > self.capacity:
            raise ValueError
        elif self.totalSizeWritten + filesize > self.capacity:
            raise ValueError
        else:
            self.totalSizeWritten += filesize
