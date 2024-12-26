def value(d,x):
    if x in d:
        return f"The key {x} is present "
    else:
        return  f"The key {x} is not present "
print(value({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5))
print(value([12,33,556,66,55,44,33,33,],4))