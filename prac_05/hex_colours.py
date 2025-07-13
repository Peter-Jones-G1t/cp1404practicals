"""
Program to print hex code of chosen colour
"""

COLOUR_TO_HEX = {"Rifle Green": "#444c38", "Inchworm": "#b2ec5d", "Copper": "#b87333", "Kelly Green": "#4cbb17",
                  "Rose": "#ff007f", "Old Gold": "#cfb53b", "Lilac": "#c8a2c8", "Linen": "#faf0e6",
                  "Eggplant": "#614051", "Denim": "#1560bd"}

colour_name = input("Enter a colour: ").title()
while colour_name != "":
    try:
        print(f"{colour_name}'s hex code is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter a colour: ").title()
