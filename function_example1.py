def y(t, v0):
    g = 9.8
    return v0*t - 0.5*g*t**2

def diff(f, x, h=1E-6):
    return (f(x+h) - f(x))/h

def h(t):
    return t**4 + 4*t

from math import sin, pi
x = 2*pi
dsin = diff(sin,x,h=1E-6)

dh = diff(h,0.1)
print(dh)

print(dsin)




