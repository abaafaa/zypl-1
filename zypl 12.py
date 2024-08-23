nums = list(range(1, 21))
print("Original list of integers:")
print(nums)

print("\nOdd numbers from the list:")
y = filter(lambda a : a % 2 == 1, nums)
y = list(y)
print(y)

print("\nEven numbers from the list:")
y = filter(lambda a : a % 2 == 0, nums)
y = list(y)
print(y)
