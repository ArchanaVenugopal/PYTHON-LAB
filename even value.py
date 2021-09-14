a = []
res=[]
number = int(input("Enter the Number of Elements : "))
for i in range(number):
    value = int(input("Enter the Elements : "))
    a.append(value)
res=[i for i in a if i>=0]
print(res)