# File: multiplication_table.py

def main():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print multiplication table using a for loop
    for i in range(1, 11):  # Loop through numbers 1 to 10
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()
