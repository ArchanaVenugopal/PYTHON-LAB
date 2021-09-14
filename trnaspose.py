m=int(input("Enter the row size : "))
n=int(input("Enter the column size : "))
mat1 = [[0 for j in range(0, n)] for i in range(0, m)]
b = [[0 for j in range(0, m)] for i in range(0, n)]
print("Enter the elements of matrix 1 : ")
for i in range(0,m):
    for j in range(0,n):
        mat1[i][j] = int(input("enter an element"))
print("Matrix 1 : ")
for i in range(0,m):
    for j in range(0,n):
        print(mat1[i][j],end=" ")
    print()

print("Matrix transpose : ")
for j in range(n):
    for i in range(m):
        b[j][i]=mat1[i][j]
for j in range(n):
    for i in range(m):
        print(b[j][i],end=" ")
    print()