#Challenge-01
print("-----------------------------------------------------------------------")
print("-------------------------- Count Students -----------------------------")
print("-----------------------------------------------------------------------")
import sqlite3
connection=sqlite3.connect("100-Days-Python/Day-39/students.db")
cursor=connection.cursor()
cursor.execute("SELECT COUNT(*) FROM students")
total_students=cursor.fetchone()[0]
print("Total number of students:",total_students)
print("-----------------------------------------------------------------------")

#Challenge-02
print("-----------------------------------------------------------------------")
print("---------------------- Calculate Average Marks ------------------------")
print("-----------------------------------------------------------------------")
cursor.execute("SELECT AVG(marks) FROM students")
average_marks=cursor.fetchone()[0]
print("Average marks:",average_marks)
print("-----------------------------------------------------------------------")

#Challenge-03
print("-----------------------------------------------------------------------")
print("------------------- Find Largest & Lowest Marks -----------------------")
print("-----------------------------------------------------------------------")
cursor.execute("SELECT MAX(marks) FROM students")
highest_marks=cursor.fetchone()[0]
cursor.execute("SELECT MIN(marks) FROM students")
lowest_marks=cursor.fetchone()[0]
print("Highest marks:",highest_marks)
print("Lowest marks:",lowest_marks)
print("-----------------------------------------------------------------------")

#Challenge-04
print("-----------------------------------------------------------------------")
print("---------------------- Students Statistics Report ---------------------")
print("-----------------------------------------------------------------------")
cursor.execute("""SELECT 
COUNT(*) AS total_students,
SUM(marks) AS total_marks,
AVG(marks) AS average_marks,
MAX(marks) AS highest_marks,
MIN(marks) AS lowest_marks
FROM students""")
result=cursor.fetchone()
print("------------------- Student Statistics Report -------------------------")
print("Total students:",result[0])
print("Total marks:",result[1])
print("Average marks:",result[2])
print("Highest marks:",result[3])
print("Lowest marks:",result[4])
print("-----------------------------------------------------------------------")

#Bonus-Challenge
print("-----------------------------------------------------------------------")
print("----------------------------- Bonus Challenge -------------------------")
print("----------------------------- Marks Analysis  -------------------------")
print("-----------------------------------------------------------------------")
minimum_marks=int(input("Enter minimum marks:"))
cursor.execute("SELECT COUNT(*) FROM students WHERE marks>-?",(minimum_marks,))
count=cursor.fetchone()[0]
print("Number of students scoring at least",minimum_marks,"marks:",count)
connection.close()
print("----------------------------------------------------------------------")
print("------------------ End of Day-40 Challenges --------------------------")
print("----------------------------------------------------------------------")