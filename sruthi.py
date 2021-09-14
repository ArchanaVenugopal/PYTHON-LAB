rows=6
for i in range(0,rows):
    for j in range(1,i+1):
        print("*",end=' ')
    print("\r")
if(j==5):
    for i in range(rows,0,-1):
        for j in range(1,i-1):
            print("*",end=' ')
        print("\r")