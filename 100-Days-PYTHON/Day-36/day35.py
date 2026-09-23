#Challenge-01
print("===========================================================================")
print("----------------------- Student Database ----------------------------------")
print("===========================================================================")
import sqlite3
conn = sqlite3.connect("100-Days-Python/Day-36/students.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL)""")
students_data = [
    ("Aarav", 85),
    ("Bhoomi", 92),
    ("Chetan", 78),
    ("Diya", 95),
    ("Esha", 88)]
with conn:
    cursor.executemany("INSERT INTO students (name, marks) VALUES (?, ?)", students_data)
cursor.execute("SELECT * FROM students")
print("Inserted Students:")
for row in cursor.fetchall():
    print(row)
conn.close()
print("---------------------------------------------------------------------------")

#Challenge-02
print("===========================================================================")
print("-----------------------  Safe Student Update ------------------------------")
print("===========================================================================")
import sqlite3
conn = sqlite3.connect("100-Days-Python/Day-36/students_update.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    name TEXT PRIMARY KEY,
    marks INTEGER)""")
with conn:
    cursor.executemany(
        "INSERT OR REPLACE INTO students VALUES (?, ?)",
        [("Anu", 80), ("Bhoomi", 90), ("Charan", 75)])
target_name = input("Enter student name: ").strip()
try:
    new_marks = int(input("Enter new marks: "))
    with conn:
        cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (new_marks, target_name))
        if cursor.rowcount == 0:
            raise ValueError(f"Student '{target_name}' not found!")
    print(f"✅ Successfully updated {target_name}'s marks to {new_marks}.")
except Exception as e:
    print(f"Transaction failed/rolled back: {e}")
cursor.execute("SELECT * FROM students")
print("\nCurrent DB State:", cursor.fetchall())
conn.close()
print("---------------------------------------------------------------------------")

#Challenge-03
print("===========================================================================")
print("-------------------------- Bank Transfer ----------------------------------")
print("===========================================================================")
import sqlite3
conn = sqlite3.connect("100-Days-Python/Day-36/bank.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL NOT NULL)""")
with conn:
    cursor.executemany("INSERT OR REPLACE INTO accounts VALUES (?, ?, ?)", [
        (101, "Bhoomi", 50000.0),
        (102, "Anu", 30000.0)])
print("--- Before Transfer ---")
cursor.execute("SELECT * FROM accounts")
for acc in cursor.fetchall():
    print(acc)
transfer_amount = 5000.0
try:
    with conn:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (transfer_amount, 101))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (transfer_amount, 102))
    print("\n✅ Transfer successful!")
except Exception as err:
    print(f"\n Transfer failed, transaction rolled back: {err}")
print("\n--- After Transfer ---")
cursor.execute("SELECT * FROM accounts")
for acc in cursor.fetchall():
    print(acc)
conn.close()
print("---------------------------------------------------------------------------")

#Challenge-04
print("===========================================================================")
print("-------------------------- Intentional Error ------------------------------")
print("===========================================================================")
import sqlite3
conn = sqlite3.connect("test_rollback.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS items")
cursor.execute("""CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    item_name TEXT UNIQUE)""")
conn.commit()
print("Initial item count:", cursor.execute("SELECT COUNT(*) FROM items").fetchone()[0])
try:
    with conn:
        cursor.execute("INSERT INTO items VALUES (1, 'Laptop')")
        print("Logged: Successfully executed Operation 1 (Laptop)")
        cursor.execute("INSERT INTO items VALUES (1, 'Smartphone')") 
except sqlite3.IntegrityError as e:
    print(f"\n Caught Expected Exception: {e}")
cursor.execute("SELECT COUNT(*) FROM items")
count = cursor.fetchone()[0]
print(f"Final item count in database: {count}")
if count == 0:
    print(" Success! Operation 1 was automatically rolled back because Operation 2 failed.")
conn.close()
print("---------------------------------------------------------------------------")

#Bonus-Challenge
print("===========================================================================")
print("-------------------------- Bonus Challenge --------------------------------")
print("-------------------------- Robot Transaction System -----------------------")
print("===========================================================================")
import sqlite3
def update_robot(connection: sqlite3.Connection, name: str, new_battery: int, new_status: str):
    """
    Safely updates battery and status in a single atomic transaction.
    """
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE robots SET battery = ? WHERE robot_name = ?", 
                (new_battery, name))
            cursor.execute(
                "UPDATE robots SET status = ? WHERE robot_name = ?", 
                (new_status, name))
            if cursor.rowcount == 0:
                raise ValueError(f"Robot '{name}' does not exist.")
        print(f"[SUCCESS] Updated {name}: Battery -> {new_battery}%, Status -> '{new_status}'")
    except Exception as error:
        print(f"[ERROR] Could not update {name}. Details: {error}")
conn = sqlite3.connect("robots_system.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS robots (
    robot_name TEXT PRIMARY KEY,
    battery INTEGER,
    status TEXT)""")
with conn:
    cursor.executemany("INSERT OR REPLACE INTO robots VALUES (?, ?, ?)", [
        ("Robo-Alpha", 100, "Idle"),
        ("Robo-Beta", 45, "Working"),
        ("Robo-Gamma", 15, "Charging")])
update_robot(conn, "Robo-Beta", 80, "Standby")
cursor.execute("SELECT * FROM robots")
print("\nRobots Database State:")
for row in cursor.fetchall():
    print(row)
conn.close()
print("---------------------------------------------------------------------------")
print("------------------------ End of Day-36 Challenges -------------------------")
print("---------------------------------------------------------------------------")