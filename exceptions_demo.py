# Two independent tasks with separate handlers.
# Step 1: Try to open the file.
try:
    file = open("names.txt", "r")
except FileNotFoundError:
    print("The names file was not found.")
else:
    # Runs only if opening the file succeeded.
    with file:
        for line in file:
            print(line.strip())

# Step 2: This task does not depend on the file.
try:
    number = int(input("Enter a whole number: "))
except ValueError:
    print("That was not a valid whole number.")
else:
    print("Twice your number is", number * 2)
