def first():
    emp=[]
    for i in range(30):
        emp.append(i**2)
    return emp[:5],emp[-5:]
first_five, last_five = first()
print("First 5 elements:", first_five)
print("Last 5 elements:", last_five)

list=[]
for i in range(30):
    list.append(i**2)
print(list[:5])
print(list[-5:])