a = [list(map(int, input().split())) for i in range(int(input()))]
k = int(input())
print(*a[k - 1])
