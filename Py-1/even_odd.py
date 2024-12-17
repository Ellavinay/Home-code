def num(value):
    for i in value:
        if i%2==0:
            print( f"the given value {i} is even number")
        else:
            print( f"The given value {i} is odd number")


num([22, 33, 44])