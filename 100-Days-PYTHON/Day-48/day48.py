#revision enumerate()
#Challenge-01
print("------------------------------------------------------------------")
print("--------------------- Predict the output -------------------------")
print('------------------------------------------------------------------')
fruits=["Aplle","Mango","Grapes"]
for i,fruit in enumerate(fruits,start=1):
    print(i,fruit)
print("-----------------------------------")

#Challenge-02
print("--------------------------------------------------------------------")
print("--------------------- Number the students --------------------------")
print("--------------------------------------------------------------------")
students=["Anu","Abhi","Bhoomi"]
for index,student in enumerate(students,start=1):
    print(index,student)
print("----------------------------------")

#Challenge-03
print("--------------------------------------------------------------------")
print("--------------------- Find passing students ------------------------")
print("--------------------------------------------------------------------")
students=["Ananya","Bhavith","Cherika","Dravya"]
marks=[85,25,55,75]
for index,mark in enumerate(marks,start=1):
    if mark>=35:
        print(index,students[index-1],"is passed with marks",mark)
print("---------------------------------")

#Challenge-04
print("--------------------------------------------------------------------")
print("-------------------------- My own logic! ---------------------------")
print("--------------------------------------------------------------------")
tasks=["Study Python","Practice Coding","Revise OOP"]
for index,task in enumerate(tasks,start=1):
    print("Task",index,":",task)
print("--------------------------------------------------------------------")
print("------------------- End of Day-48 Challenges -----------------------")
print("--------------------------------------------------------------------")