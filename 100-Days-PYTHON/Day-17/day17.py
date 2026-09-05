#=========================================================================================
#------------------------------NUMBER TRANSFORMER-----------------------------------------
#=========================================================================================
numbers=[2,4,6,8,10]
squares=[x*x for x in numbers]
cubes=[x*x*x for x in numbers]
num=[x*5 for x in numbers]
print("Square of numbers:",squares)
print("Cubes of numbers:",cubes)
print("Numbers multiplied by 5:",num)

#===========================================================================================
#-----------------------------------EVEN NUMBER FILTER--------------------------------------
#===========================================================================================
numbers=[12,7,25,30,41,50,63,72]
even_num=[x for x in numbers if x%2==0]
print("Even numbers:",even_num)
odd_num=[x for x in numbers if x%2!=0]
print("Odd numbers:",odd_num)
great_num=[x for x in numbers if x>40]
print("Numbers greater than 40:",great_num)

#==========================================================================================
#--------------------------------------STUDENT MARKS---------------------------------------
#==========================================================================================
marks=[45,78,92,33,67,88,29,95]
passed=[x for x in marks if x>=40]
print("List of students passed:",passed)
above=[x for x in marks if x>80]
print("List of students scored above 80:",above)
grade=["Pass" if x>=32 else "Fail" for x in marks]
print("List of Every marks whether student is passed or not:",grade)

#==========================================================================================
#-----------------------------------BONUS CHALLENGE----------------------------------------
#----------------------------------SMART SENSOR DATA---------------------------------------
#==========================================================================================
distance=[15,45,8,32,60,12,27,5,50]
a=[x for x in distance if x<20]
print("Dangerous/Obstacle Zone:",a)
b=[x for x in distance if x>=20]
print("Safe Zone:",b)
c=["obstacle" if x<20 else "Clear" for x in distance]
print(c)
c=[x*2 for x in distance]
print("Hypothetical Calibration Factor:",c)
