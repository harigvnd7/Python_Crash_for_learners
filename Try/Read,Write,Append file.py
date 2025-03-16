# We can read information from an external file in python using open function

player_numbers = open("Player Details","r" )                               #here player_numbers is a varible into which information from the file Player Details will be stored in code,
                                                                           #"r" means, the file will be opened in read only mode,
                                                                           #"w" means writing mode, where the file's data can be re-written
                                                                           #"a" means append, where more info can can be appended with the file,but existing data cant be modified
                                                                           #"r+" means both read and write mode

print(player_numbers.readable())                                           #this will print Boolean output, depending on whether the file was opened in read mode or not
print(player_numbers.read())                                               #this will print the information in the file
print(player_numbers.readline())                                           #this will print the line where the cursor is at in the file, so here its the first readline() print, so 1st line will be printed each time this code reaches here
print(player_numbers.readline())                                           #this will print the second line of file, as this is the second readline()
print(player_numbers.readlines())                                          #this will print all the lines in the file in the form of an array
#the above line can also be done as a for loop
for p_n in player_numbers.readlines():                                     #this will print out each info in the file, similar output to read() function before
    print(p_n)                                                             #important to know that if all the above code is written together, after the first read() is executed,
                                                                           #the cursor point in the file will be at the end, so the rest of the functions readline(), readlines()
                                                                           #and for loop will not give any output. Try commenting out one line of code above, before executing any line for the result

player_numbers.close()                                                     #always remember to close the file


''' Now let us look into writing and appending a file'''
Spain_players = open("player_list","w")                                    #here we are trying to open a file into the variable with writing mode.
                                                                           #We have not yet prepped a file player list, so the program code will thus generate a new file on its own.
                                                                           #if we had opened an exisitng file such as Player details from above, then that particular file will be opened and we could write to that file too.
Spain_players.write("Rodri - CDM")                                         #here when we run the code, a new file will be created with the entry given. this file will be displayed on the left panel under current projects
                                                                           #when using write or append, we need to be careful because each time a code is run, the entry will keep on adding to the file on the line were the cursor is in that file
Spain_players.write("\nMorata - ST")                                       #here we give a new entry, but use the '\n' command to move to the next line in the file before writing.

Spain_players.close()                                                      #important to close the file


'''Appending'''
Spain_players=open("player_list","a")                                      #opened in append mode
Spain_players.write("\nIsco - CAM")                                        #appending one new entry at the end
Spain_players.write("\nPedri - CM\nGavi-CM\nNico - LW\nLamine - RW")       #appending new set of entries to file. Each time this program is done, the code will re write the file.
Spain_players.close()
