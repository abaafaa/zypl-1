a = {"a", "b", "c", "z"}
b = {"f", "d", "a", "z"}

x = a.difference(b)
print("x =>", x)
print("a =>", a)

a.difference_update(b)
print("a =>", a)

print(a)
print(b)
a.discard("c")
b.discard("z")
print(a)
print(b)
