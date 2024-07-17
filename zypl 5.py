'''
myList = ['1', '11', 1, 'c', 'x', 2]
print(myList.index(1))
print(myList.index('x'))
# print(myList.index(4))
print(len(myList))

a = "python"
print(a[1:len(a):2])
print(a[:-2])
print(a[::2])
print(a[::-1])
print(a[2:5:-1])

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b[1:len(b):3])
print(b[:4])
print(b[::3])
print(b[::-1])
'''


l1 = [1, 2, 3, 4]
t1 = (1, 2, 3, 4)
print(l1)
print(t1)
print(l1[0])
print(t1[0])
l1[0] = 5
print(l1)

# t1[0] = 5

l1.append(-6)
print(l1)
l1.pop()
print(l1)
l1.pop(0)
print(l1)
t1.pop()














