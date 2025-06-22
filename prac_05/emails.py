"""
Emails
Estimate: 50 minutes
Actual: 41 minutes
"""


def main():
    email_to_name = {}

    email = input("Enter an email: ")
    while email != "":
        username = email.split('@')[0]
        parts = username.replace('.', ' ').split()
        name = ' '.join(part.title() for part in parts)

        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != '' and confirmation != 'y':
            name = input("Name: ")
        email_to_name[email] = name

        email = input("Enter an email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
