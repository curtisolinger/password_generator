#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

character_type = ['letters', 'numbers', 'symbols']
letters_count = numbers_count = symbols_count = 0
password = []
password_length = nr_letters + nr_symbols + nr_numbers

for i in range(password_length):
  while True:
    char = random.choice(character_type)
    if char == 'letters' and letters_count < nr_letters:
      password.append(random.choice(letters))
      letters_count += 1
      break
    elif char == 'symbols' and symbols_count < nr_symbols:
      password.append(random.choice(symbols))
      symbols_count += 1
      break
    elif char == 'numbers' and numbers_count < nr_numbers:
      password.append(random.choice(numbers))
      numbers_count += 1
      break

print(''.join(password))