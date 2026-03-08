import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list=[]
no_letters=int(input("How many letters would you like in your password?"))
no_symbols=int(input("How many symbols would you like in your password?"))
no_digits=int(input("How many digits would you like in your password?"))
for i in range(no_letters):
    password_list.append(random.choice(letters))
for i in range(no_digits):
    password_list.append(random.choice(numbers))
for i in range(no_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
final_password=""
for char in password_list:
    final_password+=char
print(f"Your final password {final_password} is ready!")