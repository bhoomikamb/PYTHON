import math
radius=float(input("Enter the radius of Cylinder's base:"))
hght=float(input("Enter the height of Cylinder:"))
volume=(math.pi*(radius**2)*hght)
tsa=(2*math.pi*radius*hght)+(2*math.pi*(radius**2))
total_vol=round(volume,2)
total_tsa=round(tsa,2)
print(f"The Volume of Cylinder is {total_vol}")
print(f"The total surface area of Cylinder is {total_tsa}")