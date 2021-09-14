a = []
n = int(input("Enter the Number of Elements : "))
for i in range(n):
    value = int(input("Enter the Elements : "))
    a.append(value)
result=[]
#for i in range(number):
for i in a:
    if(i%2!=0):
        result.append(i)
print("New list is :",result)