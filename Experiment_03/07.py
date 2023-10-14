def vowels_and_consonant_count(input_string):
    input_string = str(input_string)
    vowel_count = 0 
    consonant_count = 0 
    for item in input_string:
        if item in ['a','e','i','o','u']:
            vowel_count+=1
        elif 65 <= ord(item) <= 90 or 97 <= ord(item) <= 122:
            consonant_count+=1
    print(f"vowels {vowel_count}")
    print(f"consonant {consonant_count}")


vowels_and_consonant_count('thia aw34u5 adfjhaf ')