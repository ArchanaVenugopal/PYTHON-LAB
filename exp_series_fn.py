n = int(input("Enter the limit:"))
x = int(input("Enter The value for x:"))
def exp():
    fact=1
    Sum = 1
    for i in range(1,n+1):
        fact = fact * i
        #print(fact)

        Sum += ((x**i)/fact)
    print("The sum of series is :",(Sum))
print(exp())