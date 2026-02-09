#Checks input to determine the minimum grade number
def checkMin(w, x, y, z):
    min = 4.00

    if(w<min):
        min = w
    if(x<min):
        min = x
    if(y<min):
        min = y
    if(z<min):
        min = z
    return min

#Uses inputs to find the average grade number
def average3(w, x, y, z):
    minimum = checkMin(w, x, y, z)
    total = w + x + y + z - minimum
    if checkCurve(w, x, y, z) == False:
        return (total/3)
    else:
        return ((total/3)+0.25)

#Converts letter grades to numbers
def gradeToNumber(letter):
    if letter == 'A$':
        letter = 4.00
    elif letter == 'A-$':
        letter = 3.67
    elif letter == 'B+$':
        letter = 3.33
    elif letter == 'B$':
        letter = 3.00
    elif letter == 'B-$':
        letter = 2.67
    elif letter == 'C+$':
        letter = 2.33
    elif letter == 'C$':
        letter = 2.00
    elif letter == 'C-$':
        letter = 1.67
    elif letter == 'D+$':
        letter = 1.33
    elif letter == 'D$':
        letter = 1.00
    elif letter == 'D-$':
        letter = 0.67
    elif letter == 'F$':
        letter = 0.00
    return letter
    
#Prints letter grade based on number grade
def numberToGrade(num):
    if num < 0.67:
        return "F"
    elif num < 1.00:
        return "D-"
    elif num < 1.33:
        return "D"
    elif num < 1.67:
        return "D+"
    elif num < 2.00:
        return "C-"
    elif num < 2.33:
        return "C"
    elif num < 2.67:
        return "C+"
    elif num < 3.00:
        return "B-"
    elif num < 3.33:
        return "B"
    elif num < 3.67:
        return "B+"
    elif num < 4.00:
        return "A-"
    else:
        return "A"
    
#checks input to make sure input letter grade is valid
def checkLetter(letter):
    status = False
    if letter == 'A$':
        status = True
    elif letter == 'A-$':
        status = True
    elif letter == 'B+$':
        status = True
    elif letter == 'B$':
        status = True
    elif letter == 'B-$':
        status = True
    elif letter == 'C+$':
        status = True
    elif letter == 'C$':
        status = True
    elif letter == 'C-$':
        status = True
    elif letter == 'D+$':
        status = True
    elif letter == 'D$':
        status = True
    elif letter == 'D-$':
        status = True
    elif letter == 'F$':
        status = True
    return status
    
#Checks grades to see if curve is necessary
def checkCurve(w, x, y, z):
    if w < 2.67 and x < 2.67 and y < 2.67 and z < 2.67:
        return True
    else:
        return False