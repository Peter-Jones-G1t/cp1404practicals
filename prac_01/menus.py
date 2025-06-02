#Menu

name = input("Enter name: ")

print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello, {name}")
    elif choice == "G":
        print(f"Goodbye, {name}")
    else:
        print("Invalid option")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input(">>> ").upper()

print("Finished.")
