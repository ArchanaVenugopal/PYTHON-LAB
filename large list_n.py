list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(0, num):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print("Largest element is:", max(list1))