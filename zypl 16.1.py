a = [1, 2, 3]
b = a
print('a =', a)
print('b =', b)
print('id of a =', id(a))
print('id of b =', id(b))

a[0] = 99
print('a =', a)
print('b =', b)

a = [11, 12, 13]
print('a =', a)
print('b =', b)
print('id of a =', id(a))
print('id of b =', id(b))


a = [1, 2, 3]
c = a
print('a =', a)
print('c =', c)
print('id of a =', id(a))
print('id of c =', id(c))



c = a.copy()
print(c)
print('id of a =', id(a))
print('id of c =', id(c))
