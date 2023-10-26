my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter an index: "))
    value = my_list[index]
    print("Value at index", index, "is", value)
except IndexError:
    print("Index is out of range.")
except ValueError:
    print("Invalid input. Please enter a valid integer index.")
