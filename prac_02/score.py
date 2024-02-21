def main():
    score = float(input("Enter score: "))
    result = convert_score_to_result(score)
    print(f"Your result is {result}")


def convert_score_to_result(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()