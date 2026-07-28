#Catherine Hendrie
#July 27/28 2026
#Ceaser Cipher

word = input(" ")

encrypt = ""

for letter in word: 
    upper_letter = letter.upper()
    number = (ord(upper_letter)) - ord("A")
    new_number = number+3
    wrap_num = new_number % 26
    final_num = wrap_num + ord("A")
    encrypt_letter = (chr(wrap_num))
    encrypt = encrypt + encrypt_letter

print(encrypt)