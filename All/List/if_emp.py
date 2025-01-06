# list=[]
# if not list:
#     print("emp")
def ls(value):
    if not value:
        return "list is empty"
    return "list is occupied"
print(ls([]))
print(ls([11,22,33]))
print(ls([]))