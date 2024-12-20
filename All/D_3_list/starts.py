def num (value):
    count=0
    for i in value:
        if len(i) > 1 and i[0]==i[-1]:
           count +=1
    return count
print(num(['abc', 'xyz', 'aba', '1221']))