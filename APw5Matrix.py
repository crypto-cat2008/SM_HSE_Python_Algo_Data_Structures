import copy


class MatrixSizeError(Exception):
    pass


class Matrix:
    # Part 1
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    # Part 2
    def __eq__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix) != len(other.matrix):
                return False
            elif len(self.matrix) == 0:
                return True
            elif len(self.matrix[0]) != len(other.matrix[0]):
                return False
            else:
                if len(self.matrix) == \
                 sum([1 for i, j in zip(self.matrix, other.matrix) if i == j]):
                    return True
                else:
                    return False
        else:
            raise TypeError

    def size(self):
        if len(self.matrix) == 0:
            return 0, 0
        else:
            return len(self.matrix), len(self.matrix[0])

    # Part 3
    def __add__(self, other):
        # return self + other
        if isinstance(other, Matrix):
            if self.size() != other.size():
                raise MatrixSizeError
            else:
                return Matrix([[self.matrix[i][j] + other.matrix[i][j]
                              for j in range(len(self.matrix[0]))]
                              for i in range(len(self.matrix))])
        else:
            raise TypeError

    def __sub__(self, other):
        # return self - other
        if isinstance(other, Matrix):
            if self.size() != other.size():
                raise MatrixSizeError
            else:
                return Matrix([[self.matrix[i][j] - other.matrix[i][j]
                              for j in range(len(self.matrix[0]))]
                              for i in range(len(self.matrix))])
        else:
            raise TypeError

    # Part 4
    def __mul__(self, other):
        # return self * other
        if isinstance(other, Matrix):
            a_size = self.size()
            b_size = other.size()
            if a_size[1] != b_size[0]:
                raise MatrixSizeError
            elif a_size == (0, 0):
                return Matrix(other.matrix)
            elif b_size == (0, 0):
                return Matrix(self.matrix)
            else:
                return Matrix([[sum(a*b for a, b in zip(X_row, Y_col))
                              for Y_col in zip(*other.matrix)]
                              for X_row in self.matrix])
        else:
            raise TypeError

    # Part 5
    def transpose(self):
        if self.size == (0, 0):
            return Matrix([])
        else:
            return Matrix([[self.matrix[j][i] for j in range(len(self.matrix))]
                           for i in range(len(self.matrix[0]))])

    # Part 6
    def tr(self):
        pass

    def det(self):
        pass
