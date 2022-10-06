# Put a treasure in 
    # # #
    # # X
    # # #

a = [" ", " "," "]
b = [" ", " "," "]
c = [" ", " "," "]
map = [a, b, c]
#print(map)
position = (input("where do you want treasure? ")) #23
horizontal = int(position[0]) #2
vertical = int(position[1]) #3
col = map[horizontal-1]
col[vertical-1] = "X" # we can also use map[horizontal-1]
print(f"{a}\n{b}\n{c}")
