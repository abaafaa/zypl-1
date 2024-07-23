'''import datetime
a = datetime.date(2001, 10, 28)
print(a)

b = datetime.time(12, 18, 35, 5867)
print(b)
print(type(b))

c = datetime.datetime(2017, 7, 18, 4, 52, 33)
print(c)
print(type(c))

d = str(datetime.date()).split('-')
print(d)


'''

'''
from datetime import date
from datetime import datetime

print("===============")
print(datetime.now())
print(datetime.now().date())
x = datetime.now()
print(x)
print(type(x))
y = x.date()
print(y)
print(type(y))
print("===============")

f_date = date(2024, 6, 21)
l_date = datetime.now().date()
delta = l_date - f_date
print(delta)
print(type(delta))

_year = int(input("Year: "))
_month = int(input("Month: "))
_day = int(input("Day: "))

f_date = date(_year, _month, _day)
l_date = datetime.now().date()
delta = l_date - f_date
print(delta)

f_date = datetime(_year, _month, _day, 12, 12, 12, 12)
l_date = datetime.now()
delta = l_date - f_date
print(delta)
'''

import datetime
a = datetime.datetime(2022, 7, 13, 19, 10)
b = a + datetime.timedelta(days = 2, minutes = 10)
c = b - datetime.timedelta(days = 3, hours = 1, minutes = 20)
print(a)
print(b)
print(c)
c = datetime.datetime.now()
d = c - datetime.timedelta(hours = 12227, minutes = 43)
print(c)
print(d)




















