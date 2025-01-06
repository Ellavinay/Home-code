def num(num1,num2):
    # result = False
    for x in num1:
        for y in num2:
            if x==y:
                return  True
    return False
print(num([10, 22, 334, 44, 555], [555, 63, 74, 85, 9]))
print(num([1, 2, 3, 4, 5], [6,  7, 8, 9]))

def val(l1,l2):
    for item in l1:
        if item in l2:
            return True
    return False
print(val([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(val([1, 2, 3, 4, 5], [6, 7, 8, 9]))
print(val([5, 6, 7, 8],[9, 10]))