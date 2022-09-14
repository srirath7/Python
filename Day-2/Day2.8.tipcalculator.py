#Welcome to the tip calculator.
#What was the total bill? $123.54
#How many people to split the bill? 5
#what percentage tip would you like to give? 10, 12, or 15? 12
#Each person should pay: $27.9


print ("Welcome to the tip calculator.")
a = float(input("What was the total bill? $"))

b = float(input("How many people to split the bill? "))

c = float(input("what percentage tip would you like to give? 10, 12, or 15? "))

print(round(a*(c/100+1)/b,2))
