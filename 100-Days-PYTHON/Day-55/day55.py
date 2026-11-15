#Introduction to heapq
#Examples
print("-----------------------------------------------")
print("------------------- Examples ------------------")
print("-----------------------------------------------")
import heapq
numbers=[40,10,30,20,50]
heapq.heapify(numbers) #Convert list to heap and auto sorts in ascending order
print("Heap:",numbers)
heapq.heappush(numbers,5) #Adding new element to heap
print("After adding:",numbers)
smallest=heapq.heappop(numbers) #Removing last element from heap
print("Removed smallest:",smallest)
heapq.nsmallest(3,numbers) #Removing n smallest values from heap
print("Remove 3 smallest elements:",numbers)
heapq.nlargest(3,numbers) #Removing n largest values from heap
print("Remove 3 largest elements:",numbers)
print(numbers[0]) #Giving element from 0th index
print("-----------------------------------------------")

#Challenge-01
print("-----------------------------------------------")
print("------------------- Create a loop -------------")
print("-----------------------------------------------")
digits=[45,10,35,5,25,15]
heapq.heapify(digits)
print("Heap:",digits)
print("-----------------------------------------------")

#Challenge-02
print("-----------------------------------------------")
print("------------ Add elements to heap -------------")
print("-----------------------------------------------")
heapq.heappush(digits,5)
heapq.heappush(digits,15)
print("Added elements to heap:",digits)
print("-----------------------------------------------")

#Challenge-03
print("-----------------------------------------------")
print("------------ Remove the smallest element ------")
print("-----------------------------------------------")
rem=heapq.heappop(digits)
print("Removed smallest element from:",rem)
print("Remaining heap:",digits)
print("-----------------------------------------------")

#Challenge-04
print("-----------------------------------------------")
print("---- Find the largest and smallest elements ---")
print("-----------------------------------------------")
marks=[85,45,95,70,60,90,55]
larg=heapq.nlargest(3,marks)
small=heapq.nsmallest(3,marks)
print("Smallest 3 elements:",small)
print("Largest 3 elements:",larg)
print("-----------------------------------------------")

#Challenge-05
print("-----------------------------------------------")
print("- Mini-Project-Priority based task management -")
print("-----------------------------------------------")
import heapq
tasks=[]
tasks.append("3. Complete Python Assignment")
tasks.append("1. Prepare for exam")
tasks.append("2. Complete project")
print(tasks)
heapq.heapify(tasks)
print(tasks)
high=heapq.heappop(tasks)
print("Removed Highest prior task:",high)
print("Remaining tasks are:",tasks)
print("-----------------------------------------------")
print("--------------- End of Day-55 -----------------")
print("-----------------------------------------------")
#End of Day-55 Challenges