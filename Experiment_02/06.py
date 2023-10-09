def password_validation(input_string):
    
    if len(input_string  )> 16 or len(input_string )< 7:
        return False
    has_capital_character = False
    has_lower_character = False
    has_number_character = False
    for i in input_string:
        if i.isdigit():
            has_number_character = True
        if i.islower():
            has_lower_character = True
        if i.isupper():
            has_capital_character = True
    if(has_capital_character and has_lower_character and has_number_character):
        return True
    return False
    
string = "Password123"

print(password_validation(string))