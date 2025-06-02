"""Password checker"""

MIN_LENGTH = 8
def main():
    """Calls other program functions"""
    password = get_password()
    print_stars(password)


def print_stars(password):
    """Prints number of stars based on password length"""
    print('*' * len(password))


def get_password():
    """Gets password and checks it meets length requirements"""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter password: ")
    return password

main()