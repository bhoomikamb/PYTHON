#========================================================
#STUDENT PROFILE
#========================================================
student={"name":"Sachin",
         "age":21,
         "branch":"ECE",
         "college":"GECM",
         "cgpa":8.7}
print(student)
print("Student name is",student["name"])
print("Student's branch is",student["branch"])
print("student CGPA is",student["cgpa"])
student["year"]=3
student.pop("cgpa")
print("Updated dictionary is",student)

#========================================================
#CONTACT BOOK
#========================================================
contacts={}
for i in range(5):
    name=input("Enter the name:")
    number=input("Enter the contact number:")
    contacts[name]=number
print(contacts)
name=input("Enter your name:")
if name in contacts:
    print("The person exists!!")
    print("Their contact number is",contacts[name])
else:
    print("Contact not found!!")

#=======================================================
#SUBJECT MARKS
#=======================================================
marks={"Maths":85,
       "Python":92,
       "Electronics":78,
       "English":81}
for key in marks:
    total=sum(marks.values())
    average=total/len(marks)
highest_subject=list(marks.keys())[0]
highest_mark=marks[highest_subject]
lowest_subject=list(marks.keys())[0]
lowest_mark=marks[lowest_subject]
for subject,mark in marks.items():
    if mark>highest_mark:
        highest_mark=mark
        highest_subject=subject
    if mark<lowest_mark:
        lowest_mark=mark
        lowest_subject=subject
print("Total:",total)
print("Average:",average)
print("Highest:",highest_subject,highest_mark)
print("Lowest:",lowest_subject,lowest_mark)
print("Number of subjects:",len(marks))