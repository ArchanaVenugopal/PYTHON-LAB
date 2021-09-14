list1=['a','b','c','d'];
list2=[1,2,3,4,5,6];
print(list1)
print("list1[0]:",list1[0])
print(list1[2:])
print(list1[1:3])
print("list2[1:5]:",list2[1:5])
print(list1[-2])
list2[2]=600
print(list2)
del list2[2]
print(list2)
list3=list("hi all")
print(list3)
for x in list3:
    print(x,end=" ")
print