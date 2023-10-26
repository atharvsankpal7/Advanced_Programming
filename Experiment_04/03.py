class ValueTooHighError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
try:
    num = int(input("Enter an integer: "))
    if num > 100:
        raise ValueTooHighError("Value is too high (> 100)")
    print("Entered value is within the acceptable range.")
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter an integer.")
