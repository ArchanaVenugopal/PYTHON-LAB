def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base**exp)
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))