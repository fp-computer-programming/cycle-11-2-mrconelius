def name_multiplication():
    # Create a empty list to store names
    names = []

    # Get 5 names
    for_in range(5):
       name = input("Matthew, Blake, Jake, Aidan, Liam)
       names.append(name)

    print("\nPrinting names based on the number of unique letters:\n")

    for name in names:
        unique_leters = set(name.lower())
        print(f"{name}: ", end="")

      # Using a for loop to print each letter a number of times 
      for letter in unique_letters:
          count = name.lower().count(letter)
          print(letter * count, end-"**)

      # Using a while loop as a bonus
      index = 0
      while index < len(name):
          print (name[index], end-**)
          index += 1

      print("\n")

# Example usage:
name_multiplication()
