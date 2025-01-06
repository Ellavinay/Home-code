def even(num):
    odd_list=[]
    for i in num:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
print(even([7, 8, 120, 25, 44, 20, 27]))


