def wor_len(n, text):
    word_len=[]
    txt = text.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
result = wor_len(3, "Python vina is a powerful programming language")
print(result)
