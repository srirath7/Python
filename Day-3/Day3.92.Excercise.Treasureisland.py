print("Welcome to Treasure Island. Your mission is to find the treasure")

next = str(input('you are at a cross road. where do you want to go? "left" or "right": ')).lower()
if next == "left":
    print(next)
    next = str(input('you come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')).lower()
    if next == "wait":
        print(next)
        next = str(input('you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose? ')).lower()
        if next == "yellow":
            print("You Win!")
        elif next == "blue":
            print("Gameover")
        else:
            print("Gameover")
    else:
        print("Gameover")   
else:
    print("Gameover")

#Treasure game####