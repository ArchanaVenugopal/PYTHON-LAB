a = []
number = int(input("Enter the Number of Elements : "))
for i in range(number):
    value = int(input("Enter the Elements : "))
    a.append(value)

for i in range(number - 1):
    for j in range(0,number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("The Sorted List in Ascending Order : ", a)