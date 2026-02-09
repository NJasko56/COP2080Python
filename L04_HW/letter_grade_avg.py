from grade_compute import*

a, b, c, d = input("Enter grades: ").split()
if checkLetter(a) and checkLetter(b) and checkLetter(c) and checkLetter(d) == True:
    a = gradeToNumber(a)
    b = gradeToNumber(b)
    c = gradeToNumber(c)
    d = gradeToNumber(d)


    #Setup of ASCII grade report summary
    print("----------------------------------------")
    print("|         GRADE REPORT SUMMARY         |")
    print("----------------------------------------")

    avg = average3(a, b, c, d)

    #Report begins here
    print(f"| Grades Entered: {numberToGrade(a)} {numberToGrade(b)} {numberToGrade(c)} {numberToGrade(d)}            |")
    print(f"| Lowest Grade Dropped: {numberToGrade(checkMin(a, b, c, d))}             |")
    print(f"| Calculated Average: {avg}             |")
    print(f"| Final Letter Grade: {numberToGrade(avg)}                |")

    print("----------------------------------------")

else:
    print("Invalid Input")