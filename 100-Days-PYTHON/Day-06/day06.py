#=====================================================================
#PERSONAL INFORMATION
#=====================================================================
name=input("Enter your name:")
college=input("Enter your College:")
branch=input("Enter your Branch:")
text="myself Jaan"
print(name[:6])
print(len(college))
print(name.upper())
print(branch.title())
print(name.capitalize())
text=text.replace("Jaan","Mithuu")
print(text.find("Mithuu"))
print(text.find("Sacchii"))
words=text.split()
print(words)
words=["I","Love","to","be","alone"]
wish=" ".join(words)
print(wish)

#==================================================================
#TEXT ANALYZER
#==================================================================
sentence=input("Enter a statement:")
print("Number of characters:",len(sentence))
print("Number of words:",len(sentence.split()))
print(sentence.count("a"))
if "love" in sentence:
    print("Love exists!!")
else:
    print("Not exists!!")
print(sentence.upper())
print(sentence.lower())

#================================================================
#USERNAME GENERATOR
#================================================================
first_name=input("Enter your First Name:")
last_name=input("Enter your Last Name:")
birth_year=int(input("Enter your birth year:"))
username=(first_name[:4]+last_name[0:]+ str(birth_year))
print(username)

#================================================================
#PASSWORD VALIDATOR
password=input("Enter your password:")
if len(password)>=8:
    print("Minimum length:OK")
else:
    print("Password should contain at least 8 characters")
has_upper=False
has_lower=False
has_digit=False
for char in password:
    if char.isupper():
        has_upper=True
    if char.islower():
        has_lower=True
    if char.isdigit():
        has_digit=True
if has_upper and has_lower and has_digit and len(password) >=8:
    print("Strong Password")
else:
    print("Password does not meet all requirements.")
print("End of Program!!")