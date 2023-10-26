try:
    num1 = float(input("Enter the first number --> "))
    num2 = float(input("Enter the second number --> "))
    op = input("Enter the operation (+, -, *, /) --> ")
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print("Invalid INput.")
        result = None
    
    if result is not None:
        print("Result:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
