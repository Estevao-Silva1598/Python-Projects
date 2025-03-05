letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

#Empty password
password_list = []

#Gather the letters
for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

#Gather the symbols
for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

#Gather the numbers
for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

#Now whe need to reorder the password
random.shuffle(password_list)

#The password in a string
password = ""

#Transform the list into a string
for char in password_list:
    password += char

#Print the final password
print(f"The generated password is: {password}")