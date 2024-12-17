def num(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
print(num(1000))
print(num(20300))
print(num(1100))