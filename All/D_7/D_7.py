def prime(a):
    if(a==1):
        return False
    else:
        for i in range (2,a):
            if (a % i==0):
                return False
            return True
print(prime(7))