#Here we see how to define a class
#A class is a coder defined data type, which can have as many attributes as the coder wants, eg it can have int,float,boolean,string attributes to
#clearly define what that class represents. The class will be called by a program code, which will assign an object to a class.We will see what that does in the object file

class player_info:                                                 #here we have defined a class
    def __init__(self, name, team, position, number, injured):     #here we have defined a initialise function. In the brackets, write self first to self initialise with the values the user enters later into the object in another code where this class will be called
        self.name = name
        self.team = team
        self.position = position
        self.number = number
        self.injured = injured                                     #this self.xxx is a way of initialising the values

    def availability(self):                                        #this is an object function which is defined inside the class
        if self.injured:
            print("Player is not available due to injury")
        else:
            print("Player is healthy and available")


class club_info:                                                   #here we defined a second class club_info and initialised as before
    def __init__(self, name, league, players, champion):
        self.name = name
        self.league = league
        self.players = players
        self.champion = champion



#goto objects and Objects function file for seeing how these are called