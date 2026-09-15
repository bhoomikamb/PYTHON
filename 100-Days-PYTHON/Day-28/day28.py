#Challenge-1
print("================================================================================")
print("------------------------- Simple Context Manager -------------------------------")
print("================================================================================")
class MyContext:
    def __enter__(self):
        print("Entering Context")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("Exiting context")
with MyContext():
    print("Inside Context")
print("-------------------------------------------------------------------------------")
#Challenge-2
print("================================================================================")
print("-------------------- Context Manager witha Value -------------------------------")
print("================================================================================")
class StudentContext:
    def __enter__(self):
        print("Student session started")
        return "Bhoomi"
    def __exit__(self,exc_type,exc_value,traceback):
        print("Student session ended")
with StudentContext() as name:
    print("Student:",name)
print("-------------------------------------------------------------------------------")
#Challenge-3
print("================================================================================")
print("------------------------ File Context Manager ----------------------------------")
print("================================================================================")
with open("python.txt","w")as file:
    file.write("Myself Bhoomika M.B.\n I'm Pre-final year student in ECE departement.")
with open("python.txt","r") as file:
    data=file.read()
    print("The contents of text file:",data)
print("-------------------------------------------------------------------------------")
#Challenge-4
print("================================================================================")
print("--------------------------- Robot Connection -----------------------------------")
print("================================================================================")
class RobotConnection:
    def __enter__(self):
        print("Connecting Robot")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("Disconnecting from robot")
with RobotConnection():
    print("Robot is moving")
    print("Robot Sensors are active!")
print("-------------------------------------------------------------------------------")
#Bonuss!!!
print("================================================================================")
print("-------------------------- Bonus Challenge -------------------------------------")
print("----------------------- Smart Sensor Session -----------------------------------")
print("================================================================================")
class SensorSession:
    def __enter__(self):
        print("Sensor Session Started!")
        return "Ultrasonic Sensor"
    def __exit__(self,exc_type,exc_value,traceback):
        print("Sensor Session Ended!")
with SensorSession() as sensor:
    print("Using:",sensor)
    print("Reading a Sensor!")
print("-------------------------------------------------------------------------------")
print("---------------------- End of Day-28 Challenges -------------------------------")
print("-------------------------------------------------------------------------------")