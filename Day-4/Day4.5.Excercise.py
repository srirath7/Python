# Randomisation of banker roulette
import random
#names_input = input ("names please?")
# split helps to seperate names to Lists ["Angela", "Ben", "Jenny", "Micheal", "Chloe"]
#Names = names_input.split(",")
Names = ["Angela", "Ben", "Jenny", "Micheal", "Chloe"]
count = len(Names) #count = 5
random_number = random.randint(0, count -1)

print(Names[random_number])
