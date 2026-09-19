#Challenge-01
print("==================================================================================")
print("------------------------------- Check a File -------------------------------------")
print("==================================================================================")
from pathlib import Path
file=Path("100-Days-Python/Day-32/student.txt")
file.touch() 
print("File created!!")  #Creating new text file
print(file.exists())  #To check whether the file is exist or not
print(file.is_file()) #To check if it is a file or not
print(file.is_dir()) #To check it is a directory
print("---------------------------------------------------------------------------------")

#Challenge-02
print("==================================================================================")
print("------------------------------- Create & Write -----------------------------------")
print("==================================================================================")
file=Path("100-Days-Python/Day-32/details.txt")
file.touch()
print("File Created!!")
file.write_text("My name is Bhoomika M.B .\nI'm pursuing in Government Enginerring College," \
"Hassan in ECE department") #Writing into file
content=file.read_text() #reading from file
print(content)
print("---------------------------------------------------------------------------------")

#Challenge-03
print("==================================================================================")
print("-------------------------- Create a Project Folder -------------------------------")
print("==================================================================================")
folder=Path("100-Days-Python/Day-32/Robot_Project")
robot=folder/"robot.py"
sensor=folder/"sensor.py"
motor=folder/"motor.py" #Creating file inside folder called Robot_Project
folder.mkdir(exist_ok=True) #Creating directory
robot.touch()
sensor.touch()
motor.touch()
print("The folder and files created successfully!!")
print("----------------------------------------------------------------------------------")

#Challenge-04
print("==================================================================================")
print("------------------------------ Find Python Files ---------------------------------")
print("==================================================================================")
project=Path("100-Days-Python/Day-32")
for file in project.glob("*.py"):
    print(file)
print("----------------------------------------------------------------------------------")

#Bonus-Challenge
print("==================================================================================")
print("-------------------------- Python Project Explorer -------------------------------")
print("==================================================================================")
folder=Path("100-Days-Python/Day-32/My_Python_Project")
folder.mkdir(exist_ok=True)
main=folder/"main.py"
calc=folder/"calculator.py"
sens=folder/"sensor.py"
read_me=folder/"README.txt"
main.touch()
calc.touch()
sens.touch()
read_me.touch()
print(folder.exists())
print(folder)
for file in folder.glob("*.py"): #to print only .py files
    print(file)
for file in folder.glob("*.txt"): #to print only .txt files
    print(file)
print("----------------------------------------------------------------------------------")
print("------------------------- End of Day-32 Challenges -------------------------------")
print("----------------------------------------------------------------------------------")