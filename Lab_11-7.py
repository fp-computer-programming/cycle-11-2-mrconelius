def print_multiples_of_three(numbers):
    for num in numbers:
        if num % 3 != 0:
            continue
        print(num)

# Example usage:
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("Multiples of 3 in the list:")
print_multiples_of_three(number_list)
