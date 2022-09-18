student_scores = [1, 2, 3]
#student_scores = sorted(student_scores) # to print sort
# print(student_scores)
# instead of using max
#n = max(student_scores)
# print(n)
h = 0
for score in student_scores:
    if score > h:
        h = score
print(h)
