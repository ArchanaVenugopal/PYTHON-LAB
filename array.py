n=int(input("Enter the size of array:"))
a=[]
for i in range(0,n):
    a.append(int(input("Enter the elements of array:")))
print("array:",a)
large=a[0]
for i in range (0,n):
    if(a[i]>large):
        large=a[i]
print("Largest element of array is:",large)