"""
Program to store all your guitars!
Estimate: 30 mins
Actual: 45 mins
"""

from prac_06.guitar import Guitar


def main():
    """Stores and prints a list of your guitars"""
    print("My guitars!")

    guitars = []
    get_guitar(guitars)

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else "" # check if guitar in list is vintage
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth {guitar.cost:10,.2f}{vintage_string}")


def get_guitar(guitars):
    """Get a valid guitar"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.\n")

        name = input("Name: ")


main()
