student_scores = {
"Harry"     :100,
"Johnson"   :88,
"Berus"     :72,
"Songoku"   :61,
"Ginnga"    :55,
"Naruto"    :47,
"ashcathum"  :35,
"Tom"       :28,
"Oggy"      :14,
"Dexter"    :7,    
}

for score in student_scores:
    if student_scores[score] >= 90:
        print(f'{score} is Outstanding')
    elif  70 <= student_scores[score] < 90:
        print(f'{score} is Exceeds Expectations')
    elif  40 <= student_scores[score] < 70:
        print(f'{score} is Acceptable')
    elif  35 <= student_scores[score] < 40:
        print(f'{score} is Average')
    else:
        print(f'{score} is poor performance')    
print(student_scores[score])