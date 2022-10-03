import random
a = random.randint(1204, 9999)
print(a)
c = input("resend or stop: ")
while c == "resend":
    if c == "resend":
        a = random.randint(1204, 9999)
        print(a)
        c = input("resend or stop: ")
    else:
        print("Bye!")
