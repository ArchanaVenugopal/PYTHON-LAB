a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    value = input("Enter the word : ")
    a.append(value)
max_len = -1
for ele in a:
    if len(ele) > max_len:
        max_len = len(ele)
       # res = ele
print("Lenght of longest word is : ",max_len)

