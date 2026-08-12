#Catherine Hendrie
#Tuesday Aug11
#Python Encrypter/Decrypter
#Ceaser Sipher

purpose = input("Whould you like to encrypt or decrypt?")

if purpose == "encrypt" or "Encrypt" or "ENCRYPT" or "encript" or "enrypt" or "ENcrypt" or "encrypte" or "ENCRYPTE":
    word = input("What word would you like to encrypt:")

    encrypt = ""

    for letter in word: 
        upper_letter = letter.upper()
        number = (ord(upper_letter)) - ord("A")
        new_number = number+3
        wrap_num = new_number % 26
        final_num = wrap_num + ord("A")
        encrypt_letter = chr(final_num)
        encrypt = encrypt + encrypt_letter

    print(f"Your word is {encrypt}")

elif purpose == "decrypt" or "DECRYPT" or "Decrypt" or 'decript' or "derypt" or "DEcrypt" or "decrypte" or "DECRYPTE" or "decrypte?":
    word = input("What word would you like to decrypt:")

    decrypt = ""

    for letter in word: 
        upper_letter = letter.upper()
        number = (ord(upper_letter)) - ord("A")
        new_number = number-3
        wrap_num = new_number % 26
        final_num = wrap_num + ord("A")
        decrypt_letter = chr(final_num)
        decrypt = decrypt + encrypt_letter

    print(f"Your word is {decrypt}")