#The Treasure Island
player_health=100
print("Welcome to Treasure Island!")
name=input("Enter your name:")
print(f"Welcome,{name}.Your health is {player_health}.")
print("Choice 1")
a=input("You reached Crosslands.'Left' or 'Right'?")
aa=a.lower()
if aa=="right":
    print("You have triggered a trap!!!!")
    player_health-=50
    print(f"Your Health is {player_health}.")
elif aa=="left":
    print("You are safe!!")
else:
    print("INVALID!!")
print("Choice 2")
b=input("You reach a lake.'Swim' across or 'wait' for a boat.")
bb=b.lower()
if bb=="swim":
    print("You are attacked by a crocodile")
    player_health-=100
    print(f"Your health is {player_health}.")
elif bb=="wait":
    print("A boat arrives!.You are safe.")
else:
    print("INVALID!!")
if player_health<=0:
    print("YOU DIED!! GAME OVER!!!")
else:
    print("Choice 3")
    c=input("You arrive at the castle.Choose one door 'red','blue' or 'yellow'.")
    cc=c.lower()
    if cc=="red":
        print("Burned by fire.GAME OVER!!")
    elif cc=="blue":
        print("Eaten by beasts.GAME OVER!!")
    elif cc=="yellow":
        print("You found the treasure!. YOU WIN!!!!")