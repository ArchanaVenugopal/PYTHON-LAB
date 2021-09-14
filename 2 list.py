a = []
m = int(input("Enter the Number of Elements : "))
for i in range(m):
    value = int(input("Enter the Elements : "))
    a.append(value)
b = []
n = int(input("Enter the Number of Elements : "))
for j in range(n):
    value = int(input("Enter the Elements : "))
    b.append(value)

#Check lists length
if(len(a)==len(b)):
    print("The lists are of same length")
else:
    print("The lists are of different length")

#sum same
print("Sum of list A:",sum(a))
print("Sum of list B:",sum(b))
if(sum(a)==sum(b)):
    print("The sum of elements in lists are the same")
else:
     print("The sum of elements in lists are different")

#intersection
#for i in range(m):
 #   for j in range(n):
  #      if(a[i]==b[j]):
   #         print(a[i],"is in both lists")
        #else:
            #print("No common elemets")
if (set(a) & set(b)):
      print("Common Element :",set(a) & set(b))
else:
    print("No common elements")
