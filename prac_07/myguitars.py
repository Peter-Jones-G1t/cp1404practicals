"""
Program to read your guitars from a csv file and display them!
"""

from prac_07.guitar import Guitar


def main():
    """Display list of your guitars sorted from oldest to newest"""
    guitars = load_guitars()
    get_guitar(guitars)
    save_guitars(guitars)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars():
    """Load guitars from csv into a list of objects"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


def get_guitar(guitars):
    """Get a guitar from user and add to list"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def save_guitars(guitars):
    """Save added guitars to csv file"""
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
