def reverse_list(items):
    numbers = []

    for index in range(len(items) - 1, -1, -1):
        numbers.append(items[index])

    return numbers
print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))