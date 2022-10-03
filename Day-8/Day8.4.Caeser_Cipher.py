#Caeser Cipher encryption
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# direction = input("type 'encode' to encrypt:\n ")
text = input("Type your message:\n ").lower()
shift = int(input("Type of shift number:\n "))


def encrypt():
    cipher_text= ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'{cipher_text}')
encrypt()