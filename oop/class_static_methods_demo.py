class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of the two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers and print the class attribute calculation_type.

        Args:
            cls: The class itself (used to access class attributes).
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
