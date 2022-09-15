# Pizza billing project
#Small pizza : $15
#Medium Pizza: $20
#Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size Pizza:+$1

print("Welcome to Python Pizza Deliveries!")
S = 15
M = 20
L = 25

SP = 2
MLP = 3
C =1

size = str(input("what size of Pizza do you want? S, M or L: "))
add_pepperoni = str(input("Do you want pepperoni(Y or N)? "))
extra_cheese = str(input("Do you want cheese(Y or N)? "))

if size=="S":
    bill = S
    if add_pepperoni == "Y":
        bill +=SP
        if extra_cheese == "Y":
            bill +=C
            print(f"your bill is ${bill}")
        else:
            print(f"your bill is ${bill}")
    else:
        print(f"your bill is ${bill}")
elif size=="M":
    bill = M
    if add_pepperoni == "Y":
        bill +=MLP
        if extra_cheese == "Y":
            bill +=C
            print(f"your bill is ${bill}")
        else:
            print(f"your bill is ${bill}")
    else:
        print(f"your bill is ${bill}") 
elif size=="L":
    bill = L
    if add_pepperoni == "Y":
        bill +=MLP
        if extra_cheese == "Y":
            bill +=C
            print(f"your bill is ${bill}")
        else:
            print(f"your bill is ${bill}")
    else:
        print(f"your bill is ${bill}")      
else:
    print(f"your bill is ${bill}")
