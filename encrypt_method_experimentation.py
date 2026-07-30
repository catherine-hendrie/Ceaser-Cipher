#Catherine Hendrie
#July 28 2026
#Experimentation

import re

#Getting User Input
birthday = input("Please enter your birthday (dd/mm/yyyy):")
word = input("Please enter your desired encrypted word:")

parts = re.findall(r"\d+", birthday)
birthday_num = 0 

for unit in parts:
    int_unit = int(unit)
    birthday_num = birthday_num + int_unit

encrypt = ""
str_new_birthday_num = str(birthday_num)

for letter in word: 
    upper_letter = letter.upper()
    number = (ord(upper_letter)) - ord("A")
    new_number = number + birthday_num
    wrap_num = new_number % 26
    final_num = wrap_num + ord("A")
    encrypt_letter = (chr(final_num))
    encrypt = encrypt + encrypt_letter + str_new_birthday_num

print(encrypt)