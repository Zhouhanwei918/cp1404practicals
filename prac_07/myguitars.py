from guitar import Guitar


def main():
    """Main function to load, display, and sort guitars."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("Original list of guitars:")
    display_guitars(guitars)

    guitars.sort()

    print("\nSorted list of guitars (oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display guitars in the list."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
