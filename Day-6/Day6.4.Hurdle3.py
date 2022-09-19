<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>

# Hurdle-3
def turn_right():
    turn_left()
    turn_left()
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
    elif wall_in_front()==True:
        jump()
    else:
        break