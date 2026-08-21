#=====================================================
#DAY-01 CHALLENGE
# Personal information
#=======================================================
name=input("Enter your name: ")
age=int(input("Enter your age: "))
college=input("Enter your college name: ")
branch=input("Enter your branch: ")
current_cgpa=float(input("enter your current CGPA: "))
print("========STUDENT DETAILS========")
print("Name:",name)
print("Age:",age)
print("College:",college)
print("Branch:",branch)
print("Current CGPA:",current_cgpa)

#=======================================================
#MINI CALCULATOR
#=======================================================
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Simple calculations between 2 numbers")
print("Sum: ",a+b)
print("Subtration: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Floor division:", a//b)
print("Remainder:", a%b)
print("Power:",a**b)

#=======================================================
#SHOPPING BILL
#=======================================================
item_price=int(input("Enter the price of the item"))
quantity=int(input("Enter the quantity of the item"))
discount_percentage=int(input("Enter the discount percentage"))
total=item_price*quantity
discount=total*discount_percentage/100
final_amount=total-discount
print("TOTAL:",total)
print("DISCOUNT:",discount)
print("FINAL AMOUNT:",final_amount)

#=======================================================
#BONUS CHALLENGE
#=======================================================
birth_year=int(input("Enter your birth year: "))
current_year=int(input("Enter the current year: "))
age=current_year-birth_year
print("The approximate age of the person is:",age)
