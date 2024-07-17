'''
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

p = 1, r = 0
for i in range(int(input()) + 1):
    p *= i
    r += p
print(p)
'''

'''
n = int(input())
i = 1
while i * i * i < n:
    i += 1
if i * i * i == n:
    print(True)
else :
    print(False)
'''

n = int(input())
f = False
while n > 0:
    if n % 10 == 2:
        f = True
    n //= 10
print(f)
