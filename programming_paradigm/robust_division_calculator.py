def safe_divide(numerator, denominator):
  """
  Performs division with robust error handling.

  Args:
      numerator: The numerator (number to be divided).
      denominator: The denominator (number dividing).

  Returns:
      The result of the division (float) or an error message (str).
  """
  try:
    # Attempt conversion to float for non-numeric input
    numerator = float(numerator)
    denominator = float(denominator)
  except ValueError:
    return "Error: Please enter numeric values only."

  try:
    # Perform division and handle ZeroDivisionError
    result = numerator / denominator
    return result
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."

