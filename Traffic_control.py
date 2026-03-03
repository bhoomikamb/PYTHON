signal=input("Enter a colour of light in traffic signal:")
if (signal.upper()=="RED"):
    print("Indicates vehicles to 'STOP'.")
elif (signal.upper()=="GREEN"):
    print("Indicates vehicles to 'MOVE'.")
elif (signal.upper()=="ORANGE"):
    print("Indicates vehicles to 'GET READY'.")
else:
    print("INVALID input")
print("End of the program!!")
