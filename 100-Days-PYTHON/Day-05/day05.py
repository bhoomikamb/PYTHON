#==========================================================
#TUPLE BASICS
#==========================================================
subjects=("Biology","Python","Electronics","C","VLSI")
print(subjects)
print("The first subject is",subjects[0])
print("The last subject is",subjects[-1])
print("Total number of subjects is",len(subjects))
if "Biology" in subjects:
    print("The Subject exists!!")
else:
    print("The Subject doesn't exists!")
#subjects[0]="Maths" # It gives Type Error:'tuple' object doesn,t support item assignment.

#==========================================================
#STUDENT DETAILS
#==========================================================
student=("Jaan",21,"ECE","GECM")
for item in student:
    print(item)
name,age,branch,college=student
print(name)
print(age)
print(branch)
print(college)

#==========================================================
#REMOVE DUPLICATES USING SETS
#==========================================================
numbers=[10,20,10,30,20,40,30,50]
print("Original:",numbers)
unique=set(numbers)
print("Unique numbers:",unique)
print("Number of unique numbers:",len(unique))

#=========================================================
#BONUS CHALLENGE!!
#=========================================================
electronics={"Arduino","ESP32","Raspberry Pi","SJM32"}
programming={"Python","C","Arduino","Java"}
print(electronics|programming)
print(electronics & programming)
print(electronics - programming)
