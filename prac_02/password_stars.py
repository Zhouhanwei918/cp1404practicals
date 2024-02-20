MINIMUM_LENTH = 6

while True:
    password = input("Enter password: ")
    if len(password) < MINIMUM_LENTH:
        print(f"fPassword must be at least {MINIMUM_LENTH} characters long. Try again.")
    else:
        print("*" * len(password))
        break
