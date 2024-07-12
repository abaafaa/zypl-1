'''
import random as r

a = r.randrange(1, 100)
print("Компютер ададеро байни 1 ва 100 'фикр' кард.")
print("Онро ёбед")
n = int(input("Ададро дохил кунед: "))
while n != a:
    if n > a:
        print("Адади калонтарро дохил намудед.")
    else :
        print("Адади хурдтарро дохил намудед.")
    n = int(input("Ададро дохил кунед: "))
print("Шумо Ададро ёфтед!")
print("a =", a)
'''

for i in [1, 2, 3, 4]:
    print(i)
else :
    print("Сикл ба охир расид")

print()

for i in range(1, 501):
    print(i)
else :
    print("Сикл ба охир расид")
