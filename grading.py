marks=int(input("Enter a marks of Student:"))
if marks>=90 and marks<=100:
    print("A Grade")
elif marks>=75 and marks<90:
    print("B Grade")
elif marks>=60 and marks<75:
    print("C Grade")
elif marks>=40 and marks<60:
    print("D Grade")
else:
    print("Fail")