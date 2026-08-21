#=======================================================
#STUDENT MARKS LIST
#=======================================================
student_marks=[20,21,24,23,25]
print("The list:",student_marks)
print("The first mark is",student_marks[0])
print("The last marks is ",student_marks[-1])
student_marks.append(19)
print("List after append:",student_marks)
student_marks.remove(24)
print("The updated list is",student_marks)
print("The total marks is",sum(student_marks))
print("The average marks is",sum(student_marks)/len(student_marks))

#=======================================================
#SHOPPING LIST
#=======================================================
shopping_list=[]
for i in range(5):
    item=input("Enter the item:")
    shopping_list.append(item)
for i in range(5):
    print(i+1,".",shopping_list[i])

#=======================================================
#FINDING LARGEST AND SMALLEST NUMBER
#=======================================================
num=[10,17,2,14,7]
print("The largest number is",max(num))
print("The smallest number is",min(num))
print("Total number of elements in list num is",len(num))
print("Sum of all the numbers is",sum(num))

#=======================================================
#BONUS CHALLENGE
#=======================================================
num=[23,7,45,12]
largest=num[0]
smallest=num[0]
for number in num:
    if number>largest:
        largest=number
    if number<smallest:
        smallest=number
print("Largest number:",largest)
print("Smallest number:",smallest)
print("Number of elements:",len(num))
print("Sum:",sum(num))
print("End of Week-03 Challenges..")

