def not_poor(data):
    a='The lyrics is good!'
    b="The lyrics is poor!"
    if "not" in data:
        return a
    elif "poor" in data :
        return b
    else:
        return "error"
print(not_poor('The lyrics is not that poor!'))  # Output: 'The lyrics is good!'
print(not_poor('The lyrics is poor!'))
print(not_poor('The vinay kumar ella'))