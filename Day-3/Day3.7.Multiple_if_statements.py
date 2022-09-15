#Multiple rollercoaster check height if it is ok then check amount
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the roller coaster!")
    B = int(input("what's your age?"))
    print(B)
    photo = str(input("You want photo 'yes or no?' "))
    if B<=12:
        if photo == "yes" :
            print("You need to pay $5+$3 = $8")
        else:
            print("You need to pay $5")
    elif 12<B<18:
        if photo == "yes":
            print("You need to pay $7+$3 = $10")
        else:
            print("You need to pay $7")
    else:
        if photo == "yes":
            print("You need to pay $12+$3 = $15")
        else:
            print("You need to pay $12")
else:
    print("Sorry, you have to grow taller to ride.") 
    