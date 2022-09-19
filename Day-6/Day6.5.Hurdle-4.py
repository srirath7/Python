# Hurdle-4
# Part-1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def around():
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if not wall_in_front():
        move()
        turn_right()
    elif wall_in_front()==True:
        around()
    else:
        break
    
# Part-2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def around():
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    elif wall_in_front()==True:
        turn_left()
    else:
        break    