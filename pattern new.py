rows = int(input("Enter a limit:"))

for row in range(1, rows+1):

    for column in range(1, row+1):

        print(column * row, end=' ')

    print("")

