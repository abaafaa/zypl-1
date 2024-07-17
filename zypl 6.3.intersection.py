a = {"a", "b", "c"}
b = {"f", "d", "e"}
x = a.union(b)
print(x)
y = a | b
print(y)


a = {"a", "b", "c"}
b = {"a", "d", "e"}
x = a.intersection(b)
print(x)
y = a & b
print(y)


a = {"a", "b", "c"}
b = {"a", "d", "e"}
x = a.difference(b)
print(x)
y = a - b
print(y)


a = {"a", "b", "c"}
b = {"a", "d", "e"}
x = b.difference(a)
print(x)
y = b - a
print(y)
