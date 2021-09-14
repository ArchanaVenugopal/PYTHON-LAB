rows = int(input("Enter the limit: "))

for row in range(65, rows+1):

    for column in range(65, row + 1):

        print(chr(column), end=' ')

    print(" ")