def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage:
print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(calculate_average([]))  # Output: 0
print(calculate_average([1, 2, 'a', 4, 5]))  # Output: 0
print(calculate_average([1.5,2.5,3.5])) # Output: 2.5