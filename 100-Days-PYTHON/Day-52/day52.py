#Introduction:Shallow Copy vs Deep copy
#Challenge-01
print("---------------------------------------------------------------------")
print("---------------------- Predict the output----------------------------")
print("---------------------------------------------------------------------")
import copy #importing a library called copy
numbers=[[10,20],[30,40]]
new=copy.copy(numbers) #Shallow copy changes by changing shallow copy
#both shallow and original get changed
new[1][0]=100
print(numbers) #Output is [[10,20],[100,40]]
print(new)  #Output is [[10,20],[100,40]]
print("---------------------------------------------------------------------")

#Challenge-02
print("---------------------------------------------------------------------")
print("--------------------- Shallow copy using a list ---------------------")
print("---------------------------------------------------------------------")
students=[["Bhoomi",85],["Anu",90]]
copied_students=copy.copy(students)
copied_students[1][1]=95 #Changing value of 1st index of outer list and 1st index of inner list
print(students)
print(copied_students)
print("--------------------------------------------------------------------")

#Challenge-03
print("---------------------------------------------------------------------")
print("---------------------------- Deep copy ------------------------------")
print("---------------------------------------------------------------------")
numbers=[[1,2],[3,4]]
neww=copy.deepcopy(numbers)
neww[0][1]=99
print(numbers)
print(neww)
print("--------------------------------------------------------------------")

#Challenge-04
print("---------------------------------------------------------------------")
print("---------------------- Predict the output----------------------------")
print("---------------------------------------------------------------------")
original=[[5,10],[15,20]]
shallow=copy.copy(original)
deep=copy.deepcopy(original)
shallow[0][1]=100
deep[1][1]=200
print("Original:",original) #Changes when we change in shallow
print("Shallow:",shallow) #Changes original list with it
print("Deep:",deep) #Changes only deep not the original list
print("-------------------------------------------------------------------")

#Challenge-05
print("---------------------------------------------------------------------")
print("---------------------- Student marks mini project -------------------")
print("---------------------------------------------------------------------")
students = [
    ["Bhoomi", [80, 85, 90]],
    ["Anu", [75, 88, 92]],
    ["Rahul", [70, 78, 84]]
]
shallow=copy.copy(students)
deep_copy=copy.deepcopy(students)
shallow[0][1][0]=95
deep_copy[1][1][1]=99
print("original:",students)
print("shallow:",shallow)
print("deep copy:",deep_copy)
print("---------------------------------------------------------------------")
print("---------------------- End of Day-52 Challenges ---------------------")
print("---------------------------------------------------------------------")
#End of Day-52 Challenges