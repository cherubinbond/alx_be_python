# File: temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    # Prompt user for temperature and unit
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                converted_temperature = convert_to_celsius(temperature)
                print(f"{temperature:.1f}°F is {converted_temperature:.1f}°C")
                break
            elif unit == 'C':
                converted_temperature = convert_to_fahrenheit(temperature)
                print(f"{temperature:.1f}°C is {converted_temperature:.1f}°F")
                break
            else:
                print("Invalid input. Please enter 'C' or 'F'.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
