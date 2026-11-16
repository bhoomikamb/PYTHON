#Day-59
#Cached Property in Python
#Examples
print("------------------------------------------")
print("---------------- Examples ----------------")
print("------------------------------------------")
from functools import cached_property
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    @cached_property #calculates first access, it stores the calculated result, useful for expensive calculations
    def area(self):
        print("Calculating area:")
        return self.length*self.width
r=Rectangle(10,5)
print(r.area)
print(r.area)
del r.area #Deletes the cached attribute to make python calculate it again
print(r.area)
print("------------------------------------------")

#challenge-01
print("------------------------------------------")
print("---------- Student total marks -----------")
print("------------------------------------------")
class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @cached_property
    def total_marks(self):
        print("Calculating total marks:")
        return self.m1+self.m2+self.m3
s1=Student("Bhoomi",95,85,75)
print(s1.total_marks)
print(s1.total_marks)
del s1.total_marks
print(s1.total_marks)
print("------------------------------------------")

#Challenge-02
print("------------------------------------------")
print("---------- Employee annual salary --------")
print("------------------------------------------")
class Employee:
    def __init__(self,name,m1_salary,m2_salary,m3_salary,m4_salary,m5_salary,m6_salary,m7_salary,m8_salary,m9_salary,m10_salary,m11_salary,m12_salary):
        self.name=name
        self.m1_salary=m1_salary
        self.m2_salary=m2_salary
        self.m3_salary=m3_salary
        self.m4_salary=m4_salary
        self.m5_salary=m5_salary
        self.m6_salary=m6_salary
        self.m7_salary=m7_salary
        self.m8_salary=m8_salary
        self.m9_salary=m9_salary
        self.m10_salary=m10_salary
        self.m11_salary=m11_salary
        self.m12_salary=m12_salary
    @cached_property
    def annual_salary(self):
        print("Calculating annual salary:")
        return self.m1_salary+self.m2_salary+self.m3_salary+self.m4_salary+self.m5_salary+self.m6_salary+self.m7_salary+self.m8_salary+self.m9_salary+self.m10_salary+self.m11_salary+self.m12_salary
e1=Employee("Bhoomii",500,700,600,800,900,1000,1100,1200,1300,1400,1500,1600)
print(e1.annual_salary)
print(e1.annual_salary)
del e1.annual_salary
print(e1.annual_salary)
print("------------------------------------------")

#Challenge-03
print("------------------------------------------")
print("----------------- Circle area ------------")
print("------------------------------------------")
class Circle:
    def __init__(self,radius):
        self.radius=radius
    @cached_property
    def area(self):
        print("Calculating area")
        return 3.14*self.radius*self.radius
c1=Circle(3)
print(c1.area)
print(c1.area)
del c1.area
print(c1.area)
print("------------------------------------------")

#Challenge-04
print("------------------------------------------")
print("------------ Product final price  --------")
print("------------------------------------------")
class Product:
    def __init__(self,price,tax_rate):
        self.price=price
        self.tax_rate=tax_rate
    @cached_property
    def final_price(self):
        print("Calculating final price...")
        return self.price+(self.tax_rate/100)
p1=Product(500,20.5)
print(p1.final_price)
print(p1.final_price)
del p1.final_price
print(p1.final_price)
print("------------------------------------------")

#Challenge-05
print("------------------------------------------")
print("---------- Student result system ---------")
print("------------------------------------------")
class Student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    @cached_property
    def total_marks(self):
        print("Calculating total marks....")
        return (self.m1+self.m2+self.m3+self.m4+self.m5)
    @cached_property
    def average_marks(self):
        print("Calculating average marks....")
        return (self.m1+self.m2+self.m3+self.m4+self.m5)/5
s1=Student("Bhoomii",95,85,75,65,55)
print(s1.total_marks)
print(s1.average_marks)
print(s1.total_marks)
print(s1.average_marks)
del s1.total_marks
del s1.average_marks
print(s1.total_marks)
print(s1.average_marks)
if s1.total_marks>=135:
    print("The student is passedd!!")
else:
    print("The student is failed, tryy againn!!")
print(f"The student '{s1.name}' has total marks of '{s1.total_marks}' & average of '{s1.average_marks}'")
print("------------------------------------------")
print("------- End of Day-59 Challenges ---------")
print("------------------------------------------")
#End of Day-59 from 100-Days-Challenges