class rect:
    def __init__(self):
        self.length = int(input("Enter the length :"))
        self.width= int(input("Enter the width :"))
        print("-----------------------------------------")
    def area(self):
        return self.length*self.width

    def __lt__(self, o):
        if (self.area() < o.area()):
            return True
        else:
            return False


rect1 = rect()
rect2 = rect()
if (rect1 < rect2):
    print("rectangle 1 is smaller than rectangle 2")
else:print("rectangle 2 is smaller than rectangle 1")