
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
matrix = [[0 for j in range(0, column)] for i in range(0, row)]
transpose = [[0 for j in range(0, row)] for i in range(0, column)]
print("enter first matrix elements")
for i in range(0, row):
    for j in range(0, column):
        matrix[i][j] = int(input("enter an element"))
print("Input matrix: ")
for i in range (row):
  for j in range (column):
    print(matrix[i][j], end = " ")
  print()

for j in range(column):
  for i in range (row):
    transpose[j][i]= matrix[i][j]

print('Transpose matrix: ')
for j in range (column):
    for i in range(row):
     print (transpose[j][i], end = " ")
    print()