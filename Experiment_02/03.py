def square_of_numbers():
    list1 = []
    for i in range(31):
        list1.append(i**2)
    print(list1)

def square_of_numbers2():
    print([(i**2) for i in range(31)])

square_of_numbers()