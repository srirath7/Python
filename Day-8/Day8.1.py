#Fucntions with inputs
#Arguements and parameters

# part-1: Greet function

def Hi():
    Name = input("What is your name?: ")
    print("Hi!", Name)
    Place = input("Where you living?: ")
    print("Hope ",Place," is a very good one.")
    Ur = input("What is your job?: ")
    print("Really!", Ur,'is great work' )  
Hi()


# # Simple Inputs
def greet(Name):
    print(f"Hello {Name}")
    print(f"How are you? {Name}")
greet("Sri")

# Multiple inputs
def Hi(Name, Place, Ur):
    print(f"Hi! {Name}")
    print(f"Hope {Place}"," is a very good one.")
    print(f"Really! {Ur}",'is great work' )  
    print(f'{Name}')
Hi("Sri", "Tadipatri", "Software")

# Multiple inputs
def Hi(Name="Sri", Place="Tadipatri", Ur="Software"):
    print(f"Hi! {Name}")
    print(f"Hope {Place}"," is a very good one.")
    print(f"Really! {Ur}",'is great work' )  
    print(f'{Name}')
Hi()