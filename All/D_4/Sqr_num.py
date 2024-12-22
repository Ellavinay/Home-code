def values():
    emplist=list()
    for i in range (1,31):
        emplist.append(i**2)
    print(emplist[:5])
    print(emplist[-5:])
print(values())
