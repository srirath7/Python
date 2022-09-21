import random

F = ["Apple", "Watermelon", "Orange", "Pear", "Cherry", "Strawberry", "Grape", "Mango", "Blueberry", "Pomegranate"]
C = ["red", "green", "blue", "yellow", "orange", "Voilet", "grey", "pink","indigo"]

select = input("What do you like to find? \n   ~Fruits \n   ~Colours\n choose one of above:").lower()
if select == "fruits":
    words = F
else:
    words = C

for word in words:
    word = random.choice(words).lower()

x = word
#print(x)
#Guess
for m in range(0, len(word)+1):
    m = m
y = m
print("Letters are", m)
print("Find out the ", select,":")

z = " "
for z in word:
    z = m *"_"
print(z)



n = str.replace( input(""),z, x)

while n != word :
    print("your guess is wrong")
    n = str.replace( input("   "),z, x)
else:
    print("your guess is right. Congrats!") 
