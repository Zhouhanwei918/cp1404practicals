total = 0
number_of_items = int(input("Number of items:"))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items:"))
for i in range(number_of_items):
    price = float(input("Price of item:"))
    total += price
print(f"Total price for 3 items is:${total:.2f}")