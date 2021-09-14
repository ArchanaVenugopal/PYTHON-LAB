class Publisher():
    def __init__(self,name):
       self.name=name
    def display(self):
        print("NAME:",self.name)

class Book(Publisher):
        def __init__(self,name,title,author):
            self.title=title
            self.author=author
            super().__init__(name)

        def display(self):
            print("NAME:",self.name,"TITLE:", self.title,"AUTHOR:", self.author)

class python(Book):
    def __init__(self,name,title,author,price,pages):
        self.price=price
        self.noofpages= pages
        super().__init__(name,title,author)
    def display(self):
        print("NAME:",self.name,"TITLE:",self.title,"AUTHOR:", self.author,"PRICE:",self.price,"PAGES:",self.noofpages)
name=input("Enter the name:")
title=input("Enter the title:")
author=input("Enter the name of author:")
price=int(input("Enter the price:"))
pages=int(input("Enter the number of pages:"))
t = Publisher(name)
b = Book(name,title,author)
p = python(name,title,author,price,pages)
p.display()
t.display()
b.display()