a=[]
c=0
n=int(input("Enter number of elements:"))
for i in range(n):
    value = input("Enter the Elements : ")
    for k in value:
        if k == "a":
            c=c+1
print("Number of times A occurs is:",c)
