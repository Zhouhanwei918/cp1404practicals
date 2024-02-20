MINIMUM_LENGTH = 6


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    while True:
        password = input("Enter a password: ")
        if len(password) < MINIMUM_LENGTH:
            print(f"Password must be at least {MINIMUM_LENGTH} characters long. Try again.")
        else:
            return password


def print_asterisks(word):
    print('*' * len(word))


main()
