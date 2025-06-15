"""
CP1404 Program to display information from a list of numbers
"""


def main():
    numbers = []

    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    print(numbers)


main()
