n = int(input("Input an integer : "))
print("The factors are ")
for i in range(1, n+1):
    if(n%i==0):
            print(i)
