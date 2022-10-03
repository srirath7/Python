def function():
    a = int(input("select number: "))
    while 0==0:
        k = input("'+ - * /' select symbol: ")
        b = int(input("select number: "))
        if k == "+":
            c = a + b
        elif k == "-":
            c = a - b
        elif k == "/":
            c = a / b
        else:
            c = a * b
        print(f" Total is : {c}")
        # l = input("close or continue: ")
        # if l == "continue":
        #     a=c
        # else:
        #     a=0
        a=c
function()