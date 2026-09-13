print("===========================================================")
print("------------------ Basic Type Detector --------------------")
print("===========================================================")
from functools import singledispatch
@singledispatch
def identify(data):
    print("Unknown:",data)
@identify.register
def _(data:int):
    print("Integer:",data)
@identify.register
def _(data:str):
    print("String:",data)
@identify.register
def _(data:list):
    print("List:",data)
identify(5)
identify("Mithun Gowda")
identify([10,2,17])
print("-----------------------------------------------------------")

print("===========================================================")
print("------------------------Calculator ------------------------")
print("===========================================================")
@singledispatch
def calculate(data):
    print("Addition:",data)
@calculate.register
def _(data:int):
    print("Square of numbers:",data*data)
@calculate.register
def _(data:list):
    print("sum of List:",sum(data))
calculate(2)
calculate([10,2,17])
print("-----------------------------------------------------------")

print("===========================================================")
print("---------------------- Sensor data ------------------------")
print("===========================================================")
@singledispatch
def process_sensor(data):
    print("Parameter:",data)
@process_sensor.register
def _(data:int):
    print("Distance:",data,"cm")
@process_sensor.register
def _(data:float):
    print("Temperature:",data,"Celsius")
@process_sensor.register
def _(data:str):
    print("Sensor name:",data)
process_sensor(17)
process_sensor(1.2)
process_sensor("Ultrasonic Sensor")
print("-----------------------------------------------------------")

print("===========================================================")
print("------------------- Bonus Challenge -----------------------")
print("---------------- Robot Data Processor ---------------------")
print("===========================================================")
@singledispatch
def robot_data(data):
    print("Paramter:",data)
@robot_data.register
def _(data:int):
    print("Robot's Speed:",data)
@robot_data.register
def _(data:float):
    print("Battery Voltage:",data)
@robot_data.register
def _(data:list):
    print("Sensor readings:",data)
robot_data(150)
robot_data(7.5)
robot_data([10,15.5,18,17,2])
print("-----------------------------------------------------------")
print("------------- End of Day-26 Challenge! --------------------")
print("-----------------------------------------------------------")