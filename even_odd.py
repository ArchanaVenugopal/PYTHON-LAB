n=int(input("Enter a first number"))
m=int(input("Enter a second number"))
o=str(input("Enter an operator"))
if o=='+':
    sum=int(n)+int(m)
    print("The sum of {0} and {1} is {2}".format(n,m,sum))
elif o == '-':
    diff = int(n) - int(m)
    print("The difference of {0} and {1} is {2}".format(n, m, diff))
elif o == '*':
    p = int(n) * int(m)
    print("The product of {0} and {1} is {2}".format(n, m, p))
elif o == '/':
    q = int(n) / int(m)
     print("The quotient of {0} and {1} is {2}".format(n, m, q))
    else:
     print("invalid operator")
