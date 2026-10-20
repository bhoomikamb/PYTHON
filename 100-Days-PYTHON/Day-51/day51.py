#defaultdict
#Challenge-01
print("---------------------------------------------------------------------")
print("----------------------- Count fruits --------------------------------")
print("---------------------------------------------------------------------")
from collections import defaultdict
fruits=["Apple","Banana","Apple","Orange","Banana","Apple"]
counts=defaultdict(int)
for fruit in fruits:
    counts[fruit]+=1
print(dict(counts))
print("---------------------------------------------------------------------")

#Challenge-02
print("---------------------------------------------------------------------")
print("-------------------- Group Students by branch -----------------------")
print("---------------------------------------------------------------------")
students=[("Bhoomi","ECE"),("Anu","CSE"),
          ("Sachin","ECE"),("Dhanush","CSE"),
          ("Kiran","EEE")]
branch_students=defaultdict(list)
for name,branch in students:
    branch_students[branch].append(name)
print(dict(branch_students))
print("--------------------------------------------------------------------")

#Challenge-03
print("---------------------------------------------------------------------")
print("---------------- Group Numbers by Even and Odd ----------------------")
print("---------------------------------------------------------------------")
numbers=[10,15,22,33,40,51,64,77]
groups=defaultdict(list)
for num in numbers:
    if num%2==0:
        groups["Even"].append(num)
    else:
        groups["Odd"].append(num)
print(dict(groups))
print("--------------------------------------------------------------------")

#Challenge-04
print("---------------------------------------------------------------------")
print("---------------- Group Words by their First Letter ------------------")
print("---------------------------------------------------------------------")
words=["Apple","Ant","Banana","Ball","Cat","Car","Apricot"]
groups=defaultdict(list)
for word in words:
    first_letter=word[0]
    groups[first_letter].append(word)
print(dict(groups))
print("---------------------------------------------------------------------")
print("--------------------- End of Day-51 Challenges ----------------------")
print("---------------------------------------------------------------------")
#End of Day-51 Challenges