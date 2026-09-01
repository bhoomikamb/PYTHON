#=========================================================================
#------------------------STUDENT PROFILE----------------------------------
#=========================================================================
class Student:
    def __init__(self,marks):
        self.__marks=marks
    def set_marks(self,mark):
        if mark>0:
            self.__marks=mark
        else:
            print("Marks can't be Negative!!")
    def get_marks(self):
        return self.__marks
student=Student(750)
print("Initial marks:",student.get_marks())
student.set_marks(800)
print("Updated marks:",student.get_marks())

#==========================================================================
#-----------------------BANK ACCOUNT---------------------------------------
#==========================================================================
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Amount can't be Negative!")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Enter Valid Amount!!")
    def get_balance(self):
        return self.__balance
account=BankAccount(50000)
account.deposit(10000)
account.withdraw(2000)
print(account.get_balance())

#=======================================================================
#---------------------------EMPLOYEE SALARY-----------------------------
#=======================================================================
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("salary cannot be Negative!!")
    def get_salary(self):
        return self.__salary
emp=Employee(5000)
print("Initial Salary:",emp.get_salary())
emp.set_salary(6000)
print("Icremented Salary:",emp.get_salary())

#=====================================================================
#-------------------------BONUS CHALLENGE-----------------------------
#-----------------------SECURE ATM SYSYTEM----------------------------
#=====================================================================
class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def verify_pin(self,pin):
        return pin == self.__pin
    def check_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Amount can't be Negative!!")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Amount withdrawn successfully!!")
        else:
            print("Insufficient Balance / Invalid Amount!!")
    def change_pin(self,pin,new_pin,confirm_pin):
        if pin!=self.__pin:
            print("Incorrect old PIN!")
            return
        if new_pin!=confirm_pin:
            print("PIN doesn't match!")
            return
        self.__pin=new_pin
        print("PIN changed Successfully!!")
        def display(self):
            print("Balance:",self.__balance)
atm=ATM("1002",5000)
pin=input("Enter old PIN:")
new_pin=input("enter new PIN:")
confirm_pin=input("Confirm new PIN:")
if atm.verify_pin(pin):
    print("Correct PIN!")
    atm.deposit(10000)
    atm.withdraw(2000)
    print("Current Balance:",atm.check_balance())
    atm.change_pin(pin,new_pin,confirm_pin)
else:
    print("Incorrect PIN!!")
