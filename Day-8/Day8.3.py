#Prime number calculation

def prime_number():
    p = int(input("choose a Number: "))
    if p==1 or p==2 or p==3 :
        print("Prime")
    elif p%2==0 or p%3==0:
        print("Non-prime")
    else:
        print("Prime")
while 0==0:
    prime_number()