n=int(input("Enter the size of array:"))
a=[]
c=[]
for i in range(0,n):
    a.append(int(input("Enter the elements of array:")))
print("array:",a)
for i in a:
    if i not in c:
        c.append(i)
print("array:",c)