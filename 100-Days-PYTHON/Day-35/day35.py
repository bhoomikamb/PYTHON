#Challenge-01
import sqlite3
conn=sqlite3.connect("100-Days-Python/Day-35/memory")
print("=============================================================================")
print("--------------------------- execute many() ----------------------------------")
print("=============================================================================")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, marks INTEGER)")
students_data=[("Bhoomi",85),
               ("Sachin",95),
               ("Krishna",75),
               ("Dhanush",90),
               ("Anu",88)]
cursor.executemany("INSERT INTO students VALUES(?,?)",students_data)
conn.commit()
print(f"Successfully inserted {cursor.rowcount} students at once")
print("-----------------------------------------------------------------------------")

#Challenge-02
print("=============================================================================")
print("------------------------------ fetch one() ----------------------------------")
print("=============================================================================")
target_name=input("Enter student name to search:")or "Bhoomi"
cursor.execute("SELECT * FROM students WHERE name=?",(target_name,))
student_record=cursor.fetchone()
if student_record:
    print(f"Record found:{student_record}")
else:
    print("No matching found")
print("-----------------------------------------------------------------------------")

#Challenge-03
print("=============================================================================")
print("------------------------------ sqlite3.Row  ---------------------------------")
print("=============================================================================")
conn.row_factory=sqlite3.Row
cursor=conn.cursor()
cursor.execute("SELECT name, marks FROM students WHERE name=?",("Bhoomi",))
row=cursor.fetchone()
if row:
    print(f"Student Name:{row['name']}")
    print(f"Marks:{row['marks']}")
print("-----------------------------------------------------------------------------")

#Challenge-04
print("=============================================================================")
print("------------------------------ rollback() -----------------------------------")
print("=============================================================================")
cursor.execute("CREATE TABLE IF NOT EXISTS bank_account(account_id INT,balance REAL)")
cursor.execute("INSERT INTO bank_account VALUES (101,50000)")
conn.commit()
withdrawal=60000
try:
    cursor.execute("SELECT balance FROM bank_account WHERE account_id=101")
    current_bal=cursor.fetchone()["balance"]
    if withdrawal>current_bal:
        raise ValueError(f"Insufficient funds! Balance is {current_bal},tried to withdraw{withdrawal}")
    cursor.execute("UPDATE bank_account SET balnce=balnce-? WHERE account_id=101",(withdrawal,))
    conn.commit()
    print("Withdrawal Successfully!!")
except ValueError as error:
    print(f"Error:{error}")
    conn.rollback()
    print("Transaction rolled back successfully!")
cursor.execute("SELECT balance FROM bank_account WHERE account_id=101")
print(f"Final Balance:{cursor.fetchone()['balance']}")
print("-----------------------------------------------------------------------------")

#Bonus-Challenge
print("=============================================================================")
print("--------------------------- Robot Sensor database ---------------------------")
print("=============================================================================")
cursor.execute("""CREATE TABLE IF NOT EXISTS sensor_reading(sensor_name TEXT,distance REAL, status TEXT)""")
sensor_data=[("ultrasonic",150,"Safe"),
             ("LiDAR_Front",45.2,"Clear"),
             ("IR_bottom",8.5,"Warning"),
             ("Ultrasonic_Side",12.0,"Safe"),
             ("LiDAR_Rear",30.0,"Clear")]
cursor.executemany("INSERT INTO sensor_reading VALUES (?,?,?)",sensor_data)
conn.commit()
cursor.execute("SELECT sensor_name,distance,status FROM sensor_reading WHERE distance<20")
close_sensors=cursor.fetchall()
for sensor in close_sensors:
    print(f"SEnsor:{sensor['sensor_name']}")
    print(f"Distance:{sensor['distance']}cm")
    print(f"Status:{sensor['status']}")
    print("-"*20)
conn.close
print("-----------------------------------------------------------------------------")
print("--------------------------- End of Day-35 Challenges ------------------------")
print("-----------------------------------------------------------------------------")