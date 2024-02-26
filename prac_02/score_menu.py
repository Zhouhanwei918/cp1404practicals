MENU = ('(G)et a valid score\n'
        '(P)rint result \n'
        '(S)how stars \n'
        '(Q)uit')


def main():
    """menu choice"""
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            print("Your result is", determine_status(score))

        elif choice == "S":
            print_asterisks(score)
        print(MENU)
        choice = input(">>>").upper()

    print("farewell")


def get_valid_score():
    """Get valid score"""
    while True:
        score = int(input("Enter a valid score (0-100):"))
        if 0 <= score <= 100:
            return score
        else:
            print(f"Invalid score. Please enter a score between 0 and 100.")


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


def print_asterisks(score):
    print("*" * score)


main()
