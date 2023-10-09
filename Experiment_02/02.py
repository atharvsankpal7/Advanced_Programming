def print_even_numbers(input_list):
    for i in input_list:
        if i % 2 == 1:
            input_list.remove(i)
    print(input_list)

def print_even_numbers2(input_list):
    even_number_list = [i for i in input_list if x % 2 == 0]
    print(even_number_list)

print_even_numbers([1,
2, 3, 4, 5, 6, 7, 8, 9])