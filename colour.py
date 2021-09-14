col1 = []
m = int(input("Enter the Number of Elements : "))
for i in range(m):
    value = input("Enter the Elements : ")
    col1.append(value)
col2 = []
n = int(input("Enter the Number of Elements : "))
for j in range(n):
    value = input("Enter the Elements : ")
    col2.append(value)
result=[]
for i in range(m):
    for j in range(n):
        result = [value for value in col1 if value not in col2]

print("col1-col2",result)
