#Excercise of calculating average height
student_heights=input("Input a height of students using commas:").split()
# to get lists
print(student_heights)

#instead of sum
total_height = 0
for h in student_heights:
#    print(h)
    total_height += int(h)

print(total_height)

# instead of len
total_number = 0
for n in student_heights:
#    print(n)
    total_number += 1
print(total_number)

print(total_height,"%",total_number,"=" )

print(int(total_height/total_number))