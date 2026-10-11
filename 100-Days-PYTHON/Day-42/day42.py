#Python zip()
#Challenge-01
print("---------------------------------------------------------------")
print("-------------------- Match Names and Marks --------------------")
print("---------------------------------------------------------------")
names=["Anu","Bhoomi","Cherry","David","Sachin"]
marks=[95,85,75,65,55]
for name,mark in zip(names,marks):
    print(name,":",mark)
print("---------------------------------------------------------------")

#Challenge-02
print("---------------------------------------------------------------")
print("------------------------ Shopping Bill ------------------------")
print("---------------------------------------------------------------")
product_names=["Clothes","Laptop","Mobile","Furnitures","Sofa"]
product_price=[2000,52000,15000,150000,30000]
for name,price in zip(product_names,product_price):
    print(name,"---->","$",price)
print("---------------------------------------------------------------")

#Challenge-03
print("---------------------------------------------------------------")
print("-------------------- Calculate Total Bill ---------------------")
print("---------------------------------------------------------------")
products=["Nail Polish","RC car","Doll","Trousers","Mehandi"]
quantity=[2,1,3,5,2]
prices=[40,1500,400,500,20]
for product,quantity,price in zip(products,quantity,prices):
    print(product,":","$",quantity*price)
print("--------------------------------------------------------------")

#Challenge-04
print("---------------------------------------------------------------")
print("-------------------- Student Result Report --------------------")
print("---------------------------------------------------------------")
names=["Sachin","Bhoomi","Mithu"]
marks=[85,95,75]
subjects=["Mathematics","DSP","Python"]
for name,marks,subject in zip(names,marks,subjects):
    print(name,":",subject,"-->",mark)
print("--------------------------------------------------------------")

#Bonus-Challenge
print("---------------------------------------------------------------")
print("---------------------- Bonus Challenge ------------------------")
print("------------- Combine Two Lists into a Dictionary -------------")
print("---------------------------------------------------------------")
names=["Anu","Bhoomi","Charith","David","Eve"]
marks=[85,25,61,35,45]
student_marks=dict(zip(names,marks)) #converting zip elements to dictionary
print("Student marks:",student_marks)
for name,mark in student_marks.items():
    print(name,":",mark)
print("---------------------------------------------------------------")
print("-------------------- End of Day-42 Challenges -----------------")
print("---------------------------------------------------------------")
#End of program