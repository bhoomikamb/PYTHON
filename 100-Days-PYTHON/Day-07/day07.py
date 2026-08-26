#=================================================================
#-----------------SAFE CALCULATOR-------------------------------
#==================================================================
try:  
    a=int(input("Enter a first number:"))
    b=int(input("Enter a second number:"))
    c=a/b
except ValueError:
    print("Enter the number in digits only")
except ZeroDivisionError:
    print("Try with other numbers except zero.")
else:
    print("The Quotient is",c)

#===================================================================
#-----------------SAGE AGE INPUT-----------------------------------
#===================================================================
try:
    age=int(input("Enter your age:"))
    print("Your age is",age)
except ValueError:
    print("Please enter valid age in digits")
if age<=0:
    print("Age can't be negative!! PLease enter correct age")
else:
    print("Your age is",age)

#==================================================================
#-------------------------SAFE LIST ACCESS------------------------
#==================================================================
try:
    even_num=[2,4,6,8,10]
    index=int(input("Enter a index of list:"))
    print("Element of my index is",even_num[index])
except IndexError:
    print("Please Enter a valid index of the list!!")
else:
    print("The element of index is:",even_num[index])

#=================================================================
#----------------------BONUS CHALLENGE---------------------------
#--------------------ROBUST CALCULATOR---------------------------
#================================================================
while True:
    try:
        num1=float(input("Enter a first number:"))
        oper=input("Enter an opeartor (+,-,/,*)")
        num2=float(input("Enter a second number"))
        if oper=="+":
            result=num1+num2
        elif oper=="-":
            result=num1-num2
        elif oper=="/":
            result=num1/num2
        elif oper=="*":
            result=num1*num2
        else: 
            print("Invalid operator!!")
            continue
        print("Result",result)
    except ValueError:
        print("Please enter numbers onlyy")
    except ZeroDivisionError:
        print("Cannot divide by zero.")


