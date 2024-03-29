MINIMUM_LENGTH = 6


def main():
    while True:
        password = get_password()
        if len(password) < MINIMUM_LENGTH:
            print(f"fPassword must be at least {MINIMUM_LENGTH} characters long. Try again.")
        else:
            print_asterisks(password)
            break


def get_password():
    password = input("Enter password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
