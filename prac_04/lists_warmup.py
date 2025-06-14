"""
CP1404 list warmup activity
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = [3]
# numbers[-1] = [2]
# numbers[3] = [1]
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1. changes first element in list to "ten"
numbers[0] = "ten"

# 2. changes last element in list to 1
numbers[-1] = 1

# 3. prints all elements in the list except the first two
print(numbers[2:])

# 4. checks and prints if 9 is an element of the list
if 9 in numbers:
    print("9 is in the list")
else:
    print("9 is not in the list")
