def case_counter(input_string):
    input_string = str(input_string)
    lowercase_count = 0
    uppercase_count = 0

    for item in input_string:
        if item.islower():
            uppercase_count += 1
        elif item.isupper():
            lowercase_count += 1

    print('lowercase count :' + str(lowercase_count))
    print('uppercase count :' + str(uppercase_count))


case_counter('The quick Brown Fox')
