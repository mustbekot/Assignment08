#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# MKot, 2022-Dec-03, added code
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = int(cd_id)
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    @property
    def cd_id(self):
      return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    Properties:

    Methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of inventories.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            None.
        """
        lstOfCDObjects.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = CD(data[0],data[1],data[2])
                lstOfCDObjects.append(dicRow)
            objFile.close()
        except FileNotFoundError as e:
             print('Data file does not exist')
             print(e.__doc__)
        except Exception as e:
             print('General Error')
             print(e.__doc__)
        
    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Save inventory to the file.

        Args:
            file_name (string): name of file where data is saved to
            lst_inventory (list): list that holds the data that needs to be saved.

        Returns:
            None.
        """
        # TODone Add code here
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            lstValues = []
            lstValues.extend([row.cd_id, row.cd_title, row.cd_artist])
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
               

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Handling Input / Output
    
    Properties:
    
    Methods:
        print_menu(): None
        menu_choice(): None
        show_inventory(): None
        add_data(): (a cd_data object)
    """
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(lstOfCDObjects):
        """Displays current inventory table

        Args:
            lstOfCDObjects (list): list that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstOfCDObjects:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')
 
    # TODone add code to get CD data from user
    @staticmethod
    def add_data():
        """Gets user input new CD

        Args:
            none

        Returns:
            cd_data (object): an instance of class CD store cd information from user input 
        """
        while True:
           strID = input('Enter ID: ').strip()
           try: 
               strID = int(strID)
               break
           except:
               print('This is not an integer. Try again!')
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        cd_data = CD(strID, strTitle, stArtist)
        return cd_data


# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

while True:   
    # 1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 2. Process menu selection
    # 2.1 process exit first
    if strChoice == 'x':
        break
    # 2.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 2.3 process add a CD
    elif strChoice == 'a':
        cd = IO.add_data()
        lstOfCDObjects.append(cd)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 2.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 2.5 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 2.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
