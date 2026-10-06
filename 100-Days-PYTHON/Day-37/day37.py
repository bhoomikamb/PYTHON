print("------------------------------------------------------------------")
print("---------------------- Create Related Tables ---------------------")
print("------------------------------------------------------------------")
import sqlite3
connection=sqlite3.connect("100-Days-Python/Day-37/students.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY,name TEXT)""")
cursor.execute("INSERT INTO students VALUES(?,?)",(1,"Bhoomi"))
cursor.execute("INSERT INTO students VALUES(?,?)",(2,"Anu"))
cursor.execute("INSERT INTO students VALUES(?,?)",(3,"Chethan"))
cursor.execute("INSERT INTO students VALUES(?,?)",(4,"Diya"))
conn=sqlite3.connect("100-Days-Python/Day-37/marks.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS marks(mark_id INTEGER PRIMARY KEY,student_id INTEGER,subject TEXT,marks INTEGER)""")
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(1,1,"Python",85))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(2,2,"Python",95))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(3,3,"Python",75))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(4,4,"Python",65))
connection.commit()
connection.close()
print("------------------------------------------------------------------")

print("------------------------------------------------------------------")
print("---------------------- Student Marks JOIN ------------------------")
print("------------------------------------------------------------------")
import sqlite3
connect=sqlite3.connect("100-Days-Python/Day-37/student_marks.db")
cursor=connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY,name TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS marks(mark_id INTEGER PRIMARY KEY,
student_id INTEGER,
 subject TEXT, 
 marks INTEGER)""")
cursor.execute("INSERT INTO students VALUES(?,?)",(1,"Bhoomi"))
cursor.execute("INSERT INTO students VALUES(?,?)",(2,"Anu"))
cursor.execute("INSERT INTO students VALUES(?,?)",(3,"Chethan"))
cursor.execute("INSERT INTO students VALUES(?,?)",(4,"Diya"))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(1,1,"Python",85))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(2,2,"Python",95))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(3,3,"Python",75))
cursor.execute("INSERT INTO marks VALUES(?,?,?,?)",(4,4,"Python",65))
cursor.execute("""SELECT students.name,marks.subject,marks.marks 
FROM students 
INNER JOIN marks 
ON students.student_id=marks.student_id""")
connect.commit()
print("------------------------------------------------------------------")

print("------------------------------------------------------------------")
print("---------------------- Search Student Marks ----------------------")
print("------------------------------------------------------------------")
name=input("Enter Student name:")
cursor.execute("""SELECT students.name,marks.subject,marks.marks 
FROM students 
INNER JOIN marks 
ON students.student_id=marks.student_id
WHERE students.name=?""",("Bhoomi",))
results=cursor.fetchall()
for result in results:
    print(result)
connect.commit()
print("------------------------------------------------------------------")

print("------------------------------------------------------------------")
print("-------------------------- Average Marks -------------------------")
print("------------------------------------------------------------------")
cursor.execute("""SELECT subject,AVG(marks)
FROM marks
GROUP BY subject""")
average_marks=cursor.fetchall()
for result in average_marks:
    print(result)
connect.commit()
connect.close()
print("------------------------------------------------------------------")


print("------------------------------------------------------------------")
print("-------------------------- Bonus Challenge -----------------------")
print("------------------------- Three-Table JOIN -----------------------")
print("------------------------------------------------------------------")
import sqlite3
conn = sqlite3.connect("100-Days-Python/Day-37/student_marks.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS marks")
cursor.execute("DROP TABLE IF EXISTS subjects")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
CREATE TABLE students(
    student_id INTEGER PRIMARY KEY,
    name TEXT
)
""")
cursor.execute("""
CREATE TABLE subjects(
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT
)
""")
cursor.execute("""
CREATE TABLE marks(
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER,

    FOREIGN KEY(student_id)
        REFERENCES students(student_id),

    FOREIGN KEY(subject_id)
        REFERENCES subjects(subject_id)
)
""")
students_data = [
    (1, "Bhoomi"),
    (2, "Anu"),
    (3, "Chethan"),
    (4, "Diya")
]
cursor.executemany(
    "INSERT INTO students VALUES(?, ?)",
    students_data
)
subjects_data = [
    (101, "Python"),
    (102, "SQL"),
    (103, "Electronics")
]
cursor.executemany(
    "INSERT INTO subjects VALUES(?, ?)",
    subjects_data
)
marks_data = [
    (1, 101, 85),   # Bhoomi - Python
    (1, 102, 90),   # Bhoomi - SQL
    (2, 101, 95),   # Anu - Python
    (3, 103, 78)    # Chethan - Electronics
]
cursor.executemany(
    "INSERT INTO marks VALUES(?, ?, ?)",
    marks_data
)
conn.commit()
cursor.execute("""
SELECT
    students.name,
    subjects.subject_name,
    marks.marks
FROM students
INNER JOIN marks
    ON students.student_id = marks.student_id
INNER JOIN subjects
    ON marks.subject_id = subjects.subject_id
""")
results = cursor.fetchall()
for result in results:
    print(f"{result[0]} → {result[1]} → {result[2]}")
conn.close()