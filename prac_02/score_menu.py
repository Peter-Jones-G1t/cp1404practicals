"""Score menu"""


def main():
    """Determine what function to call based on user choice """
    score = None
    choice = input(menu() + "\n>>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option.")
        choice = input(menu() + "\n>>>").upper()

    print("Farewell!")


def menu():
    """Display the menu"""
    return """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def get_valid_score():
    """Get a valid score from user"""
    score = float(input("Enter a valid score (0 - 100):"))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = float(input("Enter a valid score (0 - 100):"))
    return score


def print_result(score):
    """Display the score grade"""
    if score is not None:
        print(f"Your result is: {determine_result(score)}")
    else:
        print("Please enter a valid score first (G).")


def print_stars(score):
    """Print number of stars based on user score"""
    if score is not None:
        print('*' * int(score))
    else:
        print("Please enter a valid score first (G).")


def determine_result(score):
    """Determine the user result"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
