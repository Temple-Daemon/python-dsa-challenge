def has_duplicates(numbers):
    if not numbers:
        return False
    original_list = []    
    for number in numbers:
        if number in original_list:
            return True
        else:
            original_list.append(number)
    return False 
print(has_duplicates([1, 2, 3, 2])) 
print(has_duplicates([1, 2, 3, 4])) 
print(has_duplicates([]))  