# Excercise is about year whether is LEAP YEAR days output can be made.

year = int(input("which year do you want to check? "))

def year1():
    if year%4 == 0:
        if year%100 == 0:
            if year%400 ==0 :
                return True
            else :
                return False
        else:
            return False
    else:
        return False
year1()
leap = year1()
if leap == True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
month1 = int(input("Enter month: "))
month = month1-1   
days = month_days[month]

print(days)

# Better to use flow chart in https://draw.io 