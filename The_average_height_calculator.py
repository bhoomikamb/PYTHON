student_heights=[180,124,165,173,189,169,146]
total_height=0
for height in student_heights:
    total_height+=height
avg_height=total_height/len(student_heights)
average_height=round(avg_height,2)
print("The average height of students is",average_height)