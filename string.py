string="myprogram.exe"
print(string[5:9])
print(string[0:9])
length=len(string)//2
print(length)
n=len(string)
#print(string[length])
for i in range(n-1,-1,-1):
    print(string[i])
c=input("Enter a char:")
for i in range(n-1):
    if(c==string[i]):
     print(i)

