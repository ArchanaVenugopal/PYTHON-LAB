lst = []
num = int(input("Enter number of elements: "))
for n in range(num):
    numbers = int(input('Enter the elements:  '))
    lst.append(numbers)
    s=0
for n in range(num):
    s=s+lst[n]
print("Sum of elements in given list is :",s)
#print("Sum of elements in given list is :", sum(lst))
