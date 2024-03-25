"""
project.txt.py
Estimate: 18 minutes
Actual:   17 minutes
"""

import datetime


class Project:
    def __init__(self, name="", start_date="", priority=int, cost=float, completion=int):
        self.name = name
        self.star_date = datetime.datetime.strptime(start_date, "%d/%m/%y").date()
        self.cost = cost
        self.complement = completion

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.star_date}, {self.priority}, {self.cost:,.2f},{self.completion}"

    def __repr__(self):
        """Return sting reoresentation of a ProgrammingLanguage."""
        return f"{self.name}, {self.star_date}, {self.cost:,.2f}, {self.complement}"

    def is_complete(self):
        """Verify if the peoject is completed."""
        return int(self.complement) == 100

    def __it__(self, other):
        """Less than, used for sorting project - by priority."""
        return self.priority <= other.priority

    def compare_date(self, input_date):
        """Compare the user_input date with project start date."""
        input_date = datetime.datetime.strptime(input_date, "%d/%m/%y").date()
        return self.start_date >= input_date

    def update_percentage(self, value):
        """Update the project completion percentage."""
        self.completion = value

    def update_priority(self, value):
        """Update the project priority."""
        self.priority = value
