starts_with = lambda x: True if x.startswith('P') else False
ends_with = lambda x: True if x.endswith('n') else False
contains = lambda x: True if 't' in x else False

print(starts_with('Python'))
print(ends_with('Python'))
print(contains('Python'))

print(starts_with('Java'))
