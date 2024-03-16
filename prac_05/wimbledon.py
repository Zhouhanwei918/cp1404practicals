FILENAME = "wimbledon.csv"



def main():
    """Read file wimbledon.csv and print the champions number with their country"""
    records = get_records(FILENAME)
    champions_to_count, countries = withdraw_records(records)
    display_results(champions_to_count, countries)


def withdraw_records(records):
    """Create dictionary"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def get_records(filename):
    """Get records from file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
