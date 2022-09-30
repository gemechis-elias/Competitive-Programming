def gradingStudents(grades):
    for item in range(len(grades)):
        if grades[item]>=38:
            num1=grades[item]//5
            num2=(num1+1)*5-grades[item]
            if num2<3:
                grades[item]=(num1+1)*5
    return grades
