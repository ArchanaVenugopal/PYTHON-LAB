a=[]
list=[]
value =input("Enter the word : ")
a.append(value)
vowels = ['a', 'e', 'i', 'o', 'u']
print("The vowels present in the word is:")
for i in a:
    if a[i] in vowels:
        print(a[i])