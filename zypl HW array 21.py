n = int(input())
k = int(input())
l = int(input())
a = list(map(int, input().split()))
r = 0
s = 0
for i in range(k - 1, l):
    r += 1
    s += a[i]
print(s / r)

