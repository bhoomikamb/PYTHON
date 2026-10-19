#regular Expression(re)
#Challenge-01
print("------------------------------------------------------")
print("------------------ Find the numbers ------------------")
print("------------------------------------------------------")
import re
test="I bought 12 pens,3 books and 25 pencils"
result=re.findall(r"\d+",test) #Finds all numbers
print(result)
print("------------------------------------------------------")

#Challenge-02
print("------------------------------------------------------")
print("------------- Find all email address -----------------")
print("------------------------------------------------------")
text="Contact us at bhoomiimb@gmail.com or basavarajumk@gmail.com"
search=re.findall(r"\w+@\w+\.\w+",text) #re.findall() finds all the speacified type present in text
#\d+ ---> takes numbers
#\d ---> single number
#\w+ ---> Words
print(search)
print("------------------------------------------------------")

#Challenge-03
print("------------------------------------------------------")
print("------------ Replace Text using re.sub() -------------")
print("------------------------------------------------------")
msg="Bhoomi scored 95 marks in 3 subjects"
out=re.sub(r"\d","#",msg) #Replacing numbers by #
print(out)
print("-----------------------------------------------------")

#Challenge-04
print("------------------------------------------------------")
print("--------------- Validate phone numbers ---------------")
print("------------------------------------------------------")
phone="9876543210"
pattern=r"\d{10}" #Limiting numbers with 10 digits
if re.fullmatch(pattern,phone): #matching pattern with phone
    print("Valid Number")
else:
    print("Invalid Number")
phone_num="98765"
pattern=r"\d{10}"
if re.fullmatch(pattern,phone_num):
    print("Valid Number")
else:
    print("Invalid Number")
print("------------------------------------------------------")
print("-------------- End of Day-50 Challenges --------------")
print("------------------------------------------------------")
#End of Day-50 Challenges