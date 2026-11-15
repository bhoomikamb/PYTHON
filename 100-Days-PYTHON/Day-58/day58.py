#Day-58 challenges
#Operator module
#Example
print("-----------------------------------------------------")
print("---------------------- Examples ---------------------")
print("-----------------------------------------------------")
import operator # importing operator library
a=10
b=5
print(operator.add(a,b)) #Addition
print(operator.mul(a,b)) #Multiplication
print(operator.lt(a,b)) #less than
print(operator.sub(a,b)) #Subtraction
print(operator.truediv(a,b)) #Division
print(operator.eq(a,b)) #Equal
print(operator.gt(a,b)) #Greater than
#print(operator.contains(a,b)) #checks membership
#itemgetter()
from operator import itemgetter
student=("Bhoomi",95,"ECE")
get_name=itemgetter(0) #Retrives an item from a list, tuple or dictionary
print(get_name(student))
#attrgetter()
from operator import attrgetter
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Bhoomii",95)
get_marks=attrgetter("marks") #retrives an attribute from an object
print(get_marks(s1))
print("-----------------------------------------------------")

#Challenge-01
print("-----------------------------------------------------")
print("------------ Basic mathematical operations ----------")
print("-----------------------------------------------------")
import operator
x=10
y=2
print("Addition:",operator.add(x,y))
print("Subtraction:",operator.sub(x,y))
print("Multiplication:",operator.mul(a,b))
print("Division:",operator.truediv(a,b))
print("-----------------------------------------------------")

#Challenge-02
print("-----------------------------------------------------")
print("------------- Student marks Comparison --------------")
print("-----------------------------------------------------")
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Bhoomii",95)
s2=Student("Bhaskar",85)
a=s1.marks
b=s2.marks
print(operator.gt(a,b))
print(operator.lt(a,b))
print(operator.eq(a,b))
print("-----------------------------------------------------")

#Challenge-03
print("-----------------------------------------------------")
print("----------- Sort students using itemgetter() --------")
print("-----------------------------------------------------")
from operator import itemgetter
students=[("Anu",85),("Bhoomii",95),("Rahul",72),("Priya",90)]
sorted_students=sorted(students,key=itemgetter(1),reverse=True)
print(sorted_students)
print("-----------------------------------------------------")

#Challenge-04
print("-----------------------------------------------------")
print("---------- Employee salary using attrgetter() -------")
print("-----------------------------------------------------")
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employee("Sachin",50000)
e2=Employee("Bhoomii",60000)
get_salary=attrgetter("salary")
get_name=attrgetter("name")
print(f"Salary of {get_name(e1)} is {get_salary(e1)}")
print(f"Salary of {get_name(e2)} is {get_salary(e2)}")
print("-----------------------------------------------------")

#Challenge-05
print("-----------------------------------------------------")
print("-------------- Shopping cart calculation  -----------")
print("-----------------------------------------------------")
import operator
from functools import reduce
prices=[100,250,150,300,200]
total=reduce(operator.add,prices) #Calculate total price
highest=max(prices)
lowest=min(prices)
is_present=operator.contains(prices,300) #membership operator
print("Toatl price:",total)
print("Highest:",highest)
print("Lowest:",lowest)
print("Is 300 present:",is_present)
print("-----------------------------------------------------")
print("--------------- End of Day-58 challenges ------------")
print("-----------------------------------------------------")
#End of Day-58 challenges out of 100-Days-Challenges