CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name=" ", year=0, cost=0):
        """creat guitar class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return string format"""
        return f"{self.name}, ({self.year}) : {self.cost}"

    def get_age(self):
        """returns how old the guitar is in years """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """returns  if the guitar is 50 or more years old"""
        return self.get_age() >= VINTAGE_AGE

    def __it__(self, other):
        """Less than , used for sorting Guitars - by year released."""
        return self.year < other.year