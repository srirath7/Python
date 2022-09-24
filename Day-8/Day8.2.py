import math


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("cover of wall: "))

def paint_calc(height=test_h, width=test_w, cover=coverage):
    cans = height*width/cover
    Total_cans = math.ceil(cans)
    print(f"{Total_cans} no.s req.")
paint_calc()
