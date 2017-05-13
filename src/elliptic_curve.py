from gmpy2 import f_mod


class EllipticCurve(object):
    def check_point(self, X, Y):
        """"Check if point belong to this curve """
        return f_mod((Y * Y), self.P) == f_mod((X * X * X + self.A * X + self.B), self.P)

    def check_delta(self):
        """"Check delta condidtion properly with definition"""
        return f_mod((4 * (self.A * self.A * self.A) + 27 * (self.B * self.B)), self.P) != 0

    def __init__(self, P, A, B):
        self.P = P
        self.A = A
        self.B = B
        if not self.check_delta():
            raise BaseException("delta is zero")
