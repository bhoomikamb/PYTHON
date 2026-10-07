#Challenge-01
print("-------------------------------------------------------------")
print("-------------------- CRUD Functions -------------------------")
print("-------------------------------------------------------------")
from os import read
import sqlite3
connection=sqlite3.connect("100-Days-PYTHON/Day-38/students.db")
cursor=connection.cursor()
cursor.execute("""DROP TABLE IF EXISTS students""")
cursor.execute("""CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY,name TEXT,marks INTEGER)""")
def add_student():
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    with connection:
        cursor.execute("INSERT INTO students(name,marks) VALUES(?,?)",(name,marks))
def view_student():
    cursor.execute("SELECT*FROM students")
    students=cursor.fetchall()
    for student in students:
        print(student)
def update_student():
    name=input("Enter student name:")
    marks=int(input("Enter new marks:"))
    with connection:
        cursor.execute("UPDATE students SET marks=? WHERE name=?",(marks,name))
def delete_student():
    name=input("Enter student name:")
    with connection:
        cursor.execute("DELETE FROM students WHERE name=?",(name,))
add_student()
view_student()
update_student()
delete_student()
print("-------------------------------------------------------------")

#Challenge-02
print("-------------------------------------------------------------")
print("----------------------- Menu System -------------------------")
print("-------------------------------------------------------------")
target_name=input("Enter student name:")
cursor.execute("SELECT*FROM students WHERE name=?",(target_name,))
student=cursor.fetchone()
if student:
    print("Student Found")
    print("Name:",student["name"])
    print("Marks:",student["marks"])
else:
    print("Student not found")
print("-------------------------------------------------------------")

#Challenge-03
print("-------------------------------------------------------------")
print("----------------------- Search Student ----------------------")
print("-------------------------------------------------------------")
connection.row_factory=sqlite3.Row
cursor=connection.cursor()
name=input("Enter student name:")
cursor.execute("SELECT name,marks FROM students WHERE name=?",(name,))
student=cursor.fetchone()
if student:
    print("Student Found:")
    print("Name:",student["name"])
    print("Marks:",student)
else:
    print("Student not found")
connection.close()
print("-------------------------------------------------------------")

#Challenge-04
print("-------------------------------------------------------------")
print("--------------------- Transaction Rollback ------------------")
print("-------------------------------------------------------------")
conn=sqlite3.connect("100-Days-Python/Day-38/bank.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS bank_account(account_id INTEGER PRIMARY KEY,balance REAL)""")
cursor.execute("INSERT OR REPLACE INTO bank_account VALUES(?,?)",(101,50000))
conn.commit()
withdrawal=60000
try:
    cursor.execute("SELECT balance FROM bank_account WHERE account_id=?",(101,))
    current_balance=cursor.fetchone()[0]
    if withdrawal>current_balance:
        raise ValueError("Insufficient balance")
    cursor.execute("""UPDATE bank_account
    SET balance=balance-?
    WHERE account_id=?""",(withdrawal,101))
    conn.commit()
except ValueError as error:
    print("Transaction failed:",error)
    conn.rollback()
cursor.execute("SELECT balance FROM bank_account WHERE account_id=?",(101,))
final_balance=cursor.fetchone()[0]
print("Final Balance:",final_balance)
conn.close()

#Bonus Challenge
print("-------------------------------------------------------------")
print("------------------ Bonus Challenge --------------------------")
print("--------------------- Transaction Rollback ------------------")
print("-------------------------------------------------------------")
conn=sqlite3.connect("100-Days-Python/Day-38/sensor_data.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS sensor_readings(sensor_name TEXT,distance REAL, status TEXT)""")
sensor_data=[("Front Sensor",15,"Safe"),
             ("Left Sensor",25,"Safe"),
             ("Right Sensor",-17,"Invalid"),
             ("Back Sesnor",30,"Safe")]
try:
    cursor.executemany("INSERT INTO sensor_readings VALUES(?,?,?)",sensor_data)
    for reading in sensor_data:
        if reading[1]<0:
            raise ValueError("Invalid sensor distance")
    conn.commit()
    print("All sensor readings saved successfully.")
except ValueError as error:
    print("Transaction failed:",error)
    conn.rollback()
cursor.execute("SELECT*FROM sensor_readings")
readings=cursor.fetchall()
for reading in readings:
    print(reading)
conn.close()
print("-------------------------------------------------------------")
print("------------------ End of Day-38 Challenges -----------------")
print("-------------------------------------------------------------")