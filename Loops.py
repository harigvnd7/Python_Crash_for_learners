# let us see how 'while loops' work with the help of a simple guessing game

secret_word = "Barcelona"                                          #we set a secret word to be guessed by user
guess = ""                                                         #initialise the guess string with just ""
guess_count = 0                                                    #to count the number of guesses user has made
guess_limit = 4
out_of_guesses = False                                             #to check later if the guess limit has been reached. Initially set as False

while guess!= secret_word and not(out_of_guesses):                 #while loop will run until the correct word is guessed by user or until the guess limit is not reached
    if guess_count <= guess_limit:                                 #if statement to check if guess limit is reached, here user can make upto 5 guesses
        guess = input("Enter your guess: ")
        guess_count += 1                                           #after each iteration, the guess count has to be incremented
    else :
        out_of_guesses = True                                      #if guess count is finally at limit, the boolean becomes True


if not(out_of_guesses):                                            #this if statement is to ensure the win comment is only if guess is right. The other condition where the program breaks out of while loop is when the guess limit is reached, that should not give win statement to user
    print("You WIN!!")
else :                                                             #if out_of_guesses is true then its also a loss to user
    print("Your are out of guesses. YOU LOSE!!")



#let us discuss 'for loops'

places = ["Angamaly","Fort Kochi","Marine Drive"]
word = "Champion"
for place in places:                                               #this will print every element in list one by one
    print(place)
for letter in word:                                                #this will print each letter in word one by one
    print(letter)
for i in range(len(places)):                                       #this means i will go to each term in list from 0th position to last position excluding the value of len(places)
    print(i)                                                       #if we just print i, it will only give the index position
    print(places[i])                                               #this will print entries from list at the index i

#let us write a function to calculate exponent using for loop
def exponent_function(base,power):
    result = 1
    for i in range(power):
        result = base * result
    return result
print(exponent_function(10,10))

#'Nested for loop'
colours = [
    ["Black","White","Blue"],
    ["Yellow","Orange","Red"],
    ["Pink","Green","Violet"],
    ["Grey","Indigo"]
]

for row in colours:                                                #this will print the elements in the list one by one, each element will be a list on its own
    print(row)
    print(row[0])                                                  #this will print the corresponding entry at 0th position for each row each time
    print(colours[0])                                              #this as we saw in lists will always print the 0th entry in the total list
    for column in row:                                             #this will print all the entries in the list one by one as individual entries
        print(column)
        