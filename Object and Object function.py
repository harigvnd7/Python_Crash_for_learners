from Classes import player_info                                                                                         #this basically means, I have imported the class 'player_info', from the python file 'Classes', which I have made seperately

from Inheritence import transfer                                                                                        #this is an inherited class that has all attributes of player_info and also its own function

Players = [
    player_info("Pele", "Brazil", "ST", 10,False),                                    #we define each objects as entries of an array
    player_info("Maradona", "Argentina", "CF",7,True),
    player_info("Zidane", "France","CM", 8,False),
    player_info("Busquets", "Spain", "CDM", 5, True),
    player_info("Cryuff", "Netherlands", "CAM", 6,False),
    player_info("Maldini", "Italy", "CB",4, False),
    player_info("Neuer","Germany", "GK",1,True),
    transfer("Pogba","France","CM",13,True),                                         #these are inherited class objects
    transfer("Bellingham","England","CF",20,False),
]


for p in Players:
    print("\n"+ p.name + " plays for "  + p.team + " at " + p.position + " position")
    p.availability()
    if p.injured and p.name[0] == "P" or p.team == "England":
        p.wants_transfer()                                                                                              #this line will only work for the objects who are defined to the class 'transfer'. the rest will show error.
                                                                                                                        #But I have given if statement such that only the right objects will fullfill the criteria and wont cause error


    else:                                                                                                               #this is for the objects not defined by the class 'transfer'. but by just 'player_info'
        print("Player is happy and wants to stay at his current club")



from Classes import club_info                                                                                           #here we have imported another class from the same file

Club1 = club_info("Barcelona","Laliga", 30, True)                                          #here we have assigned ech object seperately,which is different from before, where each object was a list
Club2 = club_info("Real Madrid","Laliga", 28, False)
Club3 = club_info("Manchester City", "EPL", 35, True)
Club4 = club_info("Bayern Munchen", "Bundesliga",32,False)
Club5 = club_info("Inter Milan", "Seria A", 25, True)
print("\n\n\n")
if Club2.champion:
    print(Club2.name + " is the Champion of " + Club2.league)
elif Club2.league == Club1.league and Club1.champion:
    print(Club1.name + " is the Champion of " + Club1.league)