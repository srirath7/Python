# Nested ifelse statement with if we use if conditions

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = int(weight/height**2)
print(BMI)

if BMI<18.5:
    print("underweight")
    if 18.5<BMI<25:
        print("Normalweight")
    else :
        print("Overweight")
else:
    print("Obese")
#complicated code to use nested


# So instead of this we use
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = int(weight/height**2)
print(BMI)

if BMI<18.5:
    print("underweight")
elif 18.5<BMI<25:
    print("Normalweight")
elif 25<BMI<30:
    print("Overweight")
else:
    print("Obese")
    
#Tickets selling
B = int(input("what's your age?"))
print(B)

if B<=12:
    print("You need to pay $5")
elif 12<B<18:
    print("You need to pay $7")
else:
    print("You need to pay $12")
