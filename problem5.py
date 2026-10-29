def count_occurrences(numbers, target):
    count_target = 0
    for number in numbers:
        if number == target:
            count_target = count_target + 1
    return count_target
print(count_occurrences([2, 5, 2, 8, 2], 2))
print(count_occurrences([1, 4, 7], 10))           