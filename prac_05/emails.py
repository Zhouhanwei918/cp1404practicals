"""
Word Occurrences
Estimate: 15 minutes
Actual:    23minutes
"""
# email_to_name = {}
#
#
# email = input("Email: ")
# emails = email.split(".")
# print(f"Is your name {emails[0]}? (Y/n)")


email_to_name = {}

email = input("Email: ")
while email != "":
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()

    confirmation = input(f"Is your name {name}? (Y/n) ")
    if confirmation.upper() != "Y" and confirmation != "":
        name = input("Name: ")

    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
