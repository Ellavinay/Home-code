def data(a,b):
    for i in a:
        if b==i:
            return True
    return False
print(data([1, 5, 8, 3],3))
print(data([1, 5, 8, 3],-1))

