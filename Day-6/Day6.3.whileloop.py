# while loop
x = 1
while x < 5 :
    x += 1
    print(x)
    
# complete Hurdle2
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def at_goal():
    print("Flag")

while at_goal()==False:
    jump()