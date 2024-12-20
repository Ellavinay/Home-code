def count4(num):
    count=0
    for i in num :
        if i == 4:
            count +=1
    return count
print(count4([2,3,5,6,7,4]))
print(count4([2,3,4,4,5,6,7]))
print(count4([2,3,4,4,5,6,7,4]))
print(count4([4,3,4,4,5,6,7,4]))
