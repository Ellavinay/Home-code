def dup(values):
    list=set()
    for i in values:
        if i not in list:
            list.add(i)
    return list
print(dup([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))

list=[10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
b=set(list)
print(b)