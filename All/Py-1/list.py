# Accept a sequence of comma-separated numbers from the user
input_data = input("Enter a sequence of comma-separated numbers: ")

# Generate a list by splitting the input string
numbers_list = input_data.split(",")

# Generate a tuple by converting the list
numbers_tuple = tuple(numbers_list)

# Display the results
print("List:", numbers_list)
print("Tuple:", numbers_tuple)
