import random
names=input("Enter everybody's names,separated by a comma:")
names_lists=names.split(",")
length=len(names_lists)
random_index=random.randint(0,length-1)
loser=names_lists[random_index]
print(loser,"is going to buy the meal today!")