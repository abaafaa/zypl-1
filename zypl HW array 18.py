a = list(map(int, input().split()))
k = 0
for i in a:
    if i < a[-1]:
        k = i
        break
print(k)
