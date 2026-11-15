#Day-57 of 100-Days Challenges
#total ordering
#Examples
print("------------------------------------------")
print("--------------- Examples -----------------")
print("------------------------------------------")
from functools import total_ordering
@total_ordering #decorator helps generate the remaining comparison methods ourselves
class Student:
    def __init__(self,marks):
        self.marks=marks
    def __eq__(self,other):
        return self.marks==other.marks
    def __lt__(self,other):
        return self.marks<other.marks
s1=Student(85)
s2=Student(90)
print(s1<s2)
print(s1==s2)
print(s1>s2)
print(s1<=s2)
print(s1>=s2)
print(s1==s2)
print("------------------------------------------")

#Challenge-01
print("------------------------------------------")
print("--------- Compare two products -----------")
print("------------------------------------------")
from functools import total_ordering
@total_ordering
class Product:
    def __init__(self,price):
        self.price=price
    def __eq__(self,other):
        return self.price==other.price
    def __lt__(self,other):
        return self.price<other.price
p1=Product(500)
p2=Product(800)
print(p1<p2)
print(p1==p2)
print(p1>p2)
print("------------------------------------------")

#Challenge-02
print("------------------------------------------")
print("------- Compare employee salaries --------")
print("------------------------------------------")
@total_ordering
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __eq__(self,other):
        return self.salary==other.salary
    def __lt__(self,other):
        return self.salary<other.salary
e1=Employee("Anu",30000)
e2=Employee("Bhoomii",40000)
print(e1<e2)
print(e1>=e2)
print("------------------------------------------")

#Challenge-03
print("------------------------------------------")
print("--------- Compare Student marks ----------")
print("------------------------------------------")
@total_ordering
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __eq__(self,other):
        self.marks==other.marks
    def __lt__(self,other):
        self.marks<other.marks
s1=Student("Anu",85)
s2=Student("Bhoomi",95)
print(s1<s2)
print(s1<=s2)
print(s1==s2)
print("------------------------------------------")

#Challenge-04
print("------------------------------------------")
print("--------------- Sort products ------------")
print("------------------------------------------")
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __eq__(self,other):
        return self.price==other.price
    def __lt__(self,other):
        return self.price<other.price
Products=[Product("Laptop",50000),
          Product("Mouse",500),
          Product("Keyboard",1500),
          Product("Monitor",12000)]
sort_product=sorted(Products)
print(sort_product)
for product in sort_product:
    print(product.name,product.price)
print("------------------------------------------")

#Challenge-05
print("------------------------------------------")
print("--- Mini-project=Student ranking system --")
print("------------------------------------------")
from functools import total_ordering
@total_ordering
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __eq__(self,other):
        self.marks==other,self.marks
    def __lt__(self,other):
        self.marks<other.marks
students=[Student("Anu",83),
          Student("Bhoomii",95),
          Student("Rahul",75),
          Student("Priya",90)]
sort_students=sorted(students)
for student in sort_students:
    print(student.name,student.marks)
print("------------------------------------------")
print("------------ End of Day-57 ---------------")
print("------------------------------------------")
#End of Day-57 Challenges