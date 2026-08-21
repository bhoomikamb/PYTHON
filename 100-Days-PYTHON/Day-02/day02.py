#========================================================
#GREETING FUNCTION
#========================================================
name=input("Enter your good name:")
def greeting():
    print("Hello dear",name)
greeting()

#========================================================
#CALCULATOR FUNCTIONS
#========================================================
a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Sum:", add(a,b))
print("Difference:", sub(a,b))
print("Product:", mul(a,b))
print("Quotient:", div(a,b))

#========================================================
#STUDENT RESULT FUNCTION
#========================================================
def result():
    marks=int(input("Enter your marks:"))
    if (marks>=35):
        return "PASS"
    else:
        return "FAIL"
student_result=result()
print("Student result is:", student_result)

#========================================================
#BONUS CHALLENGE
#========================================================
def largest():
    a=int(input("Enter a first number:"))
    b=int(input("Enter a second number:"))
    c=int(input("Enter a third number:"))
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c    
largest_num=largest()
print("The largest number is", largest_num)
print("End of program")
