import math
h=int(input("Enter the height of Wall in meters:"))
w=int(input("Enter the width of Wall in meters:"))
total_area=h*w
cans=total_area/5
total_cans=math.ceil(cans)
print(f"You will need to buy {total_cans} cans of paint.")