"""
Do-from-scratch exercise - guitar
Estimate: 50 mins
Actual: 30 mins
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
