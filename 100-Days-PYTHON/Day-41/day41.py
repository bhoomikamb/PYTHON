#Enumerate()
#Challenge-01
print("------------------------------------------------------------------------")
print("------------------------- Numbered Names -------------------------------")
print("------------------------------------------------------------------------")
fruits=["Apple","Banana","Cheery","Dragon","Strawberry"]
for index,fruit in enumerate(fruits,start=1):   #enumerate() produces pairs of an index and an item.
    print(index,fruit)
print("------------------------------------------------------------------------")

#Challenge-02
print("------------------------------------------------------------------------")
print("-------------------------- Shopping List -------------------------------")
print("------------------------------------------------------------------------")
shopping_list=["Clothes","Accessories","Furnitures","Flowers","Decoratings"]
for index,item in enumerate(shopping_list,start=1):
    print(index,item)
print("-----------------------------------------------------------------------")

#Challenge-03
print("------------------------------------------------------------------------")
print("--------------------------- Marks Report -------------------------------")
print("------------------------------------------------------------------------")
students=["Anu","Abhi","Bhoomi","Mithu"]
marks=[85,75,65,95]
for index,student in enumerate(students):
    print(index+1,student,marks[index])
#or
print("------------------")
students=["Anu","Abhi","Bhoomi","Mithu"]
marks=[85,75,65,95]
for index,student in enumerate(students,start=1):
    print(index,student,marks[index-1])
print("-----------------------------------------------------------------------")

#Bonus-Challenge
print("------------------------------------------------------------------------")
print("-------------------------- Bonus Challenge -----------------------------")
print("---------------------------- To Do List --------------------------------")
print("------------------------------------------------------------------------")
to_do_list=["Coding","Assignment","Notes","Homework","Live","Class"]
for index,list in enumerate(to_do_list,start=1):
    print(index,list)
task=int(input("Choose the task number in to_do_list:"))
print("The choosen task","--->",to_do_list[task])
print("-----------------------------------------------------------------------")
print("---------------------- End of Day-41 Challenges -----------------------")
print("-----------------------------------------------------------------------")
#End of Program