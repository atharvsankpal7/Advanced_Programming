my_dict = {"key1": "value1", "key2": "value2"}

try:
    key = input("Enter a key: ")
    value = my_dict[key]
    print("Value for key", key, "is", value)
except KeyError:
    print("Key does not exist in the dictionary.")
# just use get method