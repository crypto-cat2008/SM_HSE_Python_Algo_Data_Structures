class FlashError (Exception):
    pass


class FlashMaxFileSizeError (FlashError):
    pass


class FlashMemoryLimitError (FlashError):
    pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.max_file_size = max_file_size
        self.size_written = 0

    def write(self, v):
        if not (self.max_file_size is None) and v > self.max_file_size:
            raise FlashMaxFileSizeError
        elif v > (self.capacity - self.size_written):
            raise FlashMemoryLimitError
        else:
            self.size_written += v
