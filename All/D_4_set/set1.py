setc1 = {"green", "blue"}
setc2 = {"blue", "yellow"}

print("Original sets:")
print(setc1)
print(setc2)

setc = setc1.union(setc2)

print("\nUnion of above sets:")
print(setc)

setn1 = {1, 1, 2, 3, 4, 5}

setn2 = {1, 5, 6, 7, 8, 9}

print("\nOriginal sets:")

print(setn1)
print(setn2)
print("\nUnion of above sets:")
setn = setn1.union(setn2)
print(setn)
