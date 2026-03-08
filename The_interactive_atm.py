balance=1000
while(1):
    user_input=input("Type 'w' to withdraw,'d' to deposit and 'q' to quit").lower()
    if user_input=="q":
        print("Goodbyee!!")
    elif user_input=="d":
        amount=int(input("Enter an amount:"))
        balance+=amount
        print("Current balance",balance)
    elif user_input=="w":
        amount=int(input("Enter an amount:"))
        if amount>balance:
            print("Insufficient funds.")
            continue
        balance-=amount
        print("New balance",balance)
    else:
        print("INVALID!!")

