# Password Generator
# Asks for inputs and generates a randomized password. Not Guessable

import random


# creating lists needed for the password combination

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'J', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '=', '^']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


num_letters = int(input("Welcome to the MarcPassword Generator!\n How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))


## Easy Level
#password = ""  

#for char in range(1, num_numbers + 1):
   # password += random.choice(numbers)
    
#for char in range(1, num_letters + 1):
  #  password += random.choice(letters)
    
#for char in range(1, num_symbols + 1):
#    password += random.choice(symbols)
    

#print(password)
   # print(password_combination)
    
    
    
    #Hard Level
    #creating a list

password_list = []


for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))  # .append works the same as +=
    
for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)    # .shuffle() randomizes everything at once
    

  # initializes an empty variable that will contain the final password

password = ""

for char in password_list:
    password += char
    
    
print(f"Your Password is {password}")