import random
print("Welcome to the Pypassword Generator!")
A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
A1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
B = ["0","1","2","3","4","5","6","7","8","9"]
C = ["!","@","#","$","%","^","&","*","?",".",","]


a = int(input("How many letters would you like? \n"))#12
b = int(input("How many symbols would you like? \n"))#2
c = int(input("How many numbers would you like? \n"))#2
#print("Here is your password: \n",)
#for Easy level
# password = " "

# for x in range(1, a + 1):
# #    A = random.randint(A[n])
#     password += random.choice(A1)
# for x in range(1, b + 1):
#     password += random.choice(B)
# for x in range(1, c + 1):
#     password += random.choice(C)
# print(password)

password = []

for x in range(1, a + 1):
#    A = random.randint(A[n])
    password += random.choice(A1)
for x in range(1, b + 1):
    password += random.choice(B)
for x in range(1, c + 1):
    password += random.choice(C)
random.shuffle(password)

print(f'{password}')

p = " "
for x in password :
    p += x
print(f"Here is your password: \n{p}")