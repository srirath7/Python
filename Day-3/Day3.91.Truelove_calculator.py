# True Love calculator using python Excersice
print("Welcome to the Love calculator")
name1 = input("what's your name?")
name2 = input("what's their name?")

mix_names = name1 + name2
lowercase_string = mix_names.lower()
T = lowercase_string.count("t")
R = lowercase_string.count("r")
U = lowercase_string.count("u")
E = lowercase_string.count("E")

L = lowercase_string.count("l")
O = lowercase_string.count("o")
V = lowercase_string.count("v")
E = lowercase_string.count("e")

score1 = T+R+U+E
score2 = L+O+V+E
score = int(str(score1)+str(score2))
if score <=10:
    print(f"you are like coke and mentos, your score is {score}%")
elif score >=40 and score <=50:
    print(f"you are like alright, your score is {score}%")
else :
    print(f"you are good, your score is {score}%")