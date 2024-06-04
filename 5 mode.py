from collections import Counter

input_str = input("Enter a list of numbers separated by spaces: ")

numbers_list = [int(num) for num in input_str.split()]

counts = Counter(numbers_list)

max_count = max(counts.values())

modes = [num for num, count in counts.items() if count == max_count]

if len(modes) == 1:
    print(f"The mode of the list {numbers_list} is: {modes[0]}")
else:
    print(f"The list {numbers_list} has multiple modes: {modes}")
