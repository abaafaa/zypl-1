nums = list(range(1, 11))
print("Original list of integers:")
print(nums)

print("\nSquare numbers of the list:")
y = map(lambda a : a ** 2, nums)
y = list(y)
print(y)

print("\nCube numbers of the list:")
y = map(lambda a : a ** 3, nums)
y = list(y)
print(y)
