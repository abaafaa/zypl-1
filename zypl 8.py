import math as m
'''
print(abs(-2))
print(m.fabs(-2))
print(m.sqrt(9))
print(m.exp(1))
print(m.pi)
print(m.sin(m.pi / 2))
print(m.cos(m.pi / 3))

def my_func(a):
    x = m.fabs(a)
    y = m.sqrt(x)
    y = m.exp(m.sin(y) + 1)
    return y

print()
print(my_func(2))'''

def f(a, b, c):
    p = (a + b + c) / 2
    s = m.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
a = int(input())
b = int(input())
c = int(input())
print(f(a, b, c))
