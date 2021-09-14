str = (input("Enter the sentence : "))
len=len(str)
str=str[len-1]+str[1:len-1]+str[0]
print("The new string is:",str)