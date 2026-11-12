#Day-56 of 100 Days Challenge
#Binary search in Python
#Examples
print("------------------------------------------")
print("---------------- Examples ----------------")
print("------------------------------------------")
import bisect
numbers=[10,20,30,40,50]
bisect.insort(numbers,25) #inserts a value while maintaining sorted order 
print(numbers)
position=bisect.bisect_left(numbers,20) #Finds the insertion position before existing equal values
print(position)
pos=bisect.bisect_right(numbers,20) #Finds the insertion position after existing equal values
print(pos)
print("------------------------------------------")

#Challenge-01
print("------------------------------------------")
print("------ Find the insertion position -------")
print("------------------------------------------")
import bisect
numbers=[10,20,30,40,50]
left=bisect.bisect_left(numbers,25)
print("Insert position to left:",left)
print("------------------------------------------")

#Challenge-02
print("------------------------------------------")
print("------------- Insert an element ----------")
print("------------------------------------------")
digits=[5,15,25,35,45]
bisect.insort(digits,20)
print(digits)
print("------------------------------------------")

#Challenge-03
print("------------------------------------------")
print("--- Find positions of duplicate values ---")
print("------------------------------------------")
numbers=[10,20,20,20,30,40]
left=bisect.bisect_left(numbers,20)
right=bisect.bisect_right(numbers,20)
print("Left Position:",left)
print("Right Position:",right)
print("------------------------------------------")

#Challenge-04
print("------------------------------------------")
print("---------- Insert multiple values --------")
print("------------------------------------------")
numbers=[10,30,50,70]
new_values=[20,40,60]
#numbers.append(new_values)
for n in new_values:
    bisect.insort(numbers,n)
#new=numbers+new_values
print("New list:",numbers)
print("------------------------------------------")

#Challenge-05
print("------------------------------------------")
print("--- Mini-Project Student marks raking ----")
print("------------------------------------------")
marks=[45,55,65,75,85]
bisect.insort(marks,70)
bisect.insort(marks,90)
posit=bisect.bisect_left(marks,80)
print("Updated marks:",marks)
print("Position of 80:",posit)
print("------------------------------------------")
print("-------------- End of day-56 -------------")
print("------------------------------------------")
#Day-56 Challenges ends