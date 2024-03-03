FILENAME = "name.txt"

# question 1
out_file = open(FILENAME, "w")
name = input("Enter name: ")
print(name, file= out_file)
out_file.close()

# question2
in_file = open(FILENAME, "r")
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()

# question3
in_file = open("numbers.txt", "r")
read1 = int(in_file.readline())
read2 = int(in_file.readline())
print(read1 + read2)

# question4
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

