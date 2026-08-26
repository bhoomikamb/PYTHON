#===================================================================
#---------------------CREATE & WRITE A FILE-------------------------
#===================================================================
import os
print(os.getcwd())
file=open("100-Days-Python/Day-08/intro.txt","r")
content=file.read()
print(content)
file.close()

#===================================================================
#----------------------STUDENT NOTES--------------------------------
#===================================================================
file=open("100-Days-Python/Day-08/student_note.txt","r")
contents=file.read()
print(contents)
file.close()

#==================================================================
#-------------------------APPEND DATA------------------------------
#==================================================================
file=open("100-Days-Python/Day-08/student_notes.txt","a")
file.write("Kandamma = 900 \n")
file.close()
file=open("100-Days-Python/Day-08/student_notes.txt","r")
contents= file.read()
print(contents)
file.close()

#==================================================================
#--------------------------BONUS CHALLENGE-------------------------
#------------------------SIMPLE DIARY------------------------------
#==================================================================
with open("100-Days-Python/Day-08/entries.txt","a") as  file:
    file.write("I enjoyed learning Python.\n  Day by day I can remember what i have learnt during my coarse and learning new things \n")
with open("100-Days-Python/Day-08/entries.txt","r") as file:
    all_entries=file.read()
    print(all_entries)
print("------End of Day-08 Challenges-------")