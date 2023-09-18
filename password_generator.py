#Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for letter in range(0, nr_letters + 1):
  i = random.randint(0, len(letters) - 1)
  password = password + letters[i]

for symbol in range(0, nr_symbols + 1):
  j = random.randint(0, len(symbols) - 1)
  password = password + symbols[j]

for number in range(0, nr_numbers + 1):
  k = random.randint(0, len(numbers) - 1)
  password = password + numbers[k]

shuffled = list(password)
random.shuffle(shuffled)
shuffled_pass = ''.join(shuffled)

print(shuffled_pass)
