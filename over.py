a = []
number = int(input("Enter the Number of Elements : "))
for i in range(number):
    value = int(input("Enter the Elements : "))
    a.append(value)
#for i in range(number):
    res = ['over' if value >100 else value for value in a]
print("The list after replacement:", str(res))