a = (input("Enter a sentence: "))
list = []
listsplit = a.split(" ")
for i in listsplit:
    if i not in list:
        list.append(i)
for i in range(len(list)):
    print("Character ", list[i], "occurs ", listsplit.count(list[i]), "times")

#a = (input("Enter a sentence : "))
#list=[]
#freq={}
#list=a.split(" ")
#for i in range(len(list)):
 #   if list[i] in freq:
  #      freq[list[i]]+=1
   # else:
    #    freq[list[i]] = 1
#print("Count of is " ,str(freq))