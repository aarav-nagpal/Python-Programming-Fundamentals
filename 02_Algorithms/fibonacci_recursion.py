def fibonacci_recursive(n):
    """
    Returns the nth Fibonacci number using recursion.
    Note: Recursive approach is simple but O(2^n) time complexity.
    """
    # Base cases: 0 and 1 are the starting points
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive step: sum of the previous two numbers
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Generate the first 7 numbers in the sequence
print("First 7 Fibonacci numbers:")
for i in range(7):
    print(fibonacci_recursive(i), end="  ")
