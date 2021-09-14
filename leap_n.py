#x=2020
year=int(input("Enter limit:"))
print("Leap years are:")
for i in range(2020, year):
    if (i % 4 == 0) and (i % 100 != 0) or (i%400==0):
        print(i)
