def string(input_string,n):
    if n<0:
        return "the value should not be less than 0"
    return input_string * n
print(string("vinay ",3))
print(string("kumar ",9))
print(string("ella",0))