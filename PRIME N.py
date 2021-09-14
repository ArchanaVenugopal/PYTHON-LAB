num = int(input("Enter a number: "))
i = 1
x = 0
print("Prime numbers are:")
while x < num:
    c = 0
    for j in range(1, i+1, 1):
        a = i % j
        if a == 0:
            c = c+1

    if c == 2:
        print(i)
        x = x+1

    i = i + 1


