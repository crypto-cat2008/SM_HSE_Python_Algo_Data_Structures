import math


class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        if isinstance(re, int) or isinstance(re, float):
            self.re = re
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        if self.im >= 0.0:
            return f'{self.re}+{self.im}i'
        else:
            return f'{self.re}{self.im}i'

    # Part 2
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)
        elif isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re - other, self.im)
        elif isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        else:
            raise TypeError

    # Part 3
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re*other, self.im*other)
        elif isinstance(other, Complex):
            return Complex(self.re*other.re - self.im*other.im,
                           self.re*other.im + self.im*other.re)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re/other, self.im/other)
        elif isinstance(other, Complex):
            c = Complex(other.re, (-1)*other.im)
            n = self.__mul__(c)
            d = (other.re)**2 + (other.im)**2
            return Complex(n.re/d, n.im/d)
        else:
            raise TypeError

    # Part 4
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            n = Complex(other, 0)
            if self.re == n.re and self.im == n.im:
                return True
            else:
                return False
        elif isinstance(other, Complex):
            if self.re == other.re and self.im == other.im:
                return True
            else:
                return False
        else:
            raise TypeError

    def __abs__(self):
        return math.sqrt((self.re)**2 + (self.im)**2)
