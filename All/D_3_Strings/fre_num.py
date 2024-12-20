def num(num):
    freq= { }
    for i in num:
        keys= freq.keys()
        if i in keys:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print(num([11,22,22,11,33,44,33,22,11,33,444,55,44,55,66,55]))