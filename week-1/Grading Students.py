def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i]>=38:   #checking if grade is above 38
            x=grades[i]//5   #Floor devision 
            difference=(x+1)*5-grades[i]    #calculating difference
            if difference<3:
                grades[i]=(x+1)*5
    return grades
