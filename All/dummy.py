def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result

def list1(value):
    mul = multiply(value)
    return mul

print(list1([1, 2, 3, 4, 5]))
