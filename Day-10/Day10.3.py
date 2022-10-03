# Excercise is about year whether is LEAP YEAR or not
year = int(input("which year do you want to check? "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 ==0 :
            return=True
        else :
            return=False
    else:
        return=False
else:
    return=False
    
# Better to use flow chart in https://draw.io 