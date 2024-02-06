#Caeser Cipher encryption
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
type = input("Type'encode' to : ")
text = input("text: ").lower()
shift = int(input("Number shift: "))
if type == 'encode':  
    def cal():
        encoded = ""
        for letter in text:
            position =  alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            encoded += new_letter
        print(encoded)
    cal()   
else:
    print("Error! of encode/decode")
    
type = input("Type'decode' to : ")
shift2 = int(input("Number shift: "))

if type == 'decode':
    def cal():
        decoded = ""
        for letter in text:
            position =  alphabet.index(letter)
            new_position = position + shift2
            new_position1 = new_position - shift
            new_letter = alphabet[new_position1]
            decoded += new_letter
        print(decoded)
    cal()
else:
    print("Error! of encode/decode")
    
