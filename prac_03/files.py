"""
Program to practice reading and writing to files
"""

FILENAME = "name.txt"

# program 1.
user_name = input("Enter you name: ")
name_file = open(FILENAME, 'w')
print(user_name, file=name_file)
name_file.close()

# program 2.
name_file = open(FILENAME, 'r')
read_file = name_file.read().strip()
print(f"Hi {read_file}!")
name_file.close()

# program 3.
with open("numbers.txt", 'r') as numbers_file:
    total = int(numbers_file.readline()) + int(numbers_file.readline())
    print(total)

# program 4.
with open("numbers.txt", 'r') as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)
    print(total)
