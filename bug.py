def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Example of the bug
my_list_with_strings = [10, '20', 30, 40, 50]
average_bug = calculate_average(my_list_with_strings)
print(f"The average with strings is: {average_bug}")