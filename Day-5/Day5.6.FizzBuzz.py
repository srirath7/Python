t = 0
for n in range(0, 101):
    if n%3 ==0 and n%5 ==0:
        print("FizzBuzz")
    elif n%3 ==0:
        print("Fizz")
    elif n%5 ==0:
        print("Buzz")
    else:
        print(n)