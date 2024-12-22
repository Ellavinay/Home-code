from pickletools import string1


def data(n,str1):
    word_len=[]
    txt=str1.split(" ")
    for i in txt:
        if len(i) >n:
            word_len.append(i)
    return word_len
print(data(2,"The quick brown fox jumps over the lazy dog"))

a= "The quick brown fox jumps over the lazy dog"
b=a.split(" ")
print(b)