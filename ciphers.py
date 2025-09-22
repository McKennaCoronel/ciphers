# -------------------------------
# Caesar Cipher Functions
# -------------------------------

# TODO: Write a function to encrypt a message with Caesar Cipher
# Steps:
# 1. Loop through each letter in the plaintext
# 2. Shift the letter by the key (using ASCII or alphabet index)
# 3. Wrap around using modulo (%) if needed
# 4. Return the encrypted text

# TODO: Write a function to decrypt a message with Caesar Cipher
# Hint: This is basically the same, but subtract the shift instead of adding

def caesar_encrypt(plaintext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    for letter in plaintext.upper():
        print(letter)
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted += alphabet[(index + shift) % 26]
        else:
            encrypted += letter
    return encrypted 

def caesar_decrypt(plaintext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    for letter in plaintext.upper():
        print(letter)
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted += alphabet[(index - shift) % 26]
        else:
            encrypted += letter
    return encrypted 
    
# -------------------------------
# Vigenere Cipher Functions
# -------------------------------

# TODO: Write a function to encrypt a message with Vigenere Cipher
# - Define alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# - Initialize an empty string for result
# - Keep track of which letter of the key we’re on (key_index)
# - For each letter in the plaintext:
#     - If the letter is in alphabet:
#         - Find the numeric index of the plaintext letter
#         - Find the numeric index of the current key letter
#         - Add them together, wrap with modulo 26
#         - Convert back to a letter and add to result
#         - Move to the next key letter (use % length of key so it repeats)
#     - Else: just add the character (spaces, punctuation, etc.) unchanged
# - Return the result string

# TODO: Write a function to decrypt a message with Vigenere Cipher
# - Almost the same as encrypt, BUT subtract key value instead of adding

def vig_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    key_index = 0
    for letter in plaintext.upper():
        print(letter)
        if letter in alphabet:
            index = alphabet.index(letter)
            current_key_letter = key[key_index % len(key)]
            shift = alphabet.index(current_key_letter)
            encrypted += alphabet[(index + shift) % 26]
            key_index += 1
        else:
            encrypted += letter
    return encrypted 

def vig_decrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    key_index = 0
    for letter in plaintext.upper():
        print(letter)
        if letter in alphabet:
            index = alphabet.index(letter)
            current_key_letter = key[key_index % len(key)]
            shift = alphabet.index(current_key_letter)
            encrypted += alphabet[(index - shift) % 26]
            key_index += 1
        else:
            encrypted += letter
    return encrypted 

# -------------------------------
# Testing Area
# -------------------------------

# Example Caesar Test
plaintext = "HELLO WORLD. I am a zebra"
shift = 3
print(caesar_encrypt(plaintext, shift))  # Expected: KHOOR ZRUOG
print(caesar_decrypt("KHOOR ZRUOG", shift))  # Expected: HELLO WORLD

# Example Vigenere Test
plaintext = "ATTACK AT DAWN"
key = "LEMON"
print(vig_encrypt(plaintext, key))  # Expected: LXFOPV EF RNHR
print(vig_decrypt("LXFOPV EF RNHR", key))  # Expected: ATTACK AT DAWN


from vigenere import encrypt, decrypt

key = "LEMON"
pt = "ATTACK AT DAWN"

ct = encrypt(pt, key)
rt = decrypt(ct, key)

print("Library Encrypted:", ct)
print("Library Decrypted:", rt)