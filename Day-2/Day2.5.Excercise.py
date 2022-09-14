# Mathematical Excercise
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