from elliptic_curve import EllipticCurve
from point import Point
from ideal import Ideal
from lenstra import Lenstra

c = EllipticCurve(P=17, A=200,B=-137)

# test addition

p = Point(curve=c, X=47,Y=125)
pp = Point(curve=c, X=1, Y=9)
l = Lenstra(221)

l.curve = c
l.point = p

print(l.partial_addition(p,pp))
