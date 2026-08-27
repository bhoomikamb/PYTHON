#========================================================================
#---------------------------MATH MODULE----------------------------------
#========================================================================
from math import sqrt,factorial
from math import pow,pi
print("Square root of 25 is",sqrt(25))
print("Factorial of 24 is",factorial(24))
print("Power of 2 is",pow(2,2))
print("Value of Pi is",pi)

#=======================================================================
#-------------------------RANDOM NUMBER GENERATOR-----------------------
#=======================================================================
import random as r
number=r.randint(1,10)
print("Random number:",number)
for i in range(5):
    number=r.randint(1,100)
    print(number)
secret=r.randint(1,10)
guess=int(input("Guess the number between 1 and 10:"))
if guess==secret:
    print("Correct!")
else:
    print("Wrong! The number was",secret)

#========================================================================
#-------------------------YOUR OWN MODULE--------------------------------
#========================================================================
import my_calculator
print(my_calculator.add(10,20))
print(my_calculator.subtract(10,30))
print(my_calculator.multiply(2,3))
print(my_calculator.divide(2,10))

#========================================================================
#----------------------BONUS CHALLENGE-----------------------------------
#------------------------MINI UTILITY MODULE-----------------------------
#========================================================================
import utility
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        celsius=float(input("Enter Celsius temperature"))
        print("Celsius to Fahrenheit",utility.celsius_to_fahrenheit(celsius))
    elif choice==2:
        fahrenheit=float(input("Enter Fahrenheit temperature"))
        print("Fahrenheit to Celsius",utility.fahrenheit_to_celsius(fahrenheit))
    elif choice==3:
        kilometer=float(input("Enter kilometer"))
        print("Kilometer to Meter",utility.kilometer_to_meter(kilometer))
    elif choice==4:
        meter=float(input("Enter meter"))
        print("Meter to Kilometer",utility.meter_to_kilometer(meter))
    elif choice==5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
print("----------End of Program----------")