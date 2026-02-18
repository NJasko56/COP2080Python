from Menu import*
#imports menu.py file

mainMenu = Menu()
mainMenu.addOption("Check avaliable memory")
mainMenu.addOption("View network connections")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")
#Adds the options for the menu to display

while (True):
#A loop that is always true to allow user to enter multiple options during the same session
    num = 1
    for mainMenu._option in mainMenu._options:
        print(num, mainMenu._option)
        num = num+1
        #Displays all options using a for statement and an int variable to number them
    mainMenu.getInput()
    #Calls methods from the menu class to gather the user input and runs based on the input
    if(mainMenu.run_bash_cmd() == False):
        break
    #checks to make sure user didn't enter quit
    
    
    

