bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give? "))
splitter=int(input("How many people are splitting the bill? "))
tip_amount=bill*(tip/100)
new_bill=tip_amount/5
rounded_bill=round(new_bill,2)
print(f"Each person should pay {rounded_bill}")