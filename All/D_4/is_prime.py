def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))
print(is_prime(17))
print(is_prime(180))