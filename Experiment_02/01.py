def unique_elements(input_list):
    filtered_list = []
    for item in input_list:
        if(item not in filtered_list):
            filtered_list.append(item)
    return filtered_list
    
print(unique_elements([1,2,3,3,3,3,4,5]))
        