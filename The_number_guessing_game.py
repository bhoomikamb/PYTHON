import random
secret_number=random.randint(1,50)
guess=0
attempts=0
while guess!=secret_number:
    g=int(input("Enter your guess:"))
    attempts+=1
    if guess>secret_number:
        print("Too high!! Try again.")
    elif guess<secret_number:
        print("Too low!! Try again.")
print(f"Congratulations! You guessed the number in {attempts} tries!.")