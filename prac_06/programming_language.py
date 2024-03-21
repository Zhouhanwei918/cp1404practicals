"""
programming_language
Estimate: 12 minutes
Actual:   19 minutes
"""


class ProgrammingLanguage:
    """decide programming language"""

    def __init__(self, name, type, reflection, year):
        """"""
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """return string to print program language"""
        return f"{self.name}, {self.type} Typing, Reflection ={self.reflection}, Frist appeared in{self.year}"

    def is_dynamic(self):
        return self.type == "Dynamic"


def run_test():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == '__main__':
    run_test()