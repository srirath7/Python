words = ["Apple", "Watermelon", "Orange", "Pear", "Cherry", "Strawberry", "Grape", "Mango", "Blueberry", "Pomegranate"]
import random
import tkinter

choose = random.choice(words)
print(f'solution is {choose}')
display = []
for letter in choose:
    display += "_"
print(display)
    

guess = input("Guess a letter: ")
#for letter in choose:
#    if letter == guess:
#       print("right")
#    else:
#       print("wrong")

for position in range(len(choose)):
    letter = choose[position]
    if letter == guess:
        display[position] = letter
    else:
        display = display
print(display)