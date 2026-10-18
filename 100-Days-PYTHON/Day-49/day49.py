#counter()
#Challenge-01
print("------------------------------------------------------------")
print("---------------- Count the fruits --------------------------")
print("------------------------------------------------------------")
from collections import Counter
fruits=["Apple","Banana","Apple","Orange","Banana","Apple"]
result=Counter(fruits)
print(result) #prints how many times fruits appear in a list
print("------------------------------------------------------------")

#Challenge-02
print("------------------------------------------------------------")
print("---------------- Character frequency -----------------------")
print("------------------------------------------------------------")
word="programming"
print("Character Frequency:",Counter(word)) #Counter the appearence of each character in a word
print("------------------------------------------------------------")

#Challenge-03
print("------------------------------------------------------------")
print("---------------- Most Common items -------------------------")
print("------------------------------------------------------------")
numbers=[10,20,10,30,20,10,40,20,20]
outcome=Counter(numbers)
print("Most common items:",outcome.most_common(2)) #returns most common frequent appearence in given list upto specified numbers
print("-----------------------------------------------------------")

#Challenge-04
print("------------------------------------------------------------")
print("---------------- Find repaeted Characters ------------------")
print("------------------------------------------------------------")
place="mississippi"
repeated=Counter(place)
print("All characters & it's count",repeated.items()) #acessing each character and its count
count=repeated.most_common(3) #most 3 frequently repeated
print("Most 3 frequently repeated characters:",count)
for char,count in repeated.items(): #.items gives all the character and its count as dictionary
    if count>1:
        print(f"The '{char}' is repeated {count} times")
    else:
        print(f"The character '{char}' is repeated only {count} time")
print("----------------------------------------------------------")

#Challenge-05
print("------------------------------------------------------------")
print("------------------------ Word Frequency --------------------")
print("------------------------------------------------------------")
sentence="Python is fun and Python is Powerful"
sen=sentence.split() #Used to split the string to elements of list wrt space
result=Counter(sen)
print(result)
print("------------------------------------------------------------")
print("---------------- End of Day-49 Challenges ------------------")
print("------------------------------------------------------------")
#End of Day-49 Challenges