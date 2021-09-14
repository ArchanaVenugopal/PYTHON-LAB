rows = int(input("Enter the limit  : "))
for row in range(rows, 65, -1):

    for col in range(65, row):

        print(chr(col), end=' ')

    print("\r")