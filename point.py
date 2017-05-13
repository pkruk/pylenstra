from ideal import Ideal
from gmpy2 import invert
from gmpy2 import f_mod


class Point(Ideal):
    def __init__(self, curve, X, Y):
        """
        :param curve: point belongs to curve
        :param X: coordinate X
        :param Y: coordinate Y
        """
        self.curve = curve
        self.X = X
        self.Y = Y
        if not self.curve.check_point(self.X, self.Y):
            raise BaseException("wrong point")

    def _compare_points_(self, other):
        return (self.X == other.X) and (self.Y == other.Y)

    def __double_point__(self):
        """
        :return: 2*P 
        """
        invert_y = invert(2 * self.Y, self.curve.P)
        if invert_y == 0:
            raise BaseException('infinite')
        s = f_mod((((3 * (self.X * self.X) + self.curve.A)) * (invert_y)), self.curve.P)
        x_3 = f_mod(((s * s) - self.X - self.X), self.curve.P)
        y_3 = f_mod((s * (self.X - x_3) - self.Y), self.curve.P)
        return Point(self.curve, x_3, y_3)

    def __add_other_point(self, other):
        """
        :param other: Point 
        :return: self + other according to EC rules
        """
        x = f_mod((other.X - self.X), self.curve.P)
        x = invert(x, self.curve.P)
        if x == 0:
            raise BaseException('infinite')
        s = f_mod(((other.Y - self.Y) * x), self.curve.P)
        x_3 = f_mod((s * s - self.X - other.X), self.curve.P)
        y_3 = f_mod((s * (self.X - x_3) - self.Y), self.curve.P)
        return Point(self.curve, x_3, y_3)

    def __add__(self, other):
        if self._compare_points_(other):
            return self.__double_point__()
        else:
            return self.__add_other_point(other)

    def __str__(self):
        return "(%s, %s)" % (self.X, self.Y)

    def ideal(self):
        return False
