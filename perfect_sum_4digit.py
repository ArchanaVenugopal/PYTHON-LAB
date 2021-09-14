n1=int(input("Enter start limit:"))
n2=int(input("Enter end limit:"))
print("The numbers are: ")
for i in range(n1,n2+1):
    for j in range(1,i):
        if(i==j*j):
            num=i
            n=i
            c=0
            count = 0
            while( num > 0 ):
                a=num%10
                num=num//10
                count += 1
                if(a%2)!=0:
                    c=c+1
            if(c==0):
                #count = 0
                #while n != 0:
                    #n //= 10
                    #count += 1
                if(count == 4):
                    print(i)