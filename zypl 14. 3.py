is_num = lambda q: q.replace('.', '', 1).isdigit()

print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12345'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))

is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)

print()
print(is_num1('-16.4'))
print(is_num1('-24587.11'))
