a=[]
list=[]
value =input("Enter the word : ")
a.append(value)
vowels = ['a', 'e', 'i', 'o', 'u']
print("The vowels present in the word is:")
list = [i for i in value if i in vowels]
print(list)