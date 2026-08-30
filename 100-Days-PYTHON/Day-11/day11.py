#====================================================================
#--------------STUDENT--->ENGINEERING STUDENT------------------------
#====================================================================
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class EngineeringStudent(parent):
    def __init__(self,branch,college):
        self.branch=branch
        self.college=college
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Branch:",self.branch)
        print("College:",self.college)
stu1=EngineeringStudent("Electronics and Communication","GECM")
stu1.name="Bhoomika"
stu1.age=20
stu1.display()

#====================================================================
#-------------------------VEHICLE SYSTEM-----------------------------
#====================================================================
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display_info(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
obj1=Car("BMW",200)
obj1.display_info()
obj2=Bike("KTM",390)
obj2.display_info()

#=====================================================================
#----------------ELECTRONICS DEVICES----------------------------------
#=====================================================================
class device:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def display(self):
        print("Name:",self.name)
        print("Brand:",self.brand)
class Arduino(device):
    def __init__(self,name,brand,board_type):
        super().__init__(name,brand)
        self.board_type=board_type
    def display_arduino(self):
        self.display()
        print("Board:",self.board_type)
class ESP32(device):
    def __init__(self,name,brand,wifi):
        super().__init__(name,brand)
        self.wifi=wifi
    def display_ESP32(self):
        self.display()
        print("WIFI:",self.wifi)
ardu=Arduino("Arduino UNO","Arduino","ATmega328P")
esp32=ESP32("ESP32 Devkit","Espressif","Yes")
ardu.display_arduino()
print()
esp32.display_ESP32()

#==========================================================================
#------------------------BONUS CHALLENGE-----------------------------------
#-------------------------MINI ROBOT SYSTEM--------------------------------
#==========================================================================
class Device:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def display_info(self):
        print("Name:",self.name)
        print("Brand:",self.brand)
class Robot(Device):
    def __init__(self,name,brand,battery):
        super().__init__(name,brand)
        self.battery=battery
    def move(self):
        print("Move Forawrd")
class LineFollowerBot(Robot):
    def __init__(self,name,brand,battery,sensor_count):
        super().__init__(name,brand,battery)
        self.sensor_count=sensor_count
    def follow_line(self):
        print("Followed a Line")
    def stop(self):
        print("the robot stopped!!")
bot=LineFollowerBot("Line Follower","ESP32","7.4V",3)
bot.display_info()
bot.move()
bot.follow_line()
bot.stop()
print("End of Week-11 Challengee!!!")
