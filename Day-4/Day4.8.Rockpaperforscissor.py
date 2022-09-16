# Rock, Paper and Scissor
print("Let's play Rock, Paper and Scissor game! ")
Mine = input("What fo you want to select? 'R', 'P' or 'S':" ).lower()
if Mine == "r":
    Mine=0  
elif Mine == "p":
    Mine=1
else:
    Mine=2

if Mine == 0:
    M="Rock"
elif Mine == 1:
    M="Paper"
else:
    M="Scissor"

#print(Mine)
print("Mine: ",M)

    
import random
computer = random.randint(0, 2)

if computer == 0:
    c="Rock"
elif computer == 1:
    c="Paper"
else:
    c="Scissor"

print("computer: ",c)
#print(computer)

if Mine == computer :
    print("It's a Draw!")
elif Mine == 0 and computer == 1:
    print("computer won!")
elif Mine == 1 and computer == 2:
    print("computer won!")
elif Mine ==2 and computer == 0:
    print("computer won!")
else:
    print("Congrats! You won!") 
    