#The magic door
print("Welcome to the Dungeon!")
door=input("You see two doors.Do you choose 'red'door or the 'blue'door?")
choosen_door=door.lower()
if choosen_door=="red":
    print("You fell into a pit of fire. Game Over.")
elif choosen_door=="blue":
    print("You found the treasure chest! You Win!")
else:
    print("You stood there too long and a ghost got you. Game Over.")