input_str = input("Enter a list of numbers separated by spaces: ")

numbers_list = [int(num) for num in input_str.split()]

sorted_numbers = sorted(numbers_list)
length = len(sorted_numbers)

if length % 2 == 0:
    mid1 = sorted_numbers[length // 2 - 1]
    mid2 = sorted_numbers[length // 2]
    median = (mid1 + mid2) / 2
else:
    median = sorted_numbers[length // 2]

print(f"The median of the list {numbers_list} is: {median}")
