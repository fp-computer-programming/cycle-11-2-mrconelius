def fibonacci(n):
    # Initialize the Fibonacci sequence with the first two values
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the specified number of values
    for _ in range(2, m):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Print the Fibonacci sequence
    print(f"Fibonacci sequence with {m} values: {fib_sequence}")
    
    # Calculate and return the sum of the Fibonacci sequence
    return sum(fib_sequence)

# Example usage:
user_input = int(input("Enter a number between 2 and 100: "))

if 2 <= user_input <= 100:
    result = fibonacci(user_input)
    print(f"Sum of the Fibonacci sequence: {result}")
else:
    print("Please enter a number between 2 and 100.")
