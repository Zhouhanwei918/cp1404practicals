FILENAME = "secret.txt"


def main():
    number = load_number(FILENAME)
    guess = get_valid_integer()
    while guess != number:
        print("Guess again!")
        guess = get_valid_integer()
    print("Good job!")


def get_valid_integer():
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess  #


def load_number(filename):
    try:
        infile = open(filename, "r")
        number = int(infile.read())
    except ValueError:
        print(f"Invalid content in {filename}")
        number = 6
    except FileNotFoundError:
        print(f"{filename} not found")
        number = 4
    else:
        infile.close()
    return number


main()
