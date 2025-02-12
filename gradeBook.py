def get_grade(s1, s2, s3):
    get_grade_average = ((s1 + s2 + s3) / 3) #Average
    if 90 <= get_grade_average <= 100:
        return 'A'
    elif 80 <= get_grade_average < 90:
        return 'B'
    elif 70 <= get_grade_average < 80:
        return 'C'
    elif 60 <= get_grade_average < 70:
        return 'D'
    else:
        return 'F'