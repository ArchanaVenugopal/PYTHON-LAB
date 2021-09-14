a=input("Enter the word : ")
word=[]
length=len(a)
for i in range(length):
    word.insert(i,a[i])
ordinal=[ord(word[i]) for i in range(length)]
print(ordinal)
