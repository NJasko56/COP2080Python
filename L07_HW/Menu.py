import os


class Menu:

    def __init__(self):
        self._options = []
        self._choice = ()
        #Initializes objects with an empty list for options and an empty variable for the user's choice
        
        
    
    def addOption(self, option):
        self._options.append(option)
        #Used to add options to the menu

    @classmethod
    def getInput(self):
        self._choice = input()
        #A method to gather user input
        
        
        
    @classmethod
    def run_bash_cmd(self):
        print('-' * 80, '\n')
        print('You entered #', self._choice)
        if (self._choice == '1'):
            print('The available memory is ')
            os.system('free -tmh')
            print('\n', '-' * 80, '\n')
        elif (self._choice == '2'):
            print('The current network connections include: ')
            os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
            print('\n', '-' * 80, '\n')
        elif (self._choice == '3'):
            print('Available file space is: ')
            os.system('df -h | grep \"Filesystem\|root\"')
            print('\n', '-' * 80, '\n')
        elif (self._choice == '4'):
            return False
        elif (self._choice != '4'):
            print("Please enter an integer 1-4")
        return






    

    