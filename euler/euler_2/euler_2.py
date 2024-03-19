# Define a function to sum even Fibonacci numbers up to a maximum value
def sum_even_fibonacci(max_value):
    # Initialize the first two Fibonacci numbers and the sum of even terms
    a, b = 0, 1
    sum_even = 0
    
    # Generate Fibonacci numbers and sum even values until exceeding max_value
    while b <= max_value:
        # If the Fibonacci number is even, add it to the sum
        if b % 2 == 0:
            sum_even += b
        
        # Update the last two Fibonacci numbers
        a, b = b, a + b
        
    return sum_even

print(sum_even_fibonacci(4000000))

