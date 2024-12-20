# a=int(input("enter value : "))
# b=int(input("enter value : "))
#
#
# if a==b or a+b==5 or abs(a-b)==5:
#     print(True)
# else:
#     print(False)

def value(a,b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False
print(value(5,5,))
print(value(5,0))
print(value(12,-7))
print(value(5,11))