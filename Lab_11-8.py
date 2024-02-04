def length_multiples(input_list):
    new_list = [value * index for index, value in enumerate(input_list)]
    return new_list

# Test Case 1: List contains only integers
int_list = [1, 2, 3, 4, 5]
result_int = length_multiples(int_list)
print(f"Test Case 1: {int_list} -> {result_int}")

# Test Case 2: List contains integers and float values
mixed_list = [1, 2.5, 3, 4.5, 5]
result_mixed = length_multiples(mixed_list)
print(f"Test Case 2: {mixed_list} -> {result_mixed}")

# Test Case 3: List contains only strings
str_list = ["a", "b", "c", "d", "e"]
result_str = length_multiples(str_list)
print(f"Test Case 3: {str_list} -> {result_str}")
