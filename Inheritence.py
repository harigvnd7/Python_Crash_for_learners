from Classes import player_info                                                #importing class 'player_info' for inheritence

class transfer(player_info):                                                   #this means the class 'transfer' inherits the class 'player_info' from 'Classes' file

    def wants_transfer(self):                                                  #we are defining seperate function exclusive for this class
        print("Player wants to move to another club")


#goto objects and Objects function file for seeing how these are called