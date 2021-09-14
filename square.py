number=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    value = int(input("Enter the elements : "))
    number.append(value)
    square = [n**2 for n in number]
print(square)