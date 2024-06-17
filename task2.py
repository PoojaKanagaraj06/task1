# Function to generate a number pyramid pattern
def generate_number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end=" ")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end=" ")
        # Print reverse numbers
        for l in range(i - 1, 0, -1):
            print(l, end=" ")
        # Move to the next line
        print()

# Number of rows for the pyramid
rows = int(input("Enter The Number of Rows"))
generate_number_pyramid(rows)
