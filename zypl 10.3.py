def printme(s):
    my_str = str(s)
    l = list(my_str)
    print('*** ', end = '')
    print(*l, sep = '-', end = '')
    print(' ***')

printme("Hello")

test = 123
printme(test)

my_input = input("Сатр: ")
printme(my_input)
