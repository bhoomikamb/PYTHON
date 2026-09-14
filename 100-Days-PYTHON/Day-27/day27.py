print("==============================================================================")
print("------------------------ Number Comparison -----------------------------------")
print("==============================================================================")
from functools import cmp_to_key
numbers=[10,3,7,1,8]
def compare(a,b):
    return a-b
sorted_num=sorted(numbers,key=cmp_to_key(compare))
print("Sorted numbers in ascending order:",sorted_num)
print("------------------------------------------------------------------------------")

print("==============================================================================")
print("------------------------ Reverse Sorting -------------------------------------")
print("==============================================================================")
numbers=[10,8,7,3,1]
def compare(a,b):
    return b-a
sort=sorted(numbers,key=cmp_to_key(compare))
print("Sorted numbers in descending order:",sort)
print("------------------------------------------------------------------------------")

print("==============================================================================")
print("------------------------ Sort Students by Marks ------------------------------")
print("==============================================================================")
students=[{"name":"A","marks":75},
          {"name":"B","marks":92},
          {"name":"C","marks":68},
          {"name":"D","marks":85}]
def compare(student1,student2):
    return student2["marks"]-student1["marks"]
sorted_marks=sorted(students,key=cmp_to_key(compare))
for student in sorted_marks:
    print(student["name"],"->",student["marks"])
print("Sorted Student marks from highest to lowest:",sorted_marks)
print("------------------------------------------------------------------------------")

print("==============================================================================")
print("-------------------------- Robot Speed Ranking -------------------------------")
print("==============================================================================")
robots=[{"name":"LineBot","speed":80},
        {"name":"MazeBot","speed":60},
        {"name":"FollowBot","speed":100},
        {"name":"ObstacleBot","speed":120}]
def compare(bot1,bot2):
    return bot2["speed"]-bot1["speed"]
top_speed=sorted(robots,key=cmp_to_key(compare))
for bot in top_speed:
    print(bot["name"],"->",bot["speed"])
print("Top speed in Ascending order among the robots",top_speed)
print("------------------------------------------------------------------------------")
print("------------------------- End of Day-27 Challenge ----------------------------")
print("------------------------------------------------------------------------------")