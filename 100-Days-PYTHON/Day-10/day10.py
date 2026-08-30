#===========================================================================
#----------------------------STUDENT CLASS----------------------------------
#===========================================================================
class Student:
    def __init__(self,name,age,branch,CGPA):
        self.name=name
        self.age=age
        self.branch=branch
        self.CGPA=CGPA
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Branch:",self.branch)
        print("CGPA:",self.CGPA)
student1=Student("Bhoomika",20,"ECE",8.45)
student2=Student("Sachin",21,"ECE",7.11)
student1.display()
student2.display()

#===========================================================================
#----------------------------BANK ACCOUNT-----------------------------------
#===========================================================================
class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",amount)
        print("Balance:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance!")
        else:
            self.balance-=amount
            print("Withdrawn:",amount)
            print("Balance:",self.balance)
    def display(self):
        print("Account Number:",self.account_number)
        print("Account Holder:",self.account_holder)
        print("Balance:",self.balance)
user1=BankAccount("1234567890","Bhoomika M B",10000)
user2=BankAccount("0987654321","Sachin A G",500000)
user1.deposit(500)
user1.withdraw(2000)
user1.display()
user2.deposit(1000)
user2.withdraw(6000)
user2.display()

#===========================================================================
#----------------------------ELCTRONICS DEVICES-----------------------------
#===========================================================================
class Device:
    def __init__(self,device_name,brand,price):
        self.device_name=device_name
        self.brand=brand
        self.price=price
    def display(self):
        print("Device Name:",self.device_name)
        print("Brand:",self.brand)
        print("Price:",self.price)
item1=Device("Smartphone","Samsung",50000)
item2=Device("Laptop","ASUS",80000)
item3=Device("Tablet","Apple",60000)
item1.display()
item2.display()
item3.display()

#===========================================================================
#--------------------------BONUS CHALLENGE----------------------------------
#----------------------MINI LIBRARY SYSTEM----------------------------------
#===========================================================================
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Year:",self.year)
book1=Book("Untill Love separate us","Durjoy Datta",2011)
book1.display()

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def display_books(self):
        for book in self.books:
            book.display()
lib=Library()
lib.add_book(book1)
lib.display_books()


        