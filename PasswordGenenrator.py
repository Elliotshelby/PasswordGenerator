import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!', '@' ,'#' ,'*', '$', '%', '&', '+', '-']
print("!! Welcome to the password generator !!")
letter_count=int(input("How many letter would you like in your password\n"))
number_count=int(input("How many numbers would you like in your password\n"))
symbol_count=int(input("How many symbols would you like in your password\n"))
password_list=[]
for char in range(0,letter_count):
  password_list.append(random.choice(letter))
for char in range(0,number_count):
  password_list.append(random.choice(numbers))
for char in range(0,symbol_count):
  password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
  password+=char
print(f"Your password is : {password}")
