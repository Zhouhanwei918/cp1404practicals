# def main():
#     score = float(input("Enter score: "))
#     result = convert_score_to_result(score)
#     print(f"Your result is {result}")
#
#
#
# def convert_score_to_result(score):
#     determine the result
#     while score < 0 or score > 100:
#         print("Invalid score")
#         score = float(input("Enter score: "))
#     if score > 90:
#         result = "Excellent"
#     elif score > 50:
#         result = "Passable"
#     else:
#         result = "Bad"
#     return result
#
#
# main()


def main():
    """Get a  score and display its result."""
    score = float(input("Enter score: "))
    print("Your result is", determine_status(score))


def determine_status(score):
    """Determine the result of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

"""added radom score"""
import random


def main():
    """Get a  radom score and display its result."""
    score = random.randint(0, 100)
    print("Your result is", determine_status(score))


def determine_status(score):
    """Determine the result of a radom score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
