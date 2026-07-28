#Catherine Hendrie
#July 28 2026
#Experimentation

import math
import re

#Getting User Input
birthday = input("Please enter your birthday (dd/mm/yyyy):")
word = input("Please enter your desired encrypted word:")

parts = re.findall(r"\d+", birthday)
birthday_num = 0 

for parts in birthday:
    new_birthday_num = birthday_num + parts 

encrypt = ""

for letter in word: 
    upper_letter = letter.upper()
    number = (ord(upper_letter)) - ord("A")
    new_number = number+new_birthday_num
    final_num = wrap_num + ord("A")
    encrypt_letter = (chr(wrap_num))
    encrypt = encrypt + encrypt_letter +new_birthday_num

print(encrypt)