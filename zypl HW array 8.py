n = int(input())
a = list(map(int, input().split()))
k = 0
for i in a:
    if i % 2:
        k += 1
        print(i, end = ' ')
print("m =", k)
