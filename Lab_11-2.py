def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    clean_string = ''.join(input_string.split()).lower()
    
    # Check if the string is equal to its reverse
    return clean_string == clean_string[::-1]

# Example usage:
user_input = input("Madam, I'm Adam")
result = is_palindrome(user_input)

if result:
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")
