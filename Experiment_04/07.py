try:
    num = int(input("Enter an integer --> "))
    print("Entered integer:", num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
