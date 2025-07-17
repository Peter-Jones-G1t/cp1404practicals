"""
Class file for Project Management Program
"""


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_complete(self):
        return self.completion_percentage == 100

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f},"
                f" completion: {self.completion_percentage}%")


