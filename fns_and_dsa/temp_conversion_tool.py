# File: explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date_time = datetime.now()

    # Format the current date and time
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date_time}")

def calculate_future_date():
    # Prompt the user for the number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # Get the current date
    current_date = datetime.now().date()

    # Calculate the future date
    future_date = current_date + timedelta(days=number_of_days)

    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

