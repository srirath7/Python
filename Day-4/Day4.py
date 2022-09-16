# sample variable to Day4.2.py

pi = 'bangalore'
print(pi)
import random

first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))


print(group)