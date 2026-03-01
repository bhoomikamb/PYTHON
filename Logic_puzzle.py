a=int(input("Enter the Year:"))
if a%400==0:
    print("Leap Year!!")
elif a%100==0:
    print("Not a leap year.")
elif a%4==0:
    print("Leap Year!!")
else:
    print("Not a leap year.")