a = (input("Enter a word : "))
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print("Count of each caharcter is: " ,str(freq))