#Challenge-01
print("------------------------------------------------------------------")
print("------------------- Create an Index ------------------------------")
print("------------------------------------------------------------------")
import sqlite3
connection=sqlite3.connect("100-Days-Python/Day-39/students.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY,name TEXT,marks INTEGER)""")
students=[("Bhoomika",562),
          ("Sachin",480),
          ("Mithun",520),
          ("Abhii",590),
          ("Suma",450)]
cursor.executemany("INSERT INTO students(name,marks) VALUES(?,?)",students)
cursor.execute("""CREATE INDEX IF NOT EXISTS idx_student_name 
ON students(name)""")
connection.commit()
print("Index created successfully")
print("-----------------------------------------------------------------")

#Challenge-02
print("------------------------------------------------------------------")
print("------------------- Check the Index ------------------------------")
print("------------------------------------------------------------------")
cursor.execute("PRAGMA index_list(students)")
indexes=cursor.fetchall()
print("Indexes in student table")
for index in indexes:
    print(index)
print("-----------------------------------------------------------------")

#Challenge-03
print("------------------------------------------------------------------")
print("----------------- Search using Index Column ----------------------")
print("------------------------------------------------------------------")
connection.row_factory=sqlite3.Row
cursor=connection.cursor()
name=input("Enter name of the student:")
cursor.execute("SELECT*FROM students WHERE name=?",(name,))
student=cursor.fetchone()
if student:
    print("Student Found")
    print("Name:",student["name"])
    print("Marks:",student["marks"])
else:
    print("Student not found")
print("-----------------------------------------------------------------")

#Challenge-04
print("------------------------------------------------------------------")
print("----------------- Search using Index Column ----------------------")
print("------------------------------------------------------------------")
cursor.execute("DROP INDEX IF EXISTS idx_student_name")
connection.commit()
print("Index deleted successfully")
cursor.execute("PRAGMA index_list(students)")
indexes=cursor.fetchall()
print("Indexes in student table:")
for index in indexes:
    print(index)
print("-----------------------------------------------------------------")

#Bonus-Challenge
print("------------------------------------------------------------------")
print("-------------------------- Bonus Challenge -----------------------")
print("----------------------- Create Multiple Indexes ------------------")
print("------------------------------------------------------------------")
cursor.execute("""CREATE INDEX IF NOT EXISTS idx_student_name
ON students(name)""")
cursor.execute("""CREATE INDEX IF NOT EXISTS idx_student_marks
ON students(marks)""")
connection.commit()
cursor.execute("PRAGMA index_list(students)")
indexes=cursor.fetchall()
print("Indexes in student table:")
for index in indexes:
    print(index)
cursor.execute("DROP INDEX IF EXISTS idx_student_name")
cursor.execute("DROP INDEX IF EXISTS idx_student_marks")
connection.commit()
print("Both indexes deleted successfully!")
connection.close()
print("-----------------------------------------------------------------")
print("------------------ End of Day-39 Challenges ---------------------")
print("-----------------------------------------------------------------")