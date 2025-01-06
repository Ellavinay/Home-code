# value=int(input("enter a value : "))
# dict={}
# for i in range(1,value):
#     dict[i] = i * i
# print(dict)
def prime(a):
    if a==1:
        return False
    else:
        for i in range(2,a):
            if i%a==0:
                return False
        return True
print(prime(7))