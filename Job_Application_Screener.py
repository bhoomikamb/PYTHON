a=input("Do you know Python???")
b=input("Do you have a college degree??")
c=int(input("How many years of work experience do you have??"))
if a=="yes" and (b=="yes" or c>=3):
    print("Congratulations, you are invited to an interview!!")
else:
    print("Sorry, we are moving forward with other candidates.")
