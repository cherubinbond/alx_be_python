# File: pattern_drawing.py

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))

    # Draw the pattern using nested loops
    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end="")
            col += 1
        print()  # Move to the next line after printing each row
        row += 1

if __name__ == "__main__":
    main()
