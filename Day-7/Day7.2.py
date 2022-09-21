F = ["Apple", "Watermelon", "Orange", "Pear", "Cherry", "Strawberry", "Grape", "Mango", "Blueberry", "Pomegranate"]
C = ["red", "green", "blue", "yellow", "orange", "Voilet", "grey", "pink","indigo"]

select = input("What do you like to find? \n   ~Fruits \n   ~Colours\n choose one of above:").lower()
if select == "fruits":
    words = F
else:
    words = C


print(words)