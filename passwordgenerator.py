import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','%','&','(','*','+']

print("Welcome to the Pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Generate random letters, symbols, and numbers
password_letters = random.choices(letters, k=nr_letters)
password_symbols = random.choices(symbols, k=nr_symbols)
password_numbers = random.choices(numbers, k=nr_numbers)

# Combine all parts
password_list = password_letters + password_symbols + password_numbers

# Shuffle the password list to ensure randomness
random.shuffle(password_list)

# Join the list into a string
password = ''.join(password_list)

print(f"Your generated password is: {password}")