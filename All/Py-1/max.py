def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max=i
    return max
res=max([22,3,90,44,5,43,23,44])
print(res)

a=[22,3,90,44,5,43,23,44]
a.sort(reverse=True)
print(a)
b=a[0]
print(b)

