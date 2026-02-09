##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
# code here
grades = {} 

  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
  # code here
while True:
    User = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit?")



   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
   # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
   # code here
    if User.upper() == 'A':
        name = str(input("Enter the name of the student: "))
        if name == grades:
            print("Sorry, that student is already present.")
        else:
            ofstudent = int(input("Enter the student's grade: " ))
            if ofstudent>100 or ofstudent< 0:
                print("Please enter grade as number 0-100")
            else:
                grades[name] = ofstudent
   # Handle removing a student if user inputs 'R'
   # Check input for "What student do you want to remove? "
   # use pop to remove key/value form grades
   # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
   # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
   # code here
    if User.upper() == 'R':
        removal = input("What student do you want to remove? ")
        ready = False
        for grade in grades:
            if removal == grade:
                ready = True
        if ready == True:
            grades.pop(removal)
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")
        ready = False
   # Handle modifying a student grade if user inputs 'M'
   # "Enter the name of the student to modify: "
   # Convert grade into integer
   # If student is in grades dictionary, show existing grade "The old grade is"
   # Gather input for new grade "Enter the new grade: "
   # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
   # code here
    if User.upper() == 'M':
        change = False
        modify = input("Enter the name of the student to modify: ")
        for grade in grades:
            if modify == grade:
                change =True
        if change == True:
            print('The old grade is ', grades[modify])
            grades[modify] = int(input("Enter the new grade: "))
        else:
            print("Sorry, that student doesn't exist and couldn't be modified.")
        change = False
   # Handle printing grade average as a string if user input is 'P'
   # Use "The average grade is "
   # Handle printing all of the student names with associated grade
   # Display explictly as strings
   # code here
    elif User.upper() == 'P':
        average = 0.0
        count = 0
        for grade in grades:
            
            average += grades[grade]
            count += 1
        average = average/count
        print(f'The average grade is {average}')
        print(grades)
      

   # Handle the case for quiting if user inputs 'Q' "Goodbye!"
   # code here
    elif User.upper() == 'Q':
        print("Goodbye!")
        break

   # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
   # code here
    #else:
        #print("Sorry, that wasn't a valid choice.")
        #continue

