# Caesar Cipher Python Suite

A simple command-line tool written in Python that encodes and decodes text using the Caesar cipher method, including a custom date-based variation.

## Overview

This repository contains Python scripts that use basic math and string manipulation to scramble and unscramble messages. It demonstrates core programming skills like working with ASCII values, loops, and handling user input.

## Features

* **Encrypt and Decrypt:** Shifts letters forward or backward to hide or reveal messages.
* **Case Insensitive:** Automatically changes lowercase letters to uppercase so the math works correctly.
* **Alphabet Wrapping:** Uses math to wrap around the alphabet smoothly from Z back to A.
* **Birthday Shift:** Includes a custom script that uses a date to create a unique shift key.

## Code Example

Here is the core logic used to shift letters forward:

```python
word = "EXAMPLE"
encrypt = ""

for letter in word:  
    upper_letter = letter.upper()
    number = (ord(upper_letter)) - ord("A")
    new_number = number + 3
    wrap_num = new_number % 26
    final_num = wrap_num + ord("A")
    encrypt_letter = chr(final_num)
    encrypt = encrypt + encrypt_letter

print(encrypt)
