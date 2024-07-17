d1 = dict.fromkeys(['a', 'b'])
print(d1)
d2 = dict.fromkeys(['a', 'b'], 10)
print(d2)
d3 = dict.fromkeys(range(10), None)
print(d3)


print("''''''''''''''''''")

e = {a : a**2 for a in range(11)}
print("adad **2", e)

du = {a : a * 2 for a in range(11)}
print("* 2", du)

se = {a : a * 3 for a in range(11)}
print("* 3", se)
