# Python Average Calculation Function Bug

This repository demonstrates a common bug in Python functions that calculate averages: the failure to handle non-numeric input.

## Bug Description
The `calculate_average` function is designed to calculate the average of a list of numbers.  It correctly handles the case of an empty list to prevent a `ZeroDivisionError`. However, if the input list contains non-numeric values (like strings), a `TypeError` occurs because `sum()` cannot handle non-numeric data types.

## Solution
The solution involves adding input validation to the function. This ensures that only numbers are processed, preventing the `TypeError`.  The improved function uses a `try-except` block to gracefully handle the case where non-numeric input is encountered.
