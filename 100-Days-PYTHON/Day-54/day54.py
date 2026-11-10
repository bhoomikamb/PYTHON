#Introduction double-ended -Queue
#Example
print("--------------------------------------------------")
print("-------------------- Example ---------------------")
print("--------------------------------------------------")
from collections import deque
items=deque([1,2,3,4])
items.rotate(3) #The number is iterable to add elements from rightmost to first index
print("Rotated by 3 times:",items)
print("--------------------------------------------------")

#Challenge-01
print("--------------------------------------------------")
print("----------- Add elements at both ends ------------")
print("--------------------------------------------------")
numbers=deque([20,30,40])
numbers.appendleft(10) #Adds elements to left
numbers.append(50) #Adds elements to right
print(numbers)
print("--------------------------------------------------")

#Challenge-02
print("--------------------------------------------------")
print("------------------ Remove elements ---------------")
print("--------------------------------------------------")
fruits=deque(["apple","banana","orange","mango"])
fruits.pop() #Removes the element from right
fruits.popleft() #Removes the element from left
print(fruits)
print("--------------------------------------------------")

#Challenge-03
print("--------------------------------------------------")
print("------------------ Rotate a deque ----------------")
print("--------------------------------------------------")
numbers=deque([1,2,3,4,5])
numbers.rotate(2) #Rotate deque by 2 times
print(numbers)
print("--------------------------------------------------")

#Challenge-04
print("--------------------------------------------------")
print("------------------- Extend a deque ---------------")
print("--------------------------------------------------")
numbers=deque([10,20])
#numbers.append(30)
#numbers.append(40)
#numbers.append(50)
#or
numbers.extend([30,40,50]) #Extends the deque by adding elements from right
numbers.extendleft([5,0]) #Extends the deque by adding elements from left
#or
#numbers.appendleft(0)
#numbers.appendleft(5)
print(numbers)
print("--------------------------------------------------")

#Challenge-05
print("--------------------------------------------------")
print("------ Mini-Project - Customer service queue -----")
print("--------------------------------------------------")
customers=deque(["Customer 1","Customer 2","Customer 3"])
customers.append("Customer 4")
customers.appendleft("Emergency Customer")
customers.popleft()
print(customers)
print("--------------------------------------------------")
print("-------------- End of Day-54 Challenges ----------")
print("--------------------------------------------------")
#End of Day-54 Challenges