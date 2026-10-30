def reverse_list(items):
    numbers = []

    for index in range(len(items) - 1, -1, -1):
        numbers.append(items[index])

    return numbers
print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))

# chatgbt engineering drill exercise 
def reverse_names(names):
    reversed_list = []
    for number in range(len(names) -1, -1, -1):
        reversed_list.append(names[number])
    return reverse_list
print(reverse_names(["Temple", "David", "John", "Peter"]))
print(reverse_list(["Ada", "Grace", "Linus"]))    
