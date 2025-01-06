def list(value):
    mi=min(value)
    return mi
res=list([12,33,22,44,123,423])
print(res)


def count33(values):
    repeat=0
    for i in values:
        if i==33:
            repeat += 1
    return repeat
print(count33([11,22,33,44,33,42,33,54,33,55,333,33]))
