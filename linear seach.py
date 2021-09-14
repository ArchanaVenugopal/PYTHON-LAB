def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
array = []
n = int(input("Enter the Number of Elements : "))
for i in range(n):
    value = int(input("Enter the Elements : "))
    array.append(value)

x = int(input("Enter the Element to be searched : "))
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)