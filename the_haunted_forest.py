#The haunted forest
print("Welcome the player to the Haunted Forest!!")
a=input("Do you want to go 'left' or 'right'")
aa=a.lower()
if aa=="right":
    print("Game Over,You fell in a river!")
elif aa=="left":
    b=input("You see a glowing mushroom.Do you 'eat; it or 'ignore it'?")
    bb=b.lower()
    if bb=="eat":
        print("It was poisonous.Game Over")
    if bb=="ignore":
        print("You walked past it and found the exit! You win!")
    else:
        print("You must select one before moving ahead!!")
else:
    print("You have choosen invalid direction.")

