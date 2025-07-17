"""
Intermediate exercise - guitar
Estimate: 50 mins
Actual: 70 mins
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        vintage_string = " (vintage)" if self.is_vintage() else ""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}{vintage_string}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
