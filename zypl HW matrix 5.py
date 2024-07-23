n = int(input())
m = int(input())
d = int(input())
a = list(map(int, input().split()))

v = [[0] * m for i in range(n)]

for i in range(n):
    v[i][0] = a[i]

for i in range(n):
    for j in range(1, m):
        v[i][j] = v[i][j - 1] + d

for i in v:
    print(*i)
