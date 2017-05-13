from elliptic_curve import EllipticCurve
from point import Point
from ideal import Ideal
from gmpy2 import invert
from gmpy2 import f_mod
from gmpy2 import mpz_random
from random import randint
from gmpy2 import random_state
from gmpy2 import gcd
from gmpy2 import fac


class Lenstra(object):
    def create_curve(self):
        """
        :return: random Elliptic curve  and init Point
        """
        for i in range(10):
            try:
                self.X = self._generate_random_number()
                self.Y = self._generate_random_number()
                self.A = self._generate_random_number()
                self.B = f_mod((self.Y * self.Y - self.X * self.X * self.X - self.A * self.X), self.N)
                curve = EllipticCurve(self.N, self.A, self.B)
                return curve
            except Exception as e:
                print("Error when curve is generated %s" % str(e))
                raise Exception

    def __init__(self, N, t=0):
        self.N = N
        self.t = t if t != 0 else None
        self.curve = self.create_curve()
        self.point = Point(self.curve, self.X, self.Y)

    def _generate_random_number(self):
        """
        :return: random number  
        """
        rstate = random_state()
        r = randint(40, 100)
        return f_mod(mpz_random(rstate, 2 << r).bit_set(0).bit_set(r), self.N)

    def is_not_point(self, p):
        return (isinstance(p, Ideal) == False and isinstance(p, Point) == False)

    def partial_addition(self, P, Q):
        """
        :param P: One point on EC 
        :param Q: Second Point on EC
        :return: Partial addition point P + Q according to Lenstra publication
        """
        if P.ideal() and not Q.ideal():
            return Q
        elif not P.ideal() and Q.ideal():
            return P
        elif not P.ideal() and not Q.ideal():
            N = P.curve.P
            d = gcd(P.X - Q.X, N)
            if 1 < d < N:
                return d
            if d == 1:
                iv = invert(f_mod(P.X - Q.X, N), N)
                delta = f_mod((P.Y - Q.Y) * iv, N)
                x_3 = f_mod(delta * delta - P.X - Q.X, N)
                y_3 = f_mod(delta * (P.X - x_3) - P.Y, N)
                return Point(P.curve, x_3, y_3)
            else:
                d = gcd(P.Y + Q.Y, N)
                if 1 < d < N:
                    return d
                if d == N:
                    return Ideal()
                if d == 1:
                    iv = invert(f_mod(P.Y + Q.Y, N), N)
                    delta = f_mod((3 * P.X * P.X + P.curve.A) * iv, N)
                    x_3 = f_mod(delta * delta - P.X - Q.X, N)
                    y_3 = f_mod(delta * (P.X - x_3) - P.Y, N)
                    return Point(P.curve, x_3, y_3)

    def mul(self, k, p):
        """
        :param k: how many times 
        :param p: Point
        :return: k*P
        """
        e = bin(k)[2:]  # transform to binary
        e = e[::-1]  # reverse it
        Q = p
        R = Ideal() if e[0] == '0' else p
        for i in e:
            Q = self.partial_addition(Q, Q)
            if self.is_not_point(Q):
                return Q
            if i == '1':
                R = self.partial_addition(R, Q)
                if self.is_not_point(R):
                    return R
        return R

    def factor(self):
        """
        factor a number, just do it! 
        """
        k = randint(1000000, 100000000)
        Q = self.point
        x = 2
        while x < k:
            x += 1
            Q = self.mul(x, Q)
            if self.is_not_point(Q):
                return Q
        return None
