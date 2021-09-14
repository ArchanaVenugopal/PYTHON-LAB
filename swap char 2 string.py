
s1=input("Enter first string:")
s2=input("Enter second string:")
new_a = s2[:1] + s1[1:]
new_b = s1[:1] + s2[1:]
str=new_a + ' ' + new_b
print("The string after swap is: ",str)