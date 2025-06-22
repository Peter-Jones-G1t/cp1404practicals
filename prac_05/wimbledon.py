"""
Wimbledon
Estimate: 50 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    """Print champions with win count and countries that have won Wimbledon"""
    data = read_wimbledon_data(FILENAME)
    champions_to_wins = count_champions(data)
    countries = extract_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(f"{champion} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_wimbledon_data(filename):
    """Read csv file and return a list of rows."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        data = [line.strip().split(',') for line in in_file]
    return data


def count_champions(data):
    """Return a dictionary of champions and their win count."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        try:
            champion_to_wins[champion] += 1
        except KeyError:
            champion_to_wins[champion] = 1
    return champion_to_wins


def extract_countries(data):
    """Return a set of unique countries from the data."""
    countries = {row[1] for row in data}
    return countries


main()
