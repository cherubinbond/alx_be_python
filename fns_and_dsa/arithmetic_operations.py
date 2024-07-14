# File: arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"

# This script defines a function `perform_operation` that performs basic arithmetic operations
# based on the provided operation ('add', 'subtract', 'multiply', 'divide') and numerical inputs.
