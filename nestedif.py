n1=int(input("Enter a first number"))
n2=int(input("Enter a second number"))
n3=int(input("Enter a third number"))
if(n1>n2):
    if(n1>n3):
        print("The largest is"+str(n1))
    elif(n2>=n3):
     print("The largest is "+str(n2))
else:
        print("The largest is"+str(n3))

