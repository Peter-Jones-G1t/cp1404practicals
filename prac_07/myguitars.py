"""
Program to read your guitars from a csv file and display them!
"""

from prac_07.guitar import Guitar


def main():
    guitars = []

    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

    in_file.close()

    guitars.sort()

    for guitar in guitars:
        print(guitar)


main()
