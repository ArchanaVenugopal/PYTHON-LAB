array = []
n = int(input("Enter the Number of Elements : "))
for i in range(n):
    value = int(input("Enter the Elements : "))
    array.append(value)
item = int(input("Enter the Element to be inserted : "))
index = int(input("Enter the index value : "))
array.insert(index, item)

print(array)
