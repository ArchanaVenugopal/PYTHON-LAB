list=[]
number = int(input("Enter the Number of Elements : "))
for i in range(number):
    value = int(input("Enter the Elements : "))
    list.append(value)
print("List Before ", list)
temp_list = []
for i in list:
    if i not in temp_list:
        temp_list.append(i)

#my_list = temp_list
print("List After removing duplicates ", temp_list)