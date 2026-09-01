#==================================================================================
#--------------------------------ANIMAL SYSTEM-------------------------------------
#==================================================================================
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks!!")
class Cat(Animal):
    def sound(self):
        print("Cat meows!!")
anim1=Dog()
anim1.sound()
anim2=Cat()
anim2.sound()
print("-----------------------------------------------------------------------------")

#====================================================================================
#----------------------------SHAPE CALCULATOR----------------------------------------
#====================================================================================
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        rad=int(input("Enter radius of circle:"))
        area=3.14*3.14*rad
        print("Area of Circle:",area)
class Rectangle(Shape):
    def area(self):
        l=int(input("Enter length of rectangle:"))
        b=int(input("Enter breadth of rectangle:"))
        area=l*b
        print("Area of Rectangle:",area)
class Triangle(Shape):
    def area(self):
        b=int(input("Enter the base of the Triangle:"))
        h=int(input("Enter the height of the Triangle:"))
        area=(1/2)*b*h
        print("Area of Triangle:",area)
obj1=Circle()
obj1.area()
obj2=Rectangle()
obj2.area()
obj3=Triangle()
obj3.area()
print("------------------------------------------------------------------------")

#==============================================================================
#--------------------------ELECTRONICS SENSOR SYSTEM---------------------------
#==============================================================================
from abc import ABC, abstractmethod
class Sensor:
    @abstractmethod
    def read_data(self):
        pass
class UltrasonicSensor(Sensor):
    def read_data(self):
        print(" Ultrasonic Sensor is Reading distance...")
class IRSensor(Sensor):
    def read_data(self):
        print("Ir Sensor is Reading Infrared Signal...")
class TemperatureSensor(Sensor):
    def read_data(self):
        print("temperature Sensor is Reading Temperature...")
sensors=[UltrasonicSensor(),IRSensor(),TemperatureSensor()]
for sensor in sensors:
    sensor.read_data()
print("-------------------------------------------------------------------------")

#===============================================================================
#---------------------------BONUS CHALLENGE-------------------------------------
#--------------------------ROBOT CONTROL FRAMEWORK------------------------------
#===============================================================================
from abc import ABC, abstractmethod
class Bot:
    @abstractmethod
    def move(self):
        pass
    def stop(self):
        pass
class LineFollowerBot(Bot):
    def move(self):
        print("The bot is following the black line.")
    def stop(self):
        print("The Line Follower bot is stopped!!")
class ObstacleAvoidingBot(Bot):
    def move(self):
        print("The bot is moving while avoiding the obstacles")
    def stop(self):
        print("the Obstacle avoiding bot is stopped!!")
class HumanFollowerBot(Bot):
    def move(self):
        print("The bot is following Human")
    def stop(self):
        print("The Human Follower bot is stopped!!")
bots=[LineFollowerBot(),ObstacleAvoidingBot(),HumanFollowerBot()]
for bot in bots:
    bot.move()
    bot.stop()
print("-------------End of Day-14 Challenge----------------------")