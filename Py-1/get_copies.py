def string_copies(s, n):
    return s * n
s = input("Enter a string: ")
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = string_copies(s, n)
    print(f"Result: { result}")
