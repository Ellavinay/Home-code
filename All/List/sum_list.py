def list(values):
    sum1=sum(values)
    return sum1
res=list([22,33,44,55,66,77,88,66])
print(f"The sum of list is :{res}")

def list1(values1):
    count=0
    for x in values1:
        count +=x
    return  count
res1=list1([11,22,33,44,55,66,66,77])
print(f"The sum of list is :{res1}")