row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

position = input("Where do you want to hide the treasure?:").upper()
column=position[0]
if column=="A":
    column_index=0
elif column=="B":
    column_index=1
elif column=="C":
    column_index=2
row_index=int(position[1])-1
map[row_index][column_index]="X"
print(row1)
print(row2)
print(row3)