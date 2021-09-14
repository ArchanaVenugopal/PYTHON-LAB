file = open("test.txt", "r")
data=file.read()
words=data.split()
print(len(words))