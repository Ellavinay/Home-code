from PIL.ImageChops import multiply


def list(values):
    count=1
    for i in values:
        count *=i
    return count
res=list([1,2,3,4,5])
print(f"The sum of list is :{res}")

def list1(value):
    mul = multiply(value)
    return mul

print(list1([1, 2, 3, 4, 5]))