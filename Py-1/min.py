def min(items):
    min = items[0]
    for i in items:
        if i < min :
            min = i
    return min
a=min([22,33,44,55,700,2,10,1])
print(a)