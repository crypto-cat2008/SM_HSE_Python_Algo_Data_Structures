class NonPositiveError (Exception):
    pass


class PositiveList (list):
    def append(self, item):
        if item <= 0:
            raise NonPositiveError
        else:
            super().append(item)

