import datetime
a = datetime.datetime.today()
b = datetime.datetime.now()
print(a)
print(b)

a = datetime.datetime.today().strftime("%Y-%n-%d")
print(a)

a = datetime.datetime.today().strftime("%m/%d/%Y")
print(a)

a = datetime.datetime.today().strftime("%d.%n.%Y")
print(a)

b = datetime.datetime.today().strftime("%H:%M:%S")
print(b)
