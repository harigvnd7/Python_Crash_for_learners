# #list and coding

dogs = ["Simba","Laika","Messi","Bucky","Franky"]              #assigning values into list is with [] brackets
random_list = ["Lionel Messi",10,True]                         #lists can also include numbers or boolean or a mix of it
print(dogs)                                                    #this will print the entire list of dogs
print(dogs[2])                                                 #this will print the entry at index 2 in the list
print(dogs[1:])                                                #this will print all entries from index 1 to end of list
print(dogs[2:4])                                               #this will print entries from index 2 and 3, but won't include 4
print("" + random_list[0] + " wears number " + str(random_list[1]))
print("Is " + random_list[0] + " the Greatest of all time ? - " + str(random_list[2]))

#some of the common functions associated with lists
#important to remember that any list modifications should be done outside print command, or else program will display None as result. Any other list functons can be combined with print()

dogs.extend(random_list)                                       #adds random_list to the end of dogs list
print(dogs)
dogs = ["Simba","Laika","Messi","Bucky","Franky"]
dogs.append("Ceaser")                                          #Ceaser is added to the end of the dogs list
print(dogs)
random_list.insert(1,"Barcelona")               #Inserts another element similar to append function, but at the position we want to
print(random_list)
random_list.remove(True)                                       #Removes the entry mentioned by user from List
print(random_list)
dogs.clear()                                                   #completely clears the list
print(dogs)
dogs = ["Simba","Laika","Messi","Bucky","Franky","Ceaser"]     #re-defining dogs list after clearing in previous command
print(dogs.pop())                                              #prints last element in list, here Ceaser
dogs.pop()                                                     #pop function here removes the last entry in the list, so now Franky will be removed but rest of the list will be displayed
print(dogs)
print(dogs.index("Laika"))                                     #to print position of a  certain entry in list, if any wrong entries index is asked, it will be shown as a error


# #lets use 2 new lists
friends = ["Tony","Adesh","Jerin","Tony","Juna","Shaun","Akhil","Augustine","Sajo","Dominic","Renjith","Manuel","Eldho","Antony","Aswin","Anto"]
roll_number = [1,10,8,7,4,88,4,875,5,3,56,4,2,4,6,4,2,2,2]
print(friends.count("Tony"))                                   #counts the number of times an entry is in a list
friends.sort()                                                 #sorts the list in alphabetical order
roll_number.sort()                                             #sorts the list of numbers in ascending order
print(friends)
print(roll_number)
roll_number.reverse()                                          #reverses the list
new_friends = friends.copy()                                   #copies one list into another list
print(roll_number)
print(new_friends)

#Nested lists

nested_list = [friends,roll_number]                            #we have a nested list whose entries are also lists
print(nested_list)


#Tuples
coordinates = (122.2,83)                                       #Tuples are similar to lists but the entries cannot be modified later. The data inside tuple will be fixed.
print(coordinates)
print(coordinates[0])                                          #prints first entry of tuple

#coordinates[0]=100                                            #this statement will show error as we are trying to modify  tuple


#2D lists

colours = [                                                    #this is a 2d list or an array, it has lists at each entries
    ["Black","White","Blue"],
    ["Yellow","Orange","Red"],
    ["Pink","Green","Violet"],
    ["Grey","Indigo"]
]