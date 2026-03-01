import math
radius=float(input("enter the radius of circle:"))
circum=2*math.pi*radius
area=math.pi*(radius**2)
final_circum=round(circum,2)
final_area=round(area,2)
print(f"The circumference and area of circle is {final_circum} and {final_area} respectively.")
