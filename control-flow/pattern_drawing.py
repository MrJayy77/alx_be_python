size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for col in range(size):
        print("*", end="")  # Print without moving to next line
    print()  # Move to the next line after one row is complete
    row += 1  # Move to the next row