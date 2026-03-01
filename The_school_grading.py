test=int(input("Enter the test score (0 to 100):"))
if test>100:
    print("You have entered invalid marks!! ")
elif test>=90 and test<=100:
    print("GRADE A")
elif test>=80 and test<90:
    print("GRADE B")
elif test>=70 and test<80:
    print("GRADE C")
else:
    print("GRADE F")