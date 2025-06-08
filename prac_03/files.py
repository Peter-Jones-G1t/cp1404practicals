"""
Program to practice reading and writing to files
"""

FILENAME = "name.txt"

user_name = input("Enter you name: ")
name_file = open(FILENAME, 'w')
print(user_name, file=name_file)
name_file.close()