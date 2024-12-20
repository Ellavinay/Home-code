def value(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return  a+b
    else:
        return "Given both values should be integer"
print(value(33,44))
print(value("vinay",33))