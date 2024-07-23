a = [1, 1]
n = int(input())
for i in range(2, n):
    a.append(a[i - 1] + a[i - 2])
print(a)



n = int(input())
a = [0 for i in range(n)]
a[0] = a[1] = 1
for i in range(2, n):
    a[i] = a[i - 1] + a[i - 2]
print(a)


a = [1, 1]
n = int(input())
for i in range(2, n):
    i = a[-1] + a[-2]
    a.append(i)
print(a)

