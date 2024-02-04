def calculate_sum():
    total_sum = 0

    while True:
        user_input = input("-1")

        if user_input == "-1":
            break

        try:
            num = float(user_input)
            total_sum += num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return total_sum

# Example usage:
result = calculate_sum()
print(f"Sum of the entered numbers: {result}")
