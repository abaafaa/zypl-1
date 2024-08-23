def f():
    global s
    s += ", in func"
    print(s)

s = "example"
print("first", s)
f()
print("second", s)
