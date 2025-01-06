def same(value):
    result=0
    for i in value:
        if len(i) > 1 and i[0] == i[-1]:
            result +=1
    return result
print(same(['abc', 'xyz', 'aba', '1221','pop']))