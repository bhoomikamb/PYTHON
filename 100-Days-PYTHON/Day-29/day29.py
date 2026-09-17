#Challenge-01
print("=====================================================================")
print("--------------------- Student Databases -----------------------------")
print("=====================================================================")
from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age: int
    marks: float
student1=Student("Bhoomi",20,743)
student2=Student("Sacchi",20,800)
print(student1)
print(student2)
print("--------------------------------------------------------------------")

#Challenge-02
print("=====================================================================")
print("--------------------- Employee Databases -----------------------------")
print("=====================================================================")
@dataclass
class Employee:
    name:str
    department:str
    salary:int=0
emp1=Employee("Abhi","E&CE")
print(emp1)
print("---------------------------------------------------------------------")

#Challenge-03
print("=====================================================================")
print("--------------------- Student result Databases ----------------------")
print("=====================================================================")
@dataclass
class Student:
    name:str
    marks:int
    def result(self):
        if self.marks>=40:
            return "Pass"
        return "Fail"
student1=Student("Bhoomika",50)
student2=Student("Sachin",45)
student3=Student("Amy",35)
print(student1)
print(student1.result())
print(student2)
print(student2.result())
print(student3)
print(student3.result())
print("--------------------------------------------------------------------")

#Challenge-04
print("=====================================================================")
print("---------------------- Sensor Databases -----------------------------")
print("=====================================================================")
@dataclass
class Sensor:
    name:str
    value:float
    unit:str
sensor1=Sensor("Temperature",25.5,"degree Celsius")
sensor2=Sensor("Distance",10,"cm")
sensor3=Sensor("Voltage",3.3,"V")
print(sensor1)
print(sensor2)
print(sensor3)
print("---------------------------------------------------------------------")

#Bonus Challenge
print("=====================================================================")
print("----------------------- Bonus Challenge -----------------------------")
print("------------------------- Smart Robot -------------------------------")
print("=====================================================================")
@dataclass
class Robot:
    name:str
    speed:int
    battery:float
    def status(self):
        if self.battery>=20:
            return "Robot is Ready!"
        return "Low Battery!!"
bot1=Robot("Line Follower Bot",150,50.5)
print(bot1)
print("Bot 1 Status:",bot1.status())
bot2=Robot("Obstacle Bot",90,15.8)
print(bot2)
print("Bot 2 Status:",bot2.status())