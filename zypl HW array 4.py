n = int(input())
a = int(input())
d = int(input())
l = [a * d**i for i in range(n + 1)]
print(l)
