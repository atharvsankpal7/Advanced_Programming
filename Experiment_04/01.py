try:
    num1 = float(input("Enter the first number --> "))
    num2 = float(input("Enter the second number --> "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
