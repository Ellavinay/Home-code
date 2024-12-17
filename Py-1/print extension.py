file = input("enter the data to file type : ")
for i in file:
    if "java" in file :
        print("java")
        break
    else:
        print("file extension java not present")
        break

def fun(data):
    if "java" in data:
        return "java"
    else:
        return "extension is not present in file"
res=fun(input("enter the file type: "))
result=fun(res)
print(result)