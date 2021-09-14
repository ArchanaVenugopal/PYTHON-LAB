a = (input("Enter the string : "))
index=a[0]
for i in range(len(a)):
    a = a.replace(index, "$")
    a=index+a[1:]
print(a)