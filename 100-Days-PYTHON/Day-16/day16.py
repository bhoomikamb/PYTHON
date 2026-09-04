#========================================================================================
#---------------------------LAMBDA CALCULATOR--------------------------------------------
#========================================================================================
add= lambda x,y: x+y
sub= lambda x,y: x-y
mul= lambda x,y: x*y
div= lambda x,y: x/y
square= lambda x: x*x
print("Addition:",add(2,5))
print("Subtration:",sub(10,17))
print("Multiplication:",mul(2,5))
print("Division:",div(2,4))
print("Square:",square(5))
print("---------------------------------------------------------------------------------")

#=========================================================================================
#---------------------------------map()+Lambda--------------------------------------------
#=========================================================================================
numbers=[1,2,3,4,5,6]
squares=map(lambda x : x*x,numbers)
print("Sqaures of numbers list:",list(squares))
print("---------------------------------------------------------------------------------")

#=========================================================================================
#---------------------------------filter()+Lambda-----------------------------------------
#=========================================================================================
numbers=[10,15,20,25,30,35,40,45]
lambda x: x%2==0
even_numbers=list(filter(lambda x:x%2==0,numbers))
print("Even numbers List:",even_numbers)
num=list(filter(lambda x: x>25,numbers))
print("Numbers greater than 25:",num)
numb=list(filter(lambda x:x/5, numbers))
print("Numbers divisible by 5:",numb)
print("--------------------------------------------------------------------------------")

#=========================================================================================
#------------------------------------BONUS CHALLENGE--------------------------------------
#-------------------------------STUDENT RANKING SYSYTEM-----------------------------------
#=========================================================================================
students=[
    {"Name":"A","marks":85},
    {"Name":"B","marks":72},
    {"Name":"C","marks":95},
    {"Name":"D","marks":64}
]
#Sort by marks
print(sorted(students,key=lambda student:student["marks"]))
#Ranking Order
ranked_students=sorted(students,key=lambda student:student["marks"],reverse=True)
#Display the Ranking
for student in ranked_students:
    print(student["Name"],":",student["marks"])
print("---------------------------------------------------------------------------------")
print("-------------------------------End of Day-16 Challenges--------------------------")