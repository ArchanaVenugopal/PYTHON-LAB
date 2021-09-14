
lambda_square = lambda y: y * y
s=int(input("Enter side of square:"))
print("The area of square is:")
print(lambda_square(s))
lambda_rect = lambda l,h: l * h
l=int(input("Enter lenght of rectangle:"))
h=int(input("Enter height of rectangle:"))
print("The area of rectangle is:")
print(lambda_rect(l,h))
lambda_tri = lambda b,m: 1/2*(b * m)
b=int(input("Enter base of triangle:"))
m=int(input("Enter height of triangle:"))
print("The area of triangle is:")
print(lambda_tri(b,m))