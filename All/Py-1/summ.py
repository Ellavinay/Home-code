def summ(a,b,c):
    sum=a+b+c

    if a == b == c:
        sum=sum*3
    return sum
print(summ(22,33,44))
print(summ(2,2,2))
print(summ(11,22,11))

a=int(input("enter A value : "))
b=int(input("enter B value :"))
c=int(input("enter C value :"))

if a != b !=c :
    print(a+b+c)
else:
    print((a+b+c)*3)