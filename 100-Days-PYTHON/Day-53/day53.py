#Introduction to Python Type Hints
#Challenge-01
print("----------------------------------------------------------------")
print("------------------- Student information ------------------------")
print("----------------------------------------------------------------")
def student_info(name:str,age:int)->str:
    return f"Student name is {name} of age {age}"
    pass
print(student_info("Bhoomi",20))
print("-----------------------------------------")

#Challenge-02
print("----------------------------------------------------------------")
print("------------------- Calculate the area -------------------------")
print("----------------------------------------------------------------")
def rectangle_area(length:float,width:float)->float:
    return length*width
    pass
print("Area of Rectangle is:",rectangle_area(10.5,20.5))
print("-----------------------------------------")

#Challenge-03
print("----------------------------------------------------------------")   
print("---------------------- Check eligibility -----------------------")
print("----------------------------------------------------------------")
def is_eligible(age:int)->bool:
    if age>=18:
        return True
    else:
        return False
    pass
print(is_eligible(25))
print(is_eligible(16))
print("-----------------------------------------")

#challenge-04
print("----------------------------------------------------------------")
print("----------------------- List of marks --------------------------")
print("----------------------------------------------------------------")
def calculate_average(marks:list[int])->float:
    return sum(marks)/len(marks)
    pass
print(calculate_average([80,90,70,60,50]))
print("----------------------------------------")

#Challenge-05
print("----------------------------------------------------------------")
print("--------------- Mini Project: Simple Calculator ----------------")
print("----------------------------------------------------------------")
def calculator(a:float,b:float,operation:str)->float:
    if operation=="+":
        return a+b
    if operation=="-":
        return a-b
    if operation=="/":
        if b != 0:
            return a/b
        else:
            return "Error: Division by zero is not allowed."
    if operation=="*":
        return a*b
    pass
print(calculator(10,5,"+"))
print(calculator(10,5,"-"))
print(calculator(10,5,"*"))
print(calculator(10,0,"/"))
print(calculator(10,5,"/"))
print("----------------------------------------------------------------")
print("------------------- End of Day-53 Challenges -------------------")
print("----------------------------------------------------------------")
#Day-53 Challenges completed successfully